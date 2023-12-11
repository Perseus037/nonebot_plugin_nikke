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

## 💬 前言

你说的对，但是《NIKKE》是由金亨泰联合腾讯研发的一款全新挂机收菜游戏。游戏发生在一个被称作「意外失败」的系统错误，
在这里，用户资讯初始化失败被授予「系统错误将重启游戏」，导引数据更新失败，(4/10)Add catalogue path。
你将扮演一位名为「数据更新失败」的神秘角色，在自由的旅行中邂逅无法获取好友资讯，和他们一起，无法获取商品资讯，购买异常——同时，逐步发掘「ERROR」的真相。

## 📖 介绍

一个胜利女神：妮姬的 Wiki 插件，主要数据来源为 GameKee 

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

nk角评，nikke角评：输出一张包含对应角色数据，技能等信息的图片

example：<img src="https://github.com/Perseus037/data/blob/master/nikke%20example.png" alt="示例" >

## 📞 制作者

### 黑纸折扇 [Perseus037] (https://github.com/Perseus037)

QQ：1209228678

## 🙏 感谢

在此感谢以下开发者(项目)对本项目做出的贡献：

-  [student_2333](https://github.com/lgc2333) 对于我学习编写插件和配置qqbot等过程中的无私帮助

## 📝 更新日志

### 0.1.0.post1

- 从gamekee爬了n张图
- 重构代码，对原有代码进行模块化拆分便于维护


