# IO Agent Cloud Tutorials

IO Agent Cloud is an MCP (Model Context Protocol) server by io.net that turns GPU cloud infrastructure into standardized tool interfaces. Any MCP-compatible AI agent (Claude Code, Cursor, Windsurf, etc.) can manage decentralized GPU resources through natural language — browse hardware, compare prices, deploy containers, and manage deployments without touching a console.

## Tutorials

| # | Notebook | Description | Colab |
|---|----------|-------------|-------|
| 1 | `1-io_cloud_mcp_tutorial.ipynb` | Direct MCP tool calls. Connect to the MCP server, browse GPU hardware catalog, estimate prices, deploy/destroy containers step by step. Covers the 7 core CaaS tools. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/maris205/learn_io_ai/blob/main/en_version/7-agent_cloud/1-io_cloud_mcp_tutorial.ipynb) |
| 2 | `2-io_cloud_agent_tutorial.ipynb` | LLM + MCP Agent loop. Wire GLM-5.1 (via IO Intelligence API) to MCP tools so the model auto-selects and invokes tools from natural language — the core Agent Cloud experience. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/maris205/learn_io_ai/blob/main/en_version/7-agent_cloud/2-io_cloud_agent_tutorial.ipynb) |
| 3 | `3-io_cloud_skills_tutorial.ipynb` | Skills orchestration. Compose multiple MCP tools into high-level Skills (`hardware_scout`, `smart_deploy`, `deployment_manager`) that chain operations automatically — fewer LLM calls, higher reliability. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/maris205/learn_io_ai/blob/main/en_version/7-agent_cloud/3-io_cloud_skills_tutorial.ipynb) |

## Links

- [IO Agent Cloud Documentation](https://io.net/docs/guides/clouds/agent-cloud)
- [Chinese Tutorials](https://github.com/maris205/learn_io_ai/tree/main/cn_version/7-agent_cloud)
