from __future__ import annotations

from pathlib import Path
from statistics import median
from zipfile import ZIP_DEFLATED, ZIP_STORED, ZipFile
import xml.etree.ElementTree as ET

from PIL import Image, ImageChops, ImageDraw, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "00_source" / "1648138415955_original.jpg"
USER_CUTOUT = ROOT / "00_source" / "1648138415955_cutout_user.png"
OUT_DIR = ROOT / "03_krita_starter"
LAYER_DIR = OUT_DIR / "layers"
ORA_PATH = OUT_DIR / "takagi_live2d_layer_starter.ora"


def sample_background(img: Image.Image) -> tuple[int, int, int]:
    rgb = img.convert("RGB")
    w, h = rgb.size
    points: list[tuple[int, int, int]] = []
    margin = max(12, min(w, h) // 90)
    for x in range(margin):
        for y in range(margin):
            points.append(rgb.getpixel((x, y)))
            points.append(rgb.getpixel((w - 1 - x, y)))
            points.append(rgb.getpixel((x, h - 1 - y)))
            points.append(rgb.getpixel((w - 1 - x, h - 1 - y)))
    return tuple(int(median(channel)) for channel in zip(*points))


def color_mask(img: Image.Image, predicate) -> Image.Image:
    rgb = img.convert("RGB")
    mask = Image.new("L", rgb.size, 0)
    src = rgb.load()
    dst = mask.load()
    w, h = rgb.size
    for y in range(h):
        for x in range(w):
            if predicate(src[x, y]):
                dst[x, y] = 255
    return mask


def shape_mask(size: tuple[int, int], shapes: list[tuple[str, tuple]]) -> Image.Image:
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    w, h = size
    for kind, data in shapes:
        if kind == "rect":
            x1, y1, x2, y2 = data
            draw.rectangle((x1 * w, y1 * h, x2 * w, y2 * h), fill=255)
        elif kind == "ellipse":
            x1, y1, x2, y2 = data
            draw.ellipse((x1 * w, y1 * h, x2 * w, y2 * h), fill=255)
        elif kind == "poly":
            draw.polygon([(x * w, y * h) for x, y in data], fill=255)
    return mask


def combine(*masks: Image.Image, mode: str = "and") -> Image.Image:
    if not masks:
        raise ValueError("No masks provided")
    out = masks[0].copy()
    op = ImageChops.multiply if mode == "and" else ImageChops.lighter
    for mask in masks[1:]:
        out = op(out, mask)
    return out


def soften(mask: Image.Image, expand: int = 1, blur: float = 0.35) -> Image.Image:
    if expand:
        mask = mask.filter(ImageFilter.MaxFilter(expand * 2 + 1))
    if blur:
        mask = mask.filter(ImageFilter.GaussianBlur(blur))
    return mask


def apply_mask(img: Image.Image, mask: Image.Image) -> Image.Image:
    layer = img.convert("RGBA")
    layer.putalpha(mask)
    return layer


def save_layer(name: str, img: Image.Image, mask: Image.Image) -> Path:
    LAYER_DIR.mkdir(parents=True, exist_ok=True)
    path = LAYER_DIR / f"{name}.png"
    apply_mask(img, soften(mask)).save(path)
    return path


def make_thumbnail(img: Image.Image) -> Path:
    thumb_dir = OUT_DIR / "Thumbnails"
    thumb_dir.mkdir(parents=True, exist_ok=True)
    thumb = img.copy()
    thumb.thumbnail((256, 256))
    path = thumb_dir / "thumbnail.png"
    thumb.save(path)
    return path


def write_ora(width: int, height: int, layer_paths: list[tuple[str, Path, bool, float]], merged: Path, thumb: Path) -> None:
    image = ET.Element("image", {"w": str(width), "h": str(height)})
    stack = ET.SubElement(image, "stack")
    # ORA stack order is bottom to top in many tools. Krita also imports this
    # predictably when each layer is full canvas size.
    for name, path, visible, opacity in layer_paths:
        ET.SubElement(
            stack,
            "layer",
            {
                "name": name,
                "src": f"data/{path.name}",
                "x": "0",
                "y": "0",
                "opacity": f"{opacity:.3f}",
                "visibility": "visible" if visible else "hidden",
            },
        )
    stack_xml = ET.tostring(image, encoding="utf-8", xml_declaration=True)

    ORA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(ORA_PATH, "w") as zf:
        zf.writestr("mimetype", "image/openraster", compress_type=ZIP_STORED)
        zf.writestr("stack.xml", stack_xml, compress_type=ZIP_DEFLATED)
        zf.write(merged, "mergedimage.png", compress_type=ZIP_DEFLATED)
        zf.write(thumb, "Thumbnails/thumbnail.png", compress_type=ZIP_DEFLATED)
        for _, path, _, _ in layer_paths:
            zf.write(path, f"data/{path.name}", compress_type=ZIP_DEFLATED)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    # Prefer the user's manually prepared transparent PNG when available. It
    # preserves similar character colors that were partially removed by the
    # automatic background keying pass.
    img = Image.open(USER_CUTOUT if USER_CUTOUT.exists() else SOURCE).convert("RGBA")
    rgb = img.convert("RGB")
    w, h = img.size
    bg = sample_background(rgb)

    if "A" in img.getbands():
        subject = img.getchannel("A").point(lambda a: 255 if a > 8 else 0).filter(ImageFilter.MaxFilter(3))
    else:
        background = color_mask(
            rgb,
            lambda c: ((c[0] - bg[0]) ** 2 + (c[1] - bg[1]) ** 2 + (c[2] - bg[2]) ** 2) ** 0.5 < 34,
        )
        subject = ImageChops.invert(background).filter(ImageFilter.MaxFilter(5))

    skin = color_mask(rgb, lambda c: c[0] > 210 and c[1] > 165 and c[2] > 145 and c[0] > c[1] >= c[2] - 5)
    hair_color = color_mask(rgb, lambda c: 70 <= c[0] <= 175 and 45 <= c[1] <= 130 and 35 <= c[2] <= 120 and c[0] > c[1] + 8)
    dark = color_mask(rgb, lambda c: 25 <= c[0] <= 105 and 28 <= c[1] <= 110 and 30 <= c[2] <= 120)
    white = color_mask(rgb, lambda c: c[0] > 218 and c[1] > 210 and c[2] > 205)
    gold = color_mask(rgb, lambda c: c[0] > 165 and c[1] > 130 and 45 <= c[2] <= 120 and c[0] > c[2] + 50)

    head_zone = shape_mask((w, h), [("ellipse", (0.29, 0.12, 0.70, 0.58))])
    face_zone = shape_mask((w, h), [("ellipse", (0.31, 0.16, 0.68, 0.53))])
    eyes_zone = shape_mask((w, h), [("rect", (0.33, 0.25, 0.65, 0.39))])
    mouth_zone = shape_mask((w, h), [("ellipse", (0.40, 0.36, 0.61, 0.54))])
    ears_zone = shape_mask((w, h), [("rect", (0.28, 0.01, 0.62, 0.28))])
    left_paw_zone = shape_mask((w, h), [("rect", (0.01, 0.29, 0.36, 0.66))])
    right_paw_zone = shape_mask((w, h), [("rect", (0.62, 0.29, 0.98, 0.66))])
    arms_zone = shape_mask((w, h), [("rect", (0.02, 0.50, 0.98, 0.85))])
    dress_zone = shape_mask((w, h), [("poly", ((0.35, 0.58), (0.67, 0.58), (0.78, 1.0), (0.28, 1.0)))])
    bell_zone = shape_mask((w, h), [("ellipse", (0.44, 0.52, 0.56, 0.65))])
    hair_back_zone = shape_mask(
        (w, h),
        [
            ("poly", ((0.27, 0.16), (0.70, 0.16), (0.72, 0.90), (0.28, 0.90))),
            ("rect", (0.23, 0.36, 0.75, 0.95)),
        ],
    )
    hair_front_left_zone = shape_mask((w, h), [("poly", ((0.30, 0.14), (0.49, 0.13), (0.43, 0.91), (0.25, 0.78)))])
    hair_front_right_zone = shape_mask((w, h), [("poly", ((0.50, 0.13), (0.69, 0.16), (0.76, 0.78), (0.57, 0.91)))])

    layers: list[tuple[str, Path, bool, float]] = []

    def add(name: str, mask: Image.Image, visible: bool = True, opacity: float = 1.0) -> None:
        layers.append((name, save_layer(name, img, mask), visible, opacity))

    # Bottom to top starter stack.
    ref = OUT_DIR / "layers" / "original_reference.png"
    LAYER_DIR.mkdir(parents=True, exist_ok=True)
    img.save(ref)
    layers.append(("original_reference_hide_when_editing", ref, True, 0.22))

    add("hair_back", combine(subject, hair_color, hair_back_zone))
    add("torso_skin", combine(subject, skin, shape_mask((w, h), [("rect", (0.31, 0.50, 0.71, 0.73))])))
    add("dress_base", combine(subject, dark, dress_zone))
    add("arm_L", combine(subject, skin, arms_zone, shape_mask((w, h), [("rect", (0.01, 0.50, 0.46, 0.85))])))
    add("arm_R", combine(subject, skin, arms_zone, shape_mask((w, h), [("rect", (0.55, 0.50, 0.99, 0.85))])))
    add("cat_ear_headband", combine(subject, combine(dark, skin, mode="or"), ears_zone))
    add("head_base", combine(subject, skin, face_zone))
    add("hair_front_L", combine(subject, hair_color, hair_front_left_zone))
    add("hair_front_R", combine(subject, hair_color, hair_front_right_zone))
    add("eye_L", combine(subject, combine(white, dark, mode="or"), eyes_zone, shape_mask((w, h), [("rect", (0.32, 0.25, 0.49, 0.39))])))
    add("eye_R", combine(subject, combine(white, dark, mode="or"), eyes_zone, shape_mask((w, h), [("rect", (0.51, 0.25, 0.67, 0.39))])))
    add("mouth_open_teeth", combine(subject, combine(dark, skin, white, mode="or"), mouth_zone))
    add("choker_bell", combine(subject, combine(dark, gold, mode="or"), bell_zone))
    add("paw_L_base", combine(subject, dark, left_paw_zone))
    add("paw_L_pads_claws", combine(subject, combine(skin, white, mode="or"), left_paw_zone))
    add("paw_R_base", combine(subject, dark, right_paw_zone))
    add("paw_R_pads_claws", combine(subject, combine(skin, white, mode="or"), right_paw_zone))

    cutout = OUT_DIR / "merged_preview_cutout.png"
    apply_mask(img, subject.filter(ImageFilter.GaussianBlur(0.3))).save(cutout)
    thumb = make_thumbnail(img)
    write_ora(w, h, layers, cutout, thumb)

    print(f"Created {ORA_PATH}")
    print(f"Created {len(layers)} layer PNG files in {LAYER_DIR}")


if __name__ == "__main__":
    main()
