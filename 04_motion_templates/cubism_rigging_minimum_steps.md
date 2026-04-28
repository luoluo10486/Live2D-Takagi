# Cubism 新手版完整操作步骤

这份文档对应当前的保底版工程：

`takagi_live2d_safe_layer_starter.ora`

这个版本的目标不是马上做精细眨眼和嘴巴，而是先做一个能在 Live2D 里动起来的第一版模型。

当前路线是：

`完整人物层 -> 自动网格 -> 整体呼吸 -> 整体歪头 -> 保存工程 -> 导出模型`

## 1. 先确认你导入的是正确 PSD

在 Krita 里应该用这个文件另存出 PSD：

`C:\Users\HP\Documents\New project\takagi_live2d_personal\03_krita_starter_safe\takagi_live2d_safe_layer_starter.ora`

建议保存为：

`C:\Users\HP\Documents\New project\takagi_live2d_personal\takagi_live2d_model.psd`

然后在 Live2D Cubism Editor 里导入这个 PSD。

如果你导入后左下角图层列表里能看到下面这些图层，就说明导入对了：

- `whole_character_base_DO_NOT_DELETE`
- `optional_hair_back`
- `optional_torso_skin`
- `optional_dress_base`
- `optional_arm_L`
- `optional_arm_R`

## 2. 只保留第一个完整人物层

左下角图层列表里，第一个图层应该叫：

`whole_character_base_DO_NOT_DELETE`

这个是完整人物本体，必须保留显示。

下面所有 `optional_` 开头的图层现在都先不用，比如：

- `optional_hair_back`
- `optional_torso_skin`
- `optional_dress_base`
- `optional_arm_L`
- `optional_eye_L`
- `optional_eye_R`

请把所有 `optional_` 图层左边的小眼睛都关掉。

最后画面应该只剩一个完整人物，没有重影，也没有半透明叠加。

## 3. 只选中完整人物层

不要全选所有图层。

现在只点击选中：

`whole_character_base_DO_NOT_DELETE`

选中后，画面上应该只有一个红色外框，框住整个人物。

如果你看到很多小框、很多重叠框，说明你选多了。请取消选择后重新只点第一个完整人物层。

## 4. 给完整人物层自动生成网格

选中 `whole_character_base_DO_NOT_DELETE` 后：

1. 点击上方菜单 `建模`。
2. 找到 `网格的自动生成`。
3. 使用默认设置。
4. 点击确定。

生成后，人物上会出现很多网格线或控制点，这是正常的。

第一版不用追求网格完美，只要能动就行。

## 5. 保存 Cubism 工程

在正式做动作前先保存一次：

1. 点击 `文件`。
2. 点击 `保存` 或 `另存为`。
3. 保存为：

`C:\Users\HP\Documents\New project\takagi_live2d_personal\takagi_live2d_model.cmo3`

以后这个 `.cmo3` 就是 Live2D Cubism 的工程文件。

## 6. 做第一个动作：整体呼吸

因为现在只有一个完整人物层，所以呼吸就是让整个人物非常轻微地上下变化。

### 选择图层

只选中：

`whole_character_base_DO_NOT_DELETE`

### 找到参数

在参数面板里找到：

`呼吸`

如果你看到英文，它的 ID 通常是：

`ParamBreath`

### 设置呼吸关键点

1. 把 `呼吸` 参数拖到最左边，数值是 `0`。
2. 确认人物保持原样。
3. 把 `呼吸` 参数拖到最右边，数值是 `1`。
4. 使用移动工具，把整个人物向上移动一点点。
5. 移动幅度很小就够，大概 `5` 到 `10` 像素。
6. 来回拖动 `呼吸` 参数，检查人物是否轻微上下起伏。

如果移动太明显，就撤销一点。呼吸动作越小越自然。

## 7. 做第二个动作：整体歪头

这个版本不能做真正的头部分离歪头，因为我们只有完整人物层。这里做的是“整个人物轻微倾斜”，先用来跑通流程。

### 选择图层

只选中：

`whole_character_base_DO_NOT_DELETE`

### 找到参数

在参数面板里找到：

`角度 Z`

英文 ID 通常是：

`ParamAngleZ`

### 设置歪头关键点

1. 把 `角度 Z` 参数拖到中间，数值是 `0`。
2. 确认人物保持原样。
3. 把 `角度 Z` 参数拖到最左边。
4. 使用旋转工具，让整个人物向左轻微倾斜。
5. 倾斜角度不要太大，大概 `3` 到 `5` 度就够。
6. 把 `角度 Z` 参数拖到最右边。
7. 使用旋转工具，让整个人物向右轻微倾斜。
8. 来回拖动 `角度 Z` 参数，检查是否能左右摇摆。

注意：这里先不要做 `角度 X` 和 `角度 Y`。那是左右转头和上下点头，需要更完整的拆层，新手版先跳过。

## 8. 做第三个动作：整体左右轻摆

这个动作可以让模型不那么僵。

### 找到参数

在参数面板里找：

`身体 X`

如果没有看到，可以先跳过。不同版本默认参数名字可能不一样。

英文 ID 常见是：

`ParamBodyAngleX`

### 操作

1. 只选中 `whole_character_base_DO_NOT_DELETE`。
2. 把 `身体 X` 参数拖到最左边。
3. 把整个人物向左移动一点点。
4. 把 `身体 X` 参数拖到最右边。
5. 把整个人物向右移动一点点。
6. 来回拖动参数测试。

移动幅度控制在 `5` 到 `15` 像素，不要太大。

## 9. 暂时不要做这些

当前这个保底版只有完整人物层，所以这些动作先不要做：

- 精细眨眼
- 嘴巴开合
- 猫爪单独摆动
- 头发单独摆动
- 铃铛单独摆动

这些需要真正分层后才自然。现在强行做也可以，但效果容易很怪。

第一阶段目标是先完成：

- 呼吸
- 整体歪头
- 整体左右轻摆
- 成功导出模型
- 放进 VTube Studio 测试

## 10. 导出模型

动作能正常拖动后，就可以导出。

1. 点击上方菜单 `文件`。
2. 找到 `导出嵌入用文件`。
3. 选择 `moc3 文件导出` 或类似选项。
4. 导出目录建议用：

`C:\Users\HP\Documents\New project\takagi_live2d_personal\05_export\takagi_live2d_model`

导出后，文件夹里通常会有：

- `.moc3`
- `.model3.json`
- `textures`

如果你做了物理，还会有：

- `.physics3.json`

## 11. 放进 VTube Studio

1. 打开 VTube Studio。
2. 找到它的 `Live2DModels` 文件夹。
3. 把导出的整个模型文件夹放进去。
4. 在 VTube Studio 里加载模型。
5. 测试模型是否能显示、是否能轻微动起来。

## 12. 当前最推荐你做的下一步

你现在先完成这三步：

1. 只显示 `whole_character_base_DO_NOT_DELETE`。
2. 给它自动生成网格。
3. 保存为 `takagi_live2d_model.cmo3`。

完成后再继续做 `呼吸` 和 `角度 Z`。

---

# 分层版：头部跟随鼠标操作步骤

如果你的目标是放到网站首页，并且希望“头跟着鼠标动，身体基本不动”，就不能只用完整人物层。

你需要改用分层路线。

## 1. 分层版和整图版的区别

整图版：

- 只用 `whole_character_base_DO_NOT_DELETE`
- 优点是最简单
- 缺点是只能整个人一起动

分层版：

- 隐藏 `whole_character_base_DO_NOT_DELETE`
- 打开需要的 `optional_` 图层
- 优点是头、身体、眼睛、嘴巴可以分开动
- 缺点是边缘可能会有一点粗糙

你现在说“我要分开”，就按下面的分层版做。

## 2. 显示和隐藏哪些图层

先隐藏：

- `whole_character_base_DO_NOT_DELETE`

打开这些图层的小眼睛：

- `optional_hair_back`
- `optional_torso_skin`
- `optional_dress_base`
- `optional_arm_L`
- `optional_arm_R`
- `optional_cat_ear_headband`
- `optional_head_base`
- `optional_hair_front_L`
- `optional_hair_front_R`
- `optional_eye_L`
- `optional_eye_R`
- `optional_mouth_open_teeth`
- `optional_choker_bell`
- `optional_paw_L_base`
- `optional_paw_L_pads_claws`
- `optional_paw_R_base`
- `optional_paw_R_pads_claws`

如果打开后有些地方透明或缺块，这是自动粗拆层的限制。第一版可以先接受，重点是做出头部跟随鼠标。

## 3. 自动生成网格

这次要给每个 `optional_` 图层生成网格。

操作：

1. 隐藏 `whole_character_base_DO_NOT_DELETE`。
2. 打开所有需要的 `optional_` 图层。
3. 在左下角图层列表里依次点击每个 `optional_` 图层。
4. 对每个图层点上方的 `AUTO` 自动生成网格。

如果可以多选，就多选后一起点 `AUTO`。如果不确定，就一个一个来，最稳。

## 4. 创建头部变形器

头部跟随鼠标主要靠这个变形器。

先选中这些头部相关图层：

- `optional_cat_ear_headband`
- `optional_head_base`
- `optional_hair_front_L`
- `optional_hair_front_R`
- `optional_eye_L`
- `optional_eye_R`
- `optional_mouth_open_teeth`

然后创建弯曲变形器：

1. 点击 `建模`。
2. 点击 `变形器`。
3. 点击 `创建弯曲变形器`。
4. 名称填写：

`head_follow_deformer`

5. 选择 `设为所选对象的父级`。
6. 点击 `创建`。

以后做头部左右、上下、歪头，都优先选这个 `head_follow_deformer`。

## 5. 创建身体变形器

身体单独轻微动，不要跟头完全一样。

选中身体相关图层：

- `optional_hair_back`
- `optional_torso_skin`
- `optional_dress_base`
- `optional_arm_L`
- `optional_arm_R`
- `optional_choker_bell`
- `optional_paw_L_base`
- `optional_paw_L_pads_claws`
- `optional_paw_R_base`
- `optional_paw_R_pads_claws`

创建弯曲变形器：

`body_idle_deformer`

同样选择：

`设为所选对象的父级`

## 6. 绑定鼠标左右：`ParamAngleX`

网站上鼠标左右移动，会驱动 `ParamAngleX`。

操作：

1. 选中 `head_follow_deformer`。
2. 找到参数 `角度 X`。
3. 把 `角度 X` 拖到最左边。
4. 把头部整体向左移动一点点，或轻微压缩右侧、拉伸左侧。
5. 把 `角度 X` 拖到最右边。
6. 把头部整体向右移动一点点，或轻微压缩左侧、拉伸右侧。
7. 来回拖动 `角度 X`，看头是否左右跟随。

新手建议只做轻微平移，不要大幅变形。

## 7. 绑定鼠标上下：`ParamAngleY`

网站上鼠标上下移动，会驱动 `ParamAngleY`。

操作：

1. 选中 `head_follow_deformer`。
2. 找到参数 `角度 Y`。
3. 把 `角度 Y` 拖到最左边或下端。
4. 把头部稍微向下移动一点。
5. 把 `角度 Y` 拖到最右边或上端。
6. 把头部稍微向上移动一点。
7. 来回拖动 `角度 Y` 测试。

第一版只做上下移动就够，不要追求真正 3D 抬头低头。

## 8. 绑定歪头：`ParamAngleZ`

这个参数会让鼠标跟随更自然。

操作：

1. 选中 `head_follow_deformer`。
2. 找到 `角度 Z`。
3. 参数拖到最左边。
4. 让头部轻微左旋 `3` 到 `5` 度。
5. 参数拖到最右边。
6. 让头部轻微右旋 `3` 到 `5` 度。
7. 来回拖动 `角度 Z` 测试。

## 9. 绑定眼睛跟随：`ParamEyeBallX` 和 `ParamEyeBallY`

如果参数面板里有眼球参数，可以做。

### 眼球左右

选中：

- `optional_eye_L`
- `optional_eye_R`

找到：

`眼球 X`

操作：

- 参数左边：两只眼睛里的瞳孔区域稍微向左。
- 参数右边：两只眼睛里的瞳孔区域稍微向右。

注意：当前 `optional_eye_L` 和 `optional_eye_R` 是整只眼一层，不是瞳孔单独层。所以第一版可以先跳过眼球跟随。

## 10. 绑定身体呼吸：`ParamBreath`

选中：

`body_idle_deformer`

找到：

`呼吸`

操作：

1. 参数 `0`：身体原样。
2. 参数 `1`：身体整体上移 `5` 到 `10` 像素。
3. 来回拖动测试。

## 11. 网站鼠标跟随时会用哪些参数

后面接入 Vue 首页时，网页代码会实时设置这些参数：

- 鼠标左右位置 -> `ParamAngleX`
- 鼠标上下位置 -> `ParamAngleY`
- 鼠标左右位置 -> `ParamAngleZ` 少量倾斜
- 自动循环 -> `ParamBreath`

所以你现在最重要的是先把这四个参数做好：

- `ParamAngleX`
- `ParamAngleY`
- `ParamAngleZ`
- `ParamBreath`

## 12. 分层版当前的现实限制

这套 `optional_` 图层是自动粗拆出来的，不是专业画师手工拆层。

所以可能会有：

- 边缘不干净
- 部分区域透明
- 图层叠加时有缺块
- 大幅转头时穿帮

第一版请把动作幅度控制小一点：

- `ParamAngleX`：小幅左右
- `ParamAngleY`：小幅上下
- `ParamAngleZ`：最多 `3` 到 `5` 度
- `ParamBreath`：最多上移 `5` 到 `10` 像素

这样放到网站首页右下角，效果会比较稳。
