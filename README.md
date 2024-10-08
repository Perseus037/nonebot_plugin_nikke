<div align="center">
  <img src="https://github.com/Perseus037/data/blob/master/nikke.webp" alt="nonebot_plugin_nikke图标" >

# nonebot-plugin-nikke

_✨ 基于 NoneBot2 的胜利女神：妮姬 Wiki 插件✨ _

<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">
<a href="https://pdm.fming.dev">
  <img src="https://img.shields.io/badge/pdm-managed-blueviolet" alt="pdm-managed">
</a>
<!-- <a href="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/f4778875-45a4-4688-8e1b-b8c844440abb">
  <img src="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/f4778875-45a4-4688-8e1b-b8c844440abb.svg" alt="wakatime">
</a> -->

<br />

<a href="./LICENSE">
  <img src="https://img.shields.io/github/license/lgc-NB2Dev/nonebot-plugin-uma.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-nikke">
  <img src="https://img.shields.io/pypi/v/nonebot-plugin-nikke.svg" alt="pypi">
</a>
<a href="https://pypi.org/project/nonebot-plugin-nikke/">
  <img src="https://img.shields.io/pypi/dm/nonebot-plugin-nikke.svg" alt="pypi download">
</a>

</div>

<div align="left">

## 📖 介绍

一个胜利女神：妮姬的 Wiki 插件，主要数据来源为 GameKee 

一时兴起给群友写着玩的，我自己不玩nikke。加上太忙，故鸽。

有愿意接手继续完善的，欢迎发email，或者发个pull request我直接把你拉进来。

没有找到合适api爬立绘live2D，也没有找到合适的图床，暂时先用github凑活吧。

## 💿 安装

</details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-nikke[all]

</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-nikke[all]

</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-nikke[all]

</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-nikke[all]

</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_nikke"]

</details>

## ⚙️ 配置

无需配置，开箱即用。

## 🎉 使用

现有指令列表：

nk角评，nikke角评：输出一张包含对应角色数据，技能等信息的图片，支持精确匹配和模糊匹配。

nk评分, nk角色评分：输出一张全角色评分图，默认输出爆裂阶段3的评分图,支持选择，输入nk评分 1，bot则会回复爆烈阶段3的评分图。

目前在排队施工中的功能：nk抽卡，nk立绘

example：<img src="https://github.com/Perseus037/data/blob/master/nikke%20example.png" alt="示例" >

## 📞 制作者

### 黑纸折扇 [Perseus037] (https://github.com/Perseus037)

QQ：1209228678

## 🙏 感谢

在此感谢以下开发者(项目)对本项目做出的贡献：

-  [student_2333](https://github.com/lgc2333) 的无私帮助
-  [nonebot_plugin_bawiki](https://github.com/lgc-NB2Dev/nonebot-plugin-bawiki) 提供的结构和代码参考

插件数据源提供：

-  [GameKee](https://nikke.gamekee.com/) 
-  [Nikke-db](https://github.com/Nikke-db/Nikke-db.github.io) 

## 📝 更新日志

### 0.1.0.post2-post4
- 实现角色图片模糊搜索
- 增加新功能，nk角色评分
- 修复精确匹配重复触发函数的bug

### 0.1.0.post1

- 从gamekee爬了n张图，敲爬虫敲的我手都麻了
- 重构代码，对原有代码进行模块化拆分便于维护


