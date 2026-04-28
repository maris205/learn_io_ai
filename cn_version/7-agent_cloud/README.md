# IO Agent Cloud 教程

IO Agent Cloud 是 io.net 提供的 MCP (Model Context Protocol) 服务，它把 GPU 云基础设施封装成标准化工具接口。任何兼容 MCP 的 AI Agent（如 Claude Code、Cursor、Windsurf 等）都可以通过自然语言直接管理去中心化 GPU 资源，例如浏览硬件、比较价格、部署容器和管理部署状态，而不需要手动操作控制台。

## 教程列表

| # | Notebook | 说明 | Colab |
|---|----------|------|-------|
| 1 | `1-io_cloud_mcp_tutorial.ipynb` | 直接调用 MCP 工具。从零开始连接 MCP 服务，浏览 GPU 硬件目录、估算价格、部署/销毁容器，逐步理解底层 CaaS 工具的使用方式。 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/maris205/learn_io_ai/blob/main/cn_version/7-agent_cloud/1-io_cloud_mcp_tutorial.ipynb) |
| 2 | `2-io_cloud_agent_tutorial.ipynb` | LLM + MCP 智能体循环。将 GLM-5.1（通过 IO Intelligence API）接到 MCP 工具上，让模型根据自然语言自动选择并调用工具，体验 Agent Cloud 的核心工作流。 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/maris205/learn_io_ai/blob/main/cn_version/7-agent_cloud/2-io_cloud_agent_tutorial.ipynb) |
| 3 | `3-io_cloud_skills_tutorial.ipynb` | Skills 编排。把多个 MCP 工具封装成高级 Skill（如 `hardware_scout`、`smart_deploy`、`deployment_manager`），自动串联多步操作，减少 LLM 调用次数并提升稳定性。 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/maris205/learn_io_ai/blob/main/cn_version/7-agent_cloud/3-io_cloud_skills_tutorial.ipynb) |

## 相关链接

- [IO Agent Cloud 官方文档](https://io.net/docs/guides/clouds/agent-cloud)
- [English Tutorials](https://github.com/maris205/learn_io_ai/tree/main/en_version/7-agent_cloud)
