# Live2D-Takagi

高木同学（Takagi）个人 Live2D 模型项目。

基于一张高木同学猫爪姿势的同人插画，制作可用于 **Live2D Cubism Editor** 和 **VTube Studio** 的半身 Live2D 模型。项目包含完整的素材分层规范、Cubism 参数定义、动作模板以及自动化工具脚本。

---

## 📁 项目结构

```
Live2D-Takagi/
├── 00_source/                  # 原始素材
│   ├── 1648138415955_original.jpg    # 原始插画（第三方同人作品）
│   └── 1648138415955_cutout_user.png # 手动抠图透明 PNG
│
├── 02_specs/                   # 制作规范文档（本项目编写）
│   ├── cubism_parameters.json        # Cubism 参数定义（含物理分组）
│   ├── cubism_workflow.md            # 完整制作流程指南
│   └── live2d_layer_manifest.md      # 图层拆分清单与补画说明
│
├── 03_krita_starter_safe/      # Krita 起步文件（自动生成）
│   ├── takagi_live2d_model.kra       # Krita 工程文件
│   ├── takagi_live2d_model.psd       # PSD 格式
│   ├── takagi_live2d_safe_layer_starter.ora  # OpenRaster 格式
│   ├── merged_preview.png            # 合成预览
│   └── layers/                       # 各图层 PNG 文件
│
├── 04_motion_templates/        # 动作模板（本项目编写）
│   ├── blink_loop.motion3.json       # 眨眼循环
│   ├── idle_breath.motion3.json      # 待机呼吸
│   ├── mouth_test.motion3.json       # 嘴巴开合测试
│   ├── paw_wave.motion3.json         # 猫爪摆动
│   ├── playful_head_tilt.motion3.json # 俏皮歪头
│   └── README.md                     # 动作模板使用说明
│
├── tools/                      # 自动化工具（本项目编写）
│   ├── build_krita_layer_starter.py  # 从原图自动生成分层 ORA/PSD 文件
│   └── prepare_reference_assets.py   # 准备参考素材
│
└── takagi_live2d_model.cmo3    # Live2D Cubism 模型工程文件
```

---

## 🎯 模型参数

模型定义了以下 Cubism 参数，详见 [`02_specs/cubism_parameters.json`](02_specs/cubism_parameters.json)：

| 参数 | 说明 | 范围 |
| --- | --- | --- |
| `ParamAngleX/Y/Z` | 头部转动（左右/上下/歪头） | -20~20 / -12~12 / -10~10 |
| `ParamEyeLOpen` / `ParamEyeROpen` | 左右眼眨眼 | 0~1 |
| `ParamEyeBallX/Y` | 眼球跟随 | -1~1 |
| `ParamMouthOpenY` | 嘴巴开合 | 0~1 |
| `ParamMouthForm` | 嘴型变化 | -1~1 |
| `ParamBodyAngleX` | 身体左右轻摆 | -8~8 |
| `ParamBreath` | 呼吸循环 | 0~1 |
| `ParamHairSwing` | 长发物理摆动 | -1~1 |
| `ParamPawWave` | 猫爪轻微摆动 | -1~1 |
| `ParamBellSwing` | 铃铛摆动 | -1~1 |

---

## 🛠️ 工具使用

### 生成 Krita 分层起步文件

从原始插画自动提取图层，生成 ORA / PSD / KRA 格式的分层文件：

```bash
cd tools
pip install Pillow
python build_krita_layer_starter.py
```

输出文件位于 `03_krita_starter_safe/` 目录。

---

## 📋 制作流程概要

1. **PSD 准备** — 按 [`live2d_layer_manifest.md`](02_specs/live2d_layer_manifest.md) 拆层，补画被遮挡区域
2. **Cubism 导入** — 导入 PSD，建立部件树，生成网格
3. **参数绑定** — 按 [`cubism_workflow.md`](02_specs/cubism_workflow.md) 中的推荐顺序绑定参数
4. **物理设置** — 配置头发、铃铛、猫爪的物理效果
5. **动作模板** — 将 `04_motion_templates/` 中的 `.motion3.json` 放入模型的 `motions` 目录
6. **导出测试** — 导出 `moc3`，在 VTube Studio 中测试

---

## ⚠️ 制作注意事项

- 原图手套挡住较多手臂，拆层时手臂后方需要补画，否则猫爪摆动会露空
- 张嘴表情很大，闭嘴口型不能只压缩原嘴，需要单独画微笑嘴线
- 刘海遮脸面积较大，头部左右转动幅度建议保守
- 猫耳头箍可与头部绑定，也可单独加跟随延迟增加生动感
- 铃铛适合做小物理，但摆动幅度不要超出项圈范围

---

## 📄 许可与第三方素材声明

### 本项目原创内容

以下内容为本项目原创，仅供个人学习与非商业用途：

- `02_specs/` — 制作规范文档（参数定义、制作流程、图层清单）
- `03_krita_starter_safe/` — 自动生成的 Krita 分层起步文件
- `04_motion_templates/` — 动作模板文件
- `tools/` — 自动化工具脚本
- `takagi_live2d_model.cmo3` — Live2D Cubism 模型工程文件

### 第三方素材（非本项目原创）

| 来源 | 路径 | 作者 | 许可 |
| --- | --- | --- | --- |
| 高木同学同人插画 | `00_source/1648138415955_original.jpg` | 原画师（Pixiv 来源，具体作者待确认） | 仅供个人学习，版权归原作者所有 |
| Live2D 官方示例模型（とろろ & ひじき） | 本地使用，未包含在仓库中 | Live2D Inc.（插画 & 建模） | 按 [Live2D 无償提供マテリアル使用許諾契約書](https://www.live2d.com/eula/live2d-free-material-license-agreement_jp.html) 规定使用 |

> **注意**：とろろ & ひじき模型文件是 Live2D Inc. 官方提供的示例数据，因许可协议禁止原始素材的再配布（§4.1.1），该文件未包含在本仓库中。如需使用请自行前往 [Live2D 官方下载页面](https://www.live2d.com/learn/sample/) 获取。