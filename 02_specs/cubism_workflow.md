# Cubism 制作流程

这份流程按“尽量不改原图，只做 Live2D 需要的微调”来写。

## 1. PSD 准备

1. 在 Photoshop、Clip Studio Paint 或 Krita 中打开原图。
2. 按 `live2d_layer_manifest.md` 的清单拆层。
3. 所有会动的部位都要有自己的完整底图；被遮住的部分需要补画。
4. 背景不要放进模型 PSD，背景只作为参考图。
5. 导出 PSD 前检查图层名，尽量不要用重复名称。

## 2. Cubism 导入

1. 新建 Cubism 模型，导入 PSD。
2. 先给整体建立部件树：`Head`、`Hair`、`Face`、`Mouth`、`Body`、`Arms`、`Hands`、`Accessory`。
3. 给每个可动图层自动生成网格，脸、头发、嘴、手套建议手动调整网格密度。
4. 先绑定大参数：`ParamAngleX`、`ParamAngleY`、`ParamAngleZ`。
5. 再绑定表情参数：眼睛、嘴巴、眉毛。
6. 最后处理物理：头发、铃铛、猫爪手套。

## 3. 建议绑定顺序

1. `head_base`：先做头部 X/Y/Z，确认脸不会破。
2. `eyes`：做眨眼和眼球跟随。
3. `mouth`：做开合和嘴型。
4. `hair_front` / `hair_side`：跟随头部，再加物理。
5. `body`：做身体左右和呼吸。
6. `paw_gloves`：做猫爪轻微上下摆动。
7. `bell`：做项圈跟随和铃铛摆动。

## 4. 最小动作配置

- 待机：`ParamBreath` 循环，周期 3 到 4 秒。
- 眨眼：左右眼同时眨，间隔 3 到 6 秒随机。
- 猫爪摆动：`ParamPawWave` 小幅循环，不要超过 6 度旋转。
- 铃铛摆动：跟随头部和身体，幅度保持小。

## 5. VTube Studio 导出

1. Cubism 中导出 `moc3`。
2. 同时导出 `model3.json`、`textures`、`physics3.json`、`motions`。
3. 把整个模型文件夹放入 VTube Studio 的 `Live2DModels` 目录。
4. 进入 VTube Studio 后先测试眨眼、嘴巴、头部转动，再调物理。

## 6. 这张图的注意点

- 原图手套挡住很多手臂，拆层时手臂后方需要补画，否则猫爪轻动会露空。
- 张嘴表情很大，闭嘴口型不能只压缩原嘴，需要单独画一条微笑嘴线。
- 刘海遮脸面积较大，头部左右转动幅度建议保守。
- 猫耳头箍可以和头部绑定，也可以单独加一点跟随延迟，效果会更活。
- 铃铛很适合做小物理，但不要让它摆到离开项圈。
