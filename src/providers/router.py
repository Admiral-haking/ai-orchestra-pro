from __future__ import annotations

import os
from typing import Any


def get_client_for(role: str, cfg: dict[str, Any]):
    route = cfg["providers"]["routing"].get(role)
    provider, model = route.split(":")

    # Dev/CI support: DRY_RUN or dummy provider
    if os.getenv("DRY_RUN") == "1" or provider == "dummy":
        from .dummy_provider import DummyClient  # lazy import

        return DummyClient(model)

    if provider == "openai":
        # Fallback to dummy if key missing
        if not os.getenv("OPENAI_API_KEY"):
            from .dummy_provider import DummyClient  # lazy import

            return DummyClient(f"fallback-{model}")
        from .openai_provider import OpenAIClient  # lazy import

        return OpenAIClient(model)
    if provider == "deepseek":
        # Fallback to dummy if key missing
        if not os.getenv("DEEPSEEK_API_KEY"):
            from .dummy_provider import DummyClient  # lazy import

            return DummyClient(f"fallback-{model}")
        from .deepseek_provider import DeepSeekClient  # lazy import

        return DeepSeekClient(model)
    raise ValueError(f"Unknown provider {provider}")
