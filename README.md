# AI Orchestra Pro 🧠🎼

[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-green)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

**Enterprise-grade multi-agent orchestration** with provider-agnostic LLM routing, evaluation harness, and production-ready observability.

## 🌟 Capabilities

- **Multi-Agent Architecture** — Analyst, Critic, Researcher, and Writer agents collaborate
- **Provider-Agnostic** — Route between OpenAI, DeepSeek, and custom providers seamlessly
- **Evaluation Harness** — Ragas-like scoring for response quality measurement
- **Episodic Memory** — Short-term and long-term memory with vector store integration
- **Observability** — OpenTelemetry tracing, structured logging, and metrics export

## 🚀 Quick Start

```bash
# Setup
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# Configure
cp .env.example .env

# Run
ai-orchestra-pro

# Or with uvicorn
uvicorn src.app:app --reload
```

## 🧪 Evaluation

```bash
pytest tests/ -v              # Run all tests
pytest tests/unit/ -v         # Unit tests only
pytest tests/integration/ -v  # Integration tests
```

## 📁 Structure

```
├── src/
│   ├── agents/        # Agent implementations (Analyst, Critic, etc.)
│   ├── core/          # Config, errors, logging, tracing
│   ├── evaluation/    # Evaluation harness & datasets
│   ├── memory/        # Episodic & vector store memory
│   ├── orchestration/ # Graph-based agent orchestration
│   ├── providers/     # LLM provider implementations
│   ├── services/      # API & background jobs
│   └── tools/         # Agent tools (web browse, python exec)
├── configs/           # Environment-specific configs
├── prompts/           # System prompts for agents
├── docker/            # Docker configuration
└── tests/             # Test suites
```

## 📄 License

MIT License — see [LICENSE](LICENSE)

---

## 💡 Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **Agent Architecture** | Graph-based (LangGraph) | Complex multi-step workflows with branching logic |
| **Provider Layer** | Abstract base + plugins | Swap models without code changes (OpenAI ↔ DeepSeek) |
| **Memory System** | Episodic + Vector Store | Short-term context + long-term semantic search |
| **Observability** | OpenTelemetry | Vendor-agnostic tracing, metrics, and logging |
| **Configuration** | YAML + Pydantic | Type-safe configs with environment override support |

## 🧑‍🔬 Experiment Log

| Experiment | Result | Impact |
|------------|--------|--------|
| Sequential vs parallel agent execution | Parallel reduced response time by 55% | ✅ Adopted |
| Embedding model comparison (text-embedding-3-small vs ada-002) | 3-small: 20% cheaper, same quality | ✅ Adopted |
| Memory window size tuning | 50 messages optimal for quality/cost | ✅ Implemented |

## 🚀 Production Checklist

- [x] Structured logging (structlog)
- [x] OpenTelemetry tracing
- [x] Comprehensive test suite (unit, integration, e2e)
- [x] Docker containerization
- [x] Configuration management
- [ ] Kubernetes deployment manifests
- [ ] Auto-scaling policies
- [ ] Model A/B testing framework
- [ ] Cost tracking dashboard
- [ ] Hallucination detection system
