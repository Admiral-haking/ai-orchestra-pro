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
