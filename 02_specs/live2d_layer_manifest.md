# Live2D 拆层清单

用途：基于 `00_source/1648138415955_original.jpg` 做个人使用的 Live2D 半身模型。目标是尽量保留原图，只做 Live2D 所需的最小补画和分层。

## 画布建议

- 尺寸：保持原图比例，建议先用 `2048px` 高度重绘/分层。
- 姿态：保留当前正面猫爪姿势，不改角色比例。
- 格式：最终导出为 PSD，图层名使用英文或拼音，方便 Cubism 识别。
- 背景：不要放进 PSD 模型层；背景单独保存。

## 必拆图层

| 组 | 图层名 | 说明 |
| --- | --- | --- |
| Head | `head_base` | 脸和头部底色，需要补出被头发、嘴巴、耳朵遮住的边缘 |
| Head | `neck` | 脖子和锁骨区域，和头部分开 |
| Hair | `hair_back` | 身后长发，放在身体后方 |
| Hair | `hair_side_L` / `hair_side_R` | 两侧长发，和脸分开，方便左右晃动 |
| Hair | `hair_front_L` / `hair_front_R` | 额前大块头发，遮脸的地方需要补画脸底 |
| Face | `eye_white_L` / `eye_white_R` | 眼白，独立于脸 |
| Face | `iris_L` / `iris_R` | 虹膜和瞳孔，建议每只眼分组 |
| Face | `eye_highlight_L` / `eye_highlight_R` | 高光单独层 |
| Face | `upper_lid_L` / `upper_lid_R` | 上眼皮/闭眼线 |
| Face | `lower_lid_L` / `lower_lid_R` | 下眼线 |
| Face | `brow_L` / `brow_R` | 眉毛 |
| Face | `nose` | 鼻子小阴影 |
| Mouth | `mouth_back` | 口腔深色底 |
| Mouth | `tongue` | 舌头/口腔亮部 |
| Mouth | `upper_teeth_L` / `upper_teeth_R` | 两颗牙齿分开，开合时更自然 |
| Mouth | `mouth_line` | 嘴部线条 |
| Accessory | `cat_ear_L` / `cat_ear_R` | 猫耳头箍左右分开 |
| Accessory | `ear_inner_L` / `ear_inner_R` | 猫耳内侧粉色层 |
| Accessory | `choker` | 项圈 |
| Accessory | `bell_base` | 铃铛主体 |
| Accessory | `bell_shadow` | 铃铛阴影和开口 |
| Body | `torso_skin` | 肩膀、手臂以外的皮肤 |
| Body | `dress_base` | 裙装主体 |
| Body | `dress_shadow` | 裙装阴影，建议单独做轻微呼吸变形 |
| Arms | `arm_L_upper` / `arm_R_upper` | 上臂 |
| Arms | `arm_L_fore` / `arm_R_fore` | 前臂 |
| Hands | `paw_L_base` / `paw_R_base` | 猫爪手套主体 |
| Hands | `paw_L_pads` / `paw_R_pads` | 肉垫 |
| Hands | `paw_L_claws` / `paw_R_claws` | 白色爪尖 |

## 需要补画的位置

- 脸部：补出被刘海遮住的额头和脸颊边缘。
- 嘴部：至少补一个闭嘴口型、微笑口型和当前张嘴口型。
- 眼睛：补闭眼线，眼白后方不要漏脸色。
- 左右手套：手套后面的手臂线条要补完整，方便猫爪轻微摆动。
- 头发：身后长发被身体挡住的位置可以粗补，不需要精细到原图级别。
- 服装：裙装被铃铛和头发遮住的边缘补完整。

## 最小表情集

- `exp_default`：原图张嘴笑。
- `exp_smile_closed`：闭嘴微笑。
- `exp_blink`：眨眼。
- `exp_surprise`：眼睛略大、嘴型保持张开。
- `exp_paw_pose`：猫爪保持原姿势，可加轻微上下摆动。
