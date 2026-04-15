# When AI Learns to Manage GPUs: IO Agent Cloud Hands-On Tutorials Now Live

## Still Renting GPUs Manually?

Log into the console, browse the hardware list, compare prices, fill in parameters, hit deploy, wait for startup, check status...

The same routine, every single time.

Not anymore.

IO Agent Cloud lets you do it all with one sentence:

> "Find me the cheapest 4x H100 cluster and deploy my PyTorch image."

That's it. The AI automatically searches hardware, compares prices, provisions the deployment, confirms the status, and tells you: done, here's what it cost.

## Let's Talk Price First: It's Genuinely Cheap

No fluff, just numbers:

| GPU | io.net | AWS | Google Cloud | Lambda Labs |
|-----|--------|-----|-------------|-------------|
| RTX 4090 | **$0.30/hr** | - | - | $0.50/hr |
| A100 80G | **$1.39/hr** | $3.91/hr (p4d) | $3.67/hr | $1.99/hr |
| H100 80G | **$2.09/hr** | $5.12/hr (p5) | $4.28/hr | $2.49/hr |

io.net's pricing is typically **1/2 to 1/3** of mainstream cloud providers. The reason is simple — decentralization. io.net aggregates idle GPU capacity from around the world, with no heavy data center overhead. The cost structure is inherently lower.

For researchers, this means the same budget can run twice as many experiments.

## Now Let's Talk Security: The Natural Advantage of Decentralization

With traditional cloud GPUs, your data, models, and training logs are all stored centrally in their data centers. You trust them not to peek at your data, but you can't verify it.

io.net is different:

- **Decentralized distribution** — Your tasks run on randomly assigned nodes worldwide. No single entity can access your complete data
- **Destroy on completion** — When the container lifecycle ends, all data on the node is wiped clean. No traces left
- **No centralized storage** — io.net doesn't hold your data. The platform itself can't see what you're running
- **Short-lived isolation** — Every deployment is a fresh container environment. No cross-tenant data residue

For research involving sensitive data (medical imaging, genomic sequences, financial data), this architecture is more reassuring than traditional cloud security models.

## What Is IO Agent Cloud?

[IO Agent Cloud](https://io.net/docs/guides/clouds/agent-cloud) is an MCP (Model Context Protocol) server launched by io.net. It turns io.net's entire GPU cloud infrastructure into a set of standardized tool interfaces that any MCP-compatible AI agent (Claude Code, Cursor, Windsurf, etc.) can call directly.

In short: **It's the "hands and feet" for AI agents — enabling LLMs to not just chat, but actually operate infrastructure.**

Core capabilities:

- **Hardware browsing** — Real-time queries of GPU inventory, pricing, and specs across the io.net network
- **Smart deployment** — Create container clusters with one sentence, supporting custom images, environment variables, and port mapping
- **Deployment management** — Check status, extend duration, destroy deployments — all through natural language
- **Price estimation** — Get cost estimates before spending a dime
- **Dual authentication** — Supports both personal API keys and dynamic key forwarding for multi-tenant applications

Currently offering 18 MCP tools covering both CaaS (Container as a Service) and VMaaS (VM as a Service) product lines.

## How Does It Compare to Other Agent Platforms?

There's no shortage of AI agent platforms. Gemini can help you write code, Manus can operate a browser, everyone's building "AI assistants." But look closely — the resources they can orchestrate all share one ceiling: **generic CPU servers**.

| Capability | Gemini / ChatGPT | Manus | IO Agent Cloud |
|------------|-------------------|-------|----------------|
| Code generation | Yes | Yes | Yes (via LLM) |
| Browser automation | Limited | Yes | - |
| Rent a CPU server | Yes (Cloud Shell, etc.) | Yes (virtual sandbox) | Yes |
| **Rent a GPU server** | **No** | **No** | **Yes, and it's the core capability** |
| **Choose GPU model** | - | - | **A100 / H100 / 4090 / L40S — take your pick** |
| **Multi-node parallel deployment** | - | - | **Spin up N machines with one sentence** |
| **MCP standard protocol** | Not supported | Not supported | **Native support, 18 tools** |
| **Embed in agent systems** | Closed ecosystem | Closed ecosystem | **Plug-and-play with Claude Code / Cursor / Windsurf** |
| **Skills orchestration** | - | - | **Compose multi-tool workflows into high-level Skills** |

The key difference:

**Gemini and Manus give you a sandbox.** You can run Python scripts and manipulate files, but underneath it's a shared CPU VM — no GPU, no custom images, no persistent storage. Want to train a model? Sorry, not enough compute.

**IO Agent Cloud gives you the entire GPU cloud.** From $0.30/hr RTX 4090s to $2.09/hr H100s, from single-card fine-tuning to multi-node distributed training — you get as much compute as you need. And it's MCP-native — not a proprietary plugin for one platform, but an open standard that any MCP-compatible agent system can plug into.

This means:

- Say one sentence in **Claude Code** and deploy a GPU cluster
- Write code in **Cursor** while your agent ships training jobs to the cloud
- Work on a project in **Windsurf** and spin up GPU inference services on demand
- Build your own agent app and connect to GPU compute with a few lines of MCP SDK code

**Other agents write code in sandboxes. IO's agent runs models on real GPUs.**

## Real-World Scenarios: How Much Time Does It Actually Save?

### Scenario 1: Biology — Protein Function Prediction Fine-Tuning

Dr. Zhang is working on a protein function prediction project. She needs to LoRA fine-tune ESM-2 (Meta's protein language model, 650M parameters) on 20,000 lab-annotated enzyme activity samples, then run an evaluation round to get the F1 score.

**The old workflow:**

1. Log into 3 cloud platforms to compare prices, check which one has A100 80G available (ESM-2 fine-tuning needs at least 40G VRAM)
2. AWS p4d instances are queued up, Lambda Labs is sold out too, finally find one on some smaller platform
3. Manually configure the instance: select image, open ports, mount storage, set up SSH keys
4. SSH in and set up the environment: `pip install transformers peft accelerate`, resolve CUDA version conflicts
5. `scp` the dataset over — 300MB takes 20 minutes to transfer
6. Start training, hit OOM midway, adjust batch size, restart
7. Forget to shut down after training — charged for 8 extra hours
8. Next day the PI says "try a different learning rate" — repeat all of the above

**Total time: 2 days, of which actual training was only 3 hours.**

**Now with IO Agent Cloud:**

```
"Find me the cheapest A100 80G, deploy the nvcr.io/nvidia/pytorch:24.01-py3 image,
 mount my S3 dataset, 1 hour should be enough."
```

The agent automatically searches hardware, compares prices, and deploys. Container is ready in 3 minutes — training starts immediately. When it's done, the agent auto-destroys the instance. Not a penny wasted. PI wants different parameters? Just change one sentence and say it again.

**Total time: 3 hours 10 minutes, of which 3 hours is the training itself.**

And because it's io.net's decentralized network, Dr. Zhang's protein sequence data isn't stored centrally on any cloud provider's servers. Once the container is destroyed, the data vanishes with it. For research groups working on unpublished results, this matters.

### Scenario 2: NLP Research — Multilingual Sentiment Analysis Benchmark

Li is writing his thesis, comparing how different open-source models perform on Chinese financial sentiment analysis. He needs to fine-tune Qwen2.5-7B, Llama-3-8B, and GLM-4-9B separately, each with 3 hyperparameter configs — 9 experiments total.

**The old workflow:**

1. The lab has one 4090, wait for a senior student to finish (waited 3 days)
2. His turn — can only run one experiment at a time, 9 experiments took 4 days sequentially
3. Two runs crashed (Llama's tokenizer conflicted with the dataset encoding), debugging took half a day
4. After finishing, realized the Qwen run forgot to save the checkpoint — had to rerun
5. Manually collected metrics from 9 different directories to build a comparison table
6. Advisor's feedback: "Add a 14B model for comparison"

**Total time: nearly 2 weeks.**

**Now with IO Agent Cloud:**

```
"Spin up 3 of the cheapest 4090 machines, 2 hours each,
 deploy my training image registry.example.com/nlp-bench:v2,
 set MODEL_NAME to qwen2.5-7b, llama-3-8b, and glm-4-9b respectively."
```

Three machines start in parallel. All 9 experiments (3 hyperparameter configs per model) finish within 2 hours. Three 4090s for 2 hours — total cost $1.80. Advisor wants to add a 14B model? One more sentence, results in 10 minutes.

**Total time: 2 hours + a few sentences + under $2.**

---

Both scenarios share the same lesson: **The real value is in designing experiments and analyzing results, not wrestling with infrastructure.** IO Agent Cloud automates all the repetitive, tedious, error-prone steps in between — using the cheapest GPUs on the market, with decentralized architecture backing up your data security.

## What Did We Build?

We created a set of **3 progressive Jupyter Notebook tutorials**, from beginner to advanced, walking you through the complete IO Agent Cloud workflow step by step. Available in both Chinese and English. Every tutorial is a runnable notebook — not just theory.

### Tutorial 1: Direct MCP Tool Calls — Understanding the Basics

Connect to the MCP server from scratch and call raw tools one by one. You'll learn:

- How to connect to IO Cloud using the Python MCP SDK
- Browse the GPU hardware catalog, sort by price, find the cheapest card
- Estimate deployment costs (do the math before spending money)
- Deploy a real container (nginx), check its status, then destroy it

After this tutorial, you'll understand how IO Agent Cloud's 18 MCP tools work under the hood.

### Tutorial 2: LLM + MCP Agent — Natural Language Driven

Connect GLM-5.1 (via IO Intelligence API) to MCP tools and build a complete agent loop:

```
User speaks naturally → GLM-5.1 auto-selects tools → MCP executes → GLM-5.1 responds in plain language
```

Just say "show me available GPUs" and the model automatically decides which API to call, what parameters to pass, then translates the results into a readable answer. This is the core Agent Cloud experience — and the fundamental difference from traditional cloud consoles.

The tutorial demonstrates the full conversation flow from hardware queries and price estimation to deployment management. You can modify the prompts and chat with the agent yourself.

### Tutorial 3: Skills Orchestration — Production-Grade Architecture

Compose multiple MCP tools into high-level Skills, triggering multi-step workflows with a single sentence:

| Skill | Function | Internal Pipeline |
|-------|----------|-------------------|
| `hardware_scout` | Hardware recon | Query catalog → Sort → Filter → Recommend |
| `smart_deploy` | Smart deployment | Estimate price → Deploy → Confirm status |
| `deployment_manager` | Deployment manager | List / Check status / Destroy |

Compared to raw tools, Skills reduce the number of LLM calls, make workflows more reliable, and deliver a cleaner user experience. This is the mainstream agent architecture pattern being adopted by platforms like Dify, Coze, and OpenAI Assistants — and our tutorial teaches you to build it from scratch.

## Links

**Official Documentation**

- [IO Agent Cloud Docs](https://io.net/docs/guides/clouds/agent-cloud)

**Tutorial Code**

- [Chinese Tutorials](https://github.com/maris205/learn_io_ai/blob/main/cn_version/7-agent_cloud)
- [English Tutorials](https://github.com/maris205/learn_io_ai/tree/main/en_version/7-agent_cloud)

## Final Thoughts

The future of GPU cloud isn't a better console — it's no console at all.

Other agents write Hello World in sandboxes. IO's agent trains large models on H100s. Other agents are proprietary plugins locked to one ecosystem. IO's agent is built on the MCP open standard — one line of config to plug into any agent system. Other GPU clouds make you log in, browse, and configure everything yourself. IO's GPU cloud just listens to you.

And it's probably the cheapest GPU you'll find anywhere.

Give it a try.
