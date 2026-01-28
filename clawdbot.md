

# Clawdbot 安装与设置：分步指南

Clawdbot可以将你自己的设备变成一个生活在你最喜欢的应用程序中的个人 AI 助手，本文详细分步介绍安装与配置过程。

- [](https://www.hubwiz.com/blog/author/admin-2/)

#### [admin](https://www.hubwiz.com/blog/author/admin-2/)

Jan 26, 2026 • 5 min read

![Clawdbot 安装与设置：分步指南](https://www.hubwiz.com/blog/content/images/size/w2000/2026/01/step-by-step-guide-to-install-clawdbot.png)

Clawdbot 是一个开源的个人 AI 助手，你自己运行，在你的计算机或服务器上。它连接到你已经使用的消息应用程序 — 如 WhatsApp、Telegram、Discord、Slack、Signal 或 iMessage — 并将大型语言模型变成一个真正个人的、始终可用的同伴，可以记住上下文甚至为你采取行动。

使 Clawdbot 脱颖而出的不是流行词技术，而是实用能力:

- 它随着时间的推移记住你的偏好和过去的对话。
- 它可以主动联系你，提供提醒、简报或警报，而不是等待消息。
- 它可以执行真正的计算机级任务，如浏览器自动化、网络研究等。
- 因为你自己托管它，你拥有对你的数据和配置的完全控制。

这种组合 — 持久记忆、主动行为、可扩展的技能和自托管控制 — 推动了为什么许多早期采用者认为 Clawdbot 是几年前承诺的但我们从未从大型科技公司得到的 AI 助手。

> _如果Clawdbot安装和使用需要帮助，可以联系微信：_ **_**ezpoda**_**

## 1、Clawdbot 的结构

虽然用户体验专注于聊天和消息，但 Clawdbot 底部是一个深思熟虑的架构，具有四个关键组件:

- 网关: 这是与消息平台并协调你的助手与外部世界之间的通信的中心集线器。
- 智能体: 由 Claude、GPT 或其他模型驱动，这是"思考"发生的地方 — 维护上下文、记忆和推理的地方。
- 技能: 可选扩展，赋予 Clawdbot 超越聊天的能力，如网络研究、浏览器自动化、电子邮件访问等。
- 记忆: 一个持久的、基于文件的系统，将你的对话、偏好和上下文存储为你可以检查或与工作流程集成的真实文件。

因为这些元素相互啮合且模块化，Clawdbot 比一刀切的云助手更具适应性 — 但也更加亲力亲为，特别是在安装期间。

**在本指南中，您将看到从头到尾的精确安装说明。**

开始之前你需要什么

- Node.js v22 或更高版本安装在您的系统上。
- Git(用于某些安装路径)。
- 命令行访问(macOS/Linux 上的 Terminal，Windows 上的 PowerShell/WSL)。
- 可选: pnpm(推荐的包管理器)或 npm。
- 你希望 Clawdbot 连接到的消息应用程序(例如，WhatsApp、Telegram)。

## 2、安装 Clawdbot

获取 Clawdbot 的最简单方法是通过官方安装程序脚本，该脚本检测你的操作系统并安装所需的一切。

在你的终端中，运行:

```
curl -fsSL https://clawd.bot/install.sh | bash
```

此脚本:

- 检测你的操作系统。
- 确保 Node.js 22+ 存在。
- 使用 npm 全局安装 Clawdbot。

如果你更喜欢手动控制，你可以克隆 [GitHub 仓库](https://github.com/clawdbot/clawdbot)并从源代码构建 — 但安装程序对大多数用户来说更容易。

或者，你也可以运行

```
npm install -g clawdbot@latest
```

请注意，你需要 node.js 20+ 版本来运行 clawdbot。使用以下命令更新 node.js

```
nvm install 22
```

## 3、运行设置向导

安装后，运行交互式入门向导，该向导将引导你完成初始配置:

```
clawdbot onboard
```

该向导询问几个重要问题:

- 在哪里运行网关?(你的机器上的本地或远程)。
- 如何向 AI 提供商进行身份验证(OpenAI/Anthropic 的 OAuth 或 API 密钥)。
- 你希望连接哪些消息提供商(WhatsApp、Telegram、Discord 等)。
- 是否将 Clawdbot 安装为后台服务(守护程序)。

这种引导式设置是配置 Clawdbot 的推荐方法 — 它会自动为你构建基本配置。

## 4、启动网关

Clawdbot 运行一个"网关"，这是一个将消息应用程序与 AI 智能体连接的本地服务器:

```
clawdbot gateway --port 18789 --verbose
```

此网关运行后:

- 在以下位置打开浏览器: [http://127.0.0.1:18789/](http://127.0.0.1:18789/)

这将打开 Clawdbot 控制仪表板，你可以在其中查看日志、链接帐户和管理会话。

## 5、连接你的消息应用程序

Clawdbot 支持许多你可以与助手交谈的界面:

**1. WhatsApp**

```
pnpm clawdbot login
```

运行上述命令后，会出现一个二维码，在 WhatsApp 的 _设置 → 链接设备_ 下扫描以链接。

**2. Telegram**

对于 Telegram，通过 [@BotFather](http://twitter.com/BotFather) 创建一个机器人，并在提示时将令牌粘贴到 Clawdbot 配置中。

Discord 令牌通过在 Discord 开发者门户中创建机器人来类似地工作。

完成后，你的助手将在这些频道中显示，就好像它是一个正常的聊天联系人。

## 6、验证你的安装

你要确保一切健康并运行:

```
clawdbot health
```

这确认网关、身份验证和频道连接都处于活动状态。

当你的 Clawdbot 启动时:

- 它记住上下文和你的对话。
- 它可以发送主动消息或提醒。
- 你可以安装技能给它更多的能力。

你可以将它连接到浏览器自动化、文件操作、电子邮件解析等工具。

---

原文链接: [How to Set Up Clawdbot — Step by Step guide to setup a personal bot](https://medium.com/modelmind/how-to-set-up-clawdbot-step-by-step-guide-to-setup-a-personal-bot-3e7957ed2975)

汇智网翻译整理，转载请标明出处

[![从氛围编码到氛围工程 (实用指南)](https://www.hubwiz.com/blog/content/images/size/w600/2026/01/from-vibe-coding-to-vibe-engineering-guide.png)](https://www.hubwiz.com/blog/from-vibe-coding-to-vibe-engineering-a-practical-guide/)

[

## 从氛围编码到氛围工程 (实用指南)

这篇文章是我从 Vibe Coding 转向 Vibe Engineering 的方式 —— 我用于 AI 优先开发的简单流程以及一系列启用它的技术。



](https://www.hubwiz.com/blog/from-vibe-coding-to-vibe-engineering-a-practical-guide/)

- [](https://www.hubwiz.com/blog/author/admin-2/)

[admin](https://www.hubwiz.com/blog/author/admin-2/)Jan 27, 2026 • 21 min read

[![AI编码革命：谁将获益？](https://www.hubwiz.com/blog/content/images/size/w600/2026/01/ai-coding-revolution-who-will-benefit.png)](https://www.hubwiz.com/blog/ai-coding-revolution-who-will-benefit/)

[

## AI编码革命：谁将获益？

新研究揭示了关于 AI 辅助编程的一个惊人真相：经验比你想象的更重要



](https://www.hubwiz.com/blog/ai-coding-revolution-who-will-benefit/)

- [](https://www.hubwiz.com/blog/author/admin-2/)

[admin](https://www.hubwiz.com/blog/author/admin-2/)Jan 27, 2026 • 5 min read

[![Google：Rust实战评估](https://www.hubwiz.com/blog/content/images/size/w600/2026/01/google-hands-on-evaluation-of-rust.png)](https://www.hubwiz.com/blog/google-hands-on-evaluation-of-rust/)

[

