from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv


def _deep_merge(a: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
    out = dict(a)
    for k, v in b.items():
        if k in out and isinstance(out[k], dict) and isinstance(v, dict):
            out[k] = _deep_merge(out[k], v)
        else:
            out[k] = v
    return out


def load_config() -> dict[str, Any]:
    # Load .env once at startup (non-destructive)
    load_dotenv(override=False)
    base_path = Path("configs/base.yaml")
    env = os.getenv("APP_ENV", "dev").lower()
    override_path = Path(f"configs/{env}.yaml")

    def load_yaml(p: Path) -> dict[str, Any]:
        if not p.exists():
            return {}
        with p.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}

    cfg = load_yaml(base_path)
    override = load_yaml(override_path)
    merged = _deep_merge(cfg, override)
    return merged
