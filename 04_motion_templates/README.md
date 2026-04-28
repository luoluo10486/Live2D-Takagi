# 动作模板说明

这些文件是给当前个人 Live2D 模型用的动作模板。它们要等你在
Live2D Cubism Editor 里完成网格、参数绑定、模型导出之后再使用。

## 重要说明

这些 `.motion3.json` 不能代替“绑模型”。你仍然需要先在 Cubism Editor
里完成这些工作：

- 给图层生成网格
- 创建参数
- 把图层绑定到参数
- 导出模型

## 需要的参数

- `ParamAngleZ`：歪头
- `ParamEyeLOpen`：左眼睁闭
- `ParamEyeROpen`：右眼睁闭
- `ParamMouthOpenY`：嘴巴开合
- `ParamMouthForm`：嘴型变化
- `ParamBreath`：呼吸
- `ParamBodyAngleX`：身体左右轻摆
- `ParamHairSwing`：头发摆动
- `ParamPawWave`：猫爪轻摆
- `ParamBellSwing`：铃铛摆动

## 推荐顺序

1. 在 Live2D Cubism Editor 里导入 PSD。
2. 给所有图层生成网格。
3. 创建上面列出的参数。
4. 先绑定简单动作：`ParamAngleZ`、`ParamBreath`、眼睛、嘴巴。
5. 导出模型。
6. 把这些 `.motion3.json` 放进导出模型文件夹的 `motions` 目录。
7. 在 Cubism Viewer 或 VTube Studio 里测试。

## 文件说明

- `idle_breath.motion3.json`：待机呼吸和轻微身体摆动。
- `playful_head_tilt.motion3.json`：俏皮歪头动作。
- `blink_loop.motion3.json`：眨眼循环。
- `paw_wave.motion3.json`：猫爪轻微摆动。
- `mouth_test.motion3.json`：嘴巴开合测试。
