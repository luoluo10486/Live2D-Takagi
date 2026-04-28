from pathlib import Path
from statistics import median

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "00_source" / "1648138415955_original.jpg"
OUT_DIR = ROOT / "01_preprocess"


def sample_background(img: Image.Image) -> tuple[int, int, int]:
    rgb = img.convert("RGB")
    w, h = rgb.size
    points = []
    margin = max(8, min(w, h) // 80)
    for x in range(margin):
        for y in range(margin):
            points.append(rgb.getpixel((x, y)))
            points.append(rgb.getpixel((w - 1 - x, y)))
            points.append(rgb.getpixel((x, h - 1 - y)))
            points.append(rgb.getpixel((w - 1 - x, h - 1 - y)))
    return tuple(int(median(channel)) for channel in zip(*points))


def make_cutout() -> Image.Image:
    img = Image.open(SOURCE).convert("RGBA")
    bg = sample_background(img)
    px = img.load()
    w, h = img.size

    # The source has a flat warm background. Keep a soft edge so the cutout
    # stays useful as reference art without creating jagged borders.
    transparent_at = 28
    opaque_at = 82
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            dist = ((r - bg[0]) ** 2 + (g - bg[1]) ** 2 + (b - bg[2]) ** 2) ** 0.5
            if dist <= transparent_at:
                alpha = 0
            elif dist >= opaque_at:
                alpha = a
            else:
                alpha = int(a * ((dist - transparent_at) / (opaque_at - transparent_at)))
            px[x, y] = (r, g, b, alpha)

    out = OUT_DIR / "takagi_cat_pose_cutout.png"
    img.save(out)
    return img


def make_region_guide() -> None:
    img = Image.open(SOURCE).convert("RGB")
    draw = ImageDraw.Draw(img, "RGBA")
    w, h = img.size
    try:
        font = ImageFont.truetype("arial.ttf", max(22, w // 42))
    except OSError:
        font = ImageFont.load_default()

    regions = [
        ("cat ears/headband", (0.28, 0.01, 0.61, 0.28), (67, 113, 181, 78)),
        ("front hair L/R", (0.24, 0.13, 0.69, 0.88), (98, 172, 89, 58)),
        ("face base", (0.31, 0.19, 0.67, 0.48), (255, 212, 75, 58)),
        ("eyes/brows", (0.33, 0.26, 0.64, 0.39), (141, 88, 170, 70)),
        ("mouth/teeth", (0.40, 0.39, 0.61, 0.54), (227, 91, 91, 75)),
        ("left paw glove", (0.00, 0.31, 0.31, 0.66), (43, 153, 188, 78)),
        ("right paw glove", (0.62, 0.29, 0.96, 0.66), (43, 153, 188, 78)),
        ("arms", (0.02, 0.55, 0.96, 0.85), (241, 143, 72, 52)),
        ("choker/bell", (0.44, 0.55, 0.56, 0.65), (255, 229, 61, 90)),
        ("dress/body", (0.32, 0.61, 0.72, 1.00), (54, 72, 92, 72)),
    ]

    for label, box, color in regions:
        x1, y1, x2, y2 = [int(v) for v in (box[0] * w, box[1] * h, box[2] * w, box[3] * h)]
        draw.rectangle((x1, y1, x2, y2), fill=color, outline=(0, 0, 0, 190), width=3)
        text_pos = (x1 + 8, y1 + 6)
        draw.rectangle(
            (text_pos[0] - 4, text_pos[1] - 3, text_pos[0] + len(label) * 13 + 8, text_pos[1] + 30),
            fill=(255, 255, 255, 185),
        )
        draw.text(text_pos, label, fill=(0, 0, 0, 255), font=font)

    img.save(OUT_DIR / "takagi_cat_pose_layer_regions.png", quality=95)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    make_cutout()
    make_region_guide()


if __name__ == "__main__":
    main()
