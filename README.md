<p align="center">
  <img alt="LOGO" src="./logo.png" width="256" height="256" />
</p>

<div align="center">

# MNMA - 新月同行小助手</br>MaaNewMoonAccompanying</br>✨ 组长们的超级秋千人 ✨

基于全新架构的 [**新月同行**](https://xytx.firewick.net/home) 小助手<br/>图像技术 + 模拟控制，解放双手，由 [MaaFramework](https://github.com/MaaXYZ/MaaFramework) 与 [MFAAvalonia](https://github.com/SweetSmellFox/MFAAvalonia) 强力驱动！

<p align="center">
  <a href="https://www.python.org/" target="_blank"><img alt="python" src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white"></a>
  <a href="https://github.com/MaaXYZ/MaaFramework/blob/main/docs/zh_cn/3.1-%E4%BB%BB%E5%8A%A1%E6%B5%81%E6%B0%B4%E7%BA%BF%E5%8D%8F%E8%AE%AE.md" target="_blank"><img alt="pipeline" src="https://img.shields.io/badge/Pipeline-%23876f69?logo=paddypower&logoColor=%23FFFFFF"></a>
  <a href="https://github.com/kqcoxn/MaaNewMoonAccompanying/releases" target="_blank"><img alt="platform" src="https://img.shields.io/badge/platform-Windows-blueviolet"></a>
  <br/>
  <a href="https://github.com/kqcoxn/MaaNewMoonAccompanying/commits/main/" target="_blank"><img alt="committs" src="https://img.shields.io/github/commit-activity/m/kqcoxn/MaaNewMoonAccompanying?color=%23ff69b4"></a>
  <a href="https://github.com/kqcoxn/MaaNewMoonAccompanying/stargazers" target="_blank"><img alt="stars" src="https://img.shields.io/github/stars/kqcoxn/MaaNewMoonAccompanying?style=social"></a>
  <a href="https://github.com/kqcoxn/MaaNewMoonAccompanying/releases" target="_blank"><img alt="stars" src="https://img.shields.io/github/downloads/kqcoxn/MaaNewMoonAccompanying/total?style=social"></a>
  <br/>
  <a href="https://mirrorchyan.com/zh/projects&source=mnma-github-code" target="_blank"><img alt="mirrorc" src="https://img.shields.io/badge/Mirror%E9%85%B1-%239af3f6?logo=countingworkspro&logoColor=4f46e5"></a>
  <a href="http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=VMC132QhbMDLi5U62MlDRvtCMj9WOXRr&authKey=yJNKO4sQ%2BBFHpBCLSSEvVOAyz%2FPjknNSl70W3ugg2%2BpELnKmEiHamj1emJMWcLwQ&noverify=0&group_code=993245868" target="_blank"><img alt="QQ交流群" src="https://img.shields.io/badge/QGroup-993245868-0e80c1?logo=qq&logoColor=white"></a>
  <a href="https://zread.ai/kqcoxn/MaaNewMoonAccompanying" target="_blank"><img alt="AI文档与问答" src="https://img.shields.io/badge/Ask_Zread-_.svg?style=flat&color=00b0aa&labelColor=000000&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTQuOTYxNTYgMS42MDAxSDIuMjQxNTZDMS44ODgxIDEuNjAwMSAxLjYwMTU2IDEuODg2NjQgMS42MDE1NiAyLjI0MDFWNC45NjAxQzEuNjAxNTYgNS4zMTM1NiAxLjg4ODEgNS42MDAxIDIuMjQxNTYgNS42MDAxSDQuOTYxNTZDNS4zMTUwMiA1LjYwMDEgNS42MDE1NiA1LjMxMzU2IDUuNjAxNTYgNC45NjAxVjIuMjQwMUM1LjYwMTU2IDEuODg2NjQgNS4zMTUwMiAxLjYwMDEgNC45NjE1NiAxLjYwMDFaIiBmaWxsPSIjZmZmIi8%2BCjxwYXRoIGQ9Ik00Ljk2MTU2IDEwLjM5OTlIMi4yNDE1NkMxLjg4ODEgMTAuMzk5OSAxLjYwMTU2IDEwLjY4NjQgMS42MDE1NiAxMS4wMzk5VjEzLjc1OTlDMS42MDE1NiAxNC4xMTM0IDEuODg4MSAxNC4zOTk5IDIuMjQxNTYgMTQuMzk5OUg0Ljk2MTU2QzUuMzE1MDIgMTQuMzk5OSA1LjYwMTU2IDE0LjExMzQgNS42MDE1NiAxMy43NTk5VjExLjAzOTlDNS42MDE1NiAxMC42ODY0IDUuMzE1MDIgMTAuMzk5OSA0Ljk2MTU2IDEwLjM5OTlaIiBmaWxsPSIjZmZmIi8%2BCjxwYXRoIGQ9Ik0xMy43NTg0IDEuNjAwMUgxMS4wMzg0QzEwLjY4NSAxLjYwMDEgMTAuMzk4NCAxLjg4NjY0IDEwLjM5ODQgMi4yNDAxVjQuOTYwMUMxMC4zOTg0IDUuMzEzNTYgMTAuNjg1IDUuNjAwMSAxMS4wMzg0IDUuNjAwMUgxMy43NTg0QzE0LjExMTkgNS42MDAxIDE0LjM5ODQgNS4zMTM1NiAxNC4zOTg0IDQuOTYwMVYyLjI0MDFDMTQuMzk4NCAxLjg4NjY0IDE0LjExMTkgMS42MDAxIDEzLjc1ODQgMS42MDAxWiIgZmlsbD0iI2ZmZiIvPgo8cGF0aCBkPSJNNCAxMkwxMiA0TDQgMTJaIiBmaWxsPSIjZmZmIi8%2BCjxwYXRoIGQ9Ik00IDEyTDEyIDQiIHN0cm9rZT0iI2ZmZiIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgo8L3N2Zz4K&logoColor=ffffff"></a>
</p>

</div>

## 功能列表

### 活动功能

> 当前活动：正乌托邦（2025.10.23-2025.11.20）

- [x] 「正乌托邦」领取每日等效时
- [x] 「十环线圈」自动研发

<details>
<summary>往期活动</summary>

#### 曙光归途

> 2025.9.25 - 2025.10.23

- [x] 「曙光归途」领取每日小熊猫币
- [x] 「太空资源收集」新了个月
- [x] 「未来记忆」领取每日奖励
- [x] 「列车长的见面礼」领取体力

#### 雨中徐行

> 2025.8.21 - 2025.9.25

- [x] 「雨中徐行」领取每日痕迹
- [x] 「遗迹寻获」自动挖掘
- [x] 「列车长的见面礼」领取体力

#### 错航成旅

> 2025.7.24 - 2025.8.21

- [x] 「错航成旅」领取每日弹壳
- [x] 「缤纷纪念卡」领取每日票据
- [x] 「血橙与餐厅」自动炒菜机
- [x] 「码头八点半」自动驾驶（1-1 至 1-10）
- [x] 「列车长的见面礼」领取体力
- [x] 「今日南廷」获取奖励

#### 乐园不妙夜

> 2025.6.12 - 2025.7.24

- [x] 「乐园不妙夜」领取每日代币
- [x] 「融变超」合成大曦瓜
- [x] 「环线调度」自动驾驶
- [x] 「未来记忆」领取每日奖励

#### 往像螺旋

> 2025.5.29 - 2025.6.12

- [x] 「往像螺旋」每日决雍作战
- [x] 「往像螺旋」领取每日尘质
- [x] 「工坊开放日」领取奖励
- [x] 「流域清扫」自动清扫
- [x] 「今日南廷」领取每日奖励

#### 血茧时辙

> 2025.4.30 - 2025.5.29

- [x] 「血茧时辙」领取每日残片
- [x] 「决雍协定」领取体力与奖励

#### 禅世遗香

> 2025.4.3 - 2025.4.30

- [x] 「禅世遗香」领取每日禅香
- [x] 「列车长的见面礼」每日体力领取
- [x] 「未来记忆」领取今日奖励

</details>

### 常驻功能

- **登录签到**
  - [x] 启动登录
  - [x] 每日签到
  - [x] ~~紧张刺激的~~七日签到
- **检查邮件**
  - [x] 领取邮件奖励
  - [x] 删除已读邮件
- **每日采购**
  - [x] 免费补给包
  - [x] 数构银物资
  - [x] 情报物资
- **友谊交换**
  - [x] 情报点互换
  - [x] 自动同意好友
  - [x] 好友换新
- **清体力**
  - [x] 全种类资源
  - [x] 自动使用合剂
  - [x] 自动助战
- **城市探索**
  - [x] 资源收取
  - [x] 制造订单
  - [x] 设施管理
  - [x] 传闻调查
  - [x] 城市事件
- **每日升级**
  - [x] 特工升一级
  - [x] 卡带升一级
- **领取奖励**
  - [x] 角色升一级
  - [x] 每日/周任务
  - [x] 组长手册
- **轮换周常**
  - [x] 冰饮大热斗
  - [x] 自动站台肉鸽
  - [x] 拘束塔每周奖励
  - [ ] 险境复现
- **连续战斗**
  - [x] 不可自动战斗托管
  - [x] 连续作战
  - [x] 自动爬塔
- **实用小功能**
  - [x] 卡带升级
  - [x] 卡带词条定向
  - [x] 特工批量谈话
  - [x] 好友批量换新
  - [x] 剧情阅读器
  - [x] 抽卡统计

具体更新日志可参考[更新记录](/assets/resource/Announcement/3.更新记录.md)

\* 若有其他功能需求请提交 [issue](https://github.com/kqcoxn/MaaNewMoonAccompanying/issues?q=is%3Aissue)

## 使用教程

**每次版本更新后请手动把仅第一次出现的界面过一遍！**

- [文图教程](https://docs.codax.site/mnma/guide/users/start.html)

## 加入我们

🐧~~吹水~~交流群：[993245868](http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=VMC132QhbMDLi5U62MlDRvtCMj9WOXRr&authKey=yJNKO4sQ%2BBFHpBCLSSEvVOAyz%2FPjknNSl70W3ugg2%2BpELnKmEiHamj1emJMWcLwQ&noverify=0&group_code=993245868)

如果您在使用过程中遇到了问题、有更好的想法、希望参与开发，或是单纯想要聊天吹水，欢迎加入 MNMA 交流群！

## \*Mirror 酱支持

在 [Mirrorc 官方](https://mirrorchyan.com/zh/projects?source=mnma-github-code) 的帮助下， MNMA 同样也接入了 Mirror 酱 的国内高速下载与更新服务，详情请见[【Bilibili】震惊！MAA 开启收费功能？！](https://www.bilibili.com/video/BV1cZFreLEja/)

您可以通过 [此链接](https://mirrorchyan.com/zh/projects?rid=MNMA&source=mnma-github-code) 获取带有 Mirror 酱服务的 MNMA。

简单来说，Mirror 酱（简称 mirrorc）是一个由开源社区维护的有偿分发平台，可以理解为一个中转站，从海外源获取一份最新版存至国内站点，当您需要时直接从国内站点下载。

由于海内外下载、站点维护等需要，mirrorc 会产生大量开销，因此 mirrorc 的服务是有偿的，但这**并不代表 MNMA 是收费的，您完全可以通过其他方式更新并无限制使用，仅在您需要 mirrorc 时才需要自行向 mirrorc 方付费，MNMA 社区并不承担此过程中的一切责任，当出现问题时您可以在 mirrorc 客户群联系客服解决。**

## 免责声明

本软件开源、免费，仅供学习交流使用。若您遇到商家使用本软件进行代练并收费，可能是分发、设备或时间等费用，产生的费用、问题及后果与本软件无关。

**在使用过程中，MNMA 可能存在任何意想不到的问题，因 MNMA 自身漏洞、文本理解有歧义、异常操作导致的账号问题等开发组不承担任何责任，请在确保在阅读完用户手册、自行尝试运行效果后谨慎使用！**

## 常见问题

请确保现有 [issue](https://github.com/kqcoxn/MaaNewMoonAccompanying/issues?q=is%3Aissue) 中还没有与您遇到的类似的问题

- [文档站-用户手册-问题排查](https://docs.codax.site/mnma/guide/users/errors.html)

特别感谢 [@Yakir-George](https://github.com/Yakir-George) 在项目开发时期的测试与反馈！

如果有其他问题，欢迎提交 [issue](https://github.com/kqcoxn/MaaNewMoonAccompanying/issues?q=is%3Aissue)，或在 [交流群](http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=VMC132QhbMDLi5U62MlDRvtCMj9WOXRr&authKey=yJNKO4sQ%2BBFHpBCLSSEvVOAyz%2FPjknNSl70W3ugg2%2BpELnKmEiHamj1emJMWcLwQ&noverify=0&group_code=993245868) 内提问，您的反馈将使更多组长受益！

## 鸣谢

### 贡献者

感谢以下开发者对本项目作出的贡献:

[![Contributors](https://contrib.rocks/image?repo=kqcoxn/MaaNewMoonAccompanying&max=1000)](https://github.com/kqcoxn/MaaNewMoonAccompanying/graphs/contributors)

### 依赖与工具

- **本项目由 [MaaXYZ](https://github.com/MaaXYZ)/[MaaFramework](https://github.com/MaaXYZ/MaaFramework) 强力驱动！**
- 项目模板：[MaaXYZ](https://github.com/MaaXYZ)/[MaaPracticeBoilerplate](https://github.com/MaaXYZ/MaaPracticeBoilerplate)
- GUI：[SweetSmellFox](https://github.com/SweetSmellFox)/[MFAAvalonia](https://github.com/SweetSmellFox/MFAAvalonia/tree/master)
- Pipeline 编辑器：[kqcoxn](https://github.com/kqcoxn)/[MaaPipelineEditor](https://github.com/kqcoxn/MaaPipelineEditor)
- 截图小工具：[SweetSmellFox](https://github.com/SweetSmellFox)/[MFATools](https://github.com/SweetSmellFox/MFATools)
- 测试：[MaaXYZ](https://github.com/MaaXYZ)/[MaaDebugger](https://github.com/MaaXYZ/MaaDebugger)
- 分发：[MirrorChyan](https://github.com/MirrorChyan)/[Mirror 酱](https://mirrorchyan.com/zh/get-start?source=mnma-github-code)

游戏官网：[烛薪网络-新月同行](https://xytx.firewick.net/home)

## 统计

[![Star History Chart](https://api.star-history.com/svg?repos=kqcoxn/MaaNewMoonAccompanying&type=Date)](https://www.star-history.com/#kqcoxn/MaaNewMoonAccompanying&Date)
