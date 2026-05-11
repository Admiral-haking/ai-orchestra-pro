from __future__ import annotations

from typing import Any


def safe_exec(code: str, sandbox_vars: dict[str, Any] | None = None) -> dict[str, Any]:
    """Very constrained Python execution. Avoids builtins and IO.
    WARNING: For demo only; replace with a proper sandbox like pyodide or subprocess jail.
    """
    allowed_builtins = {"range": range, "len": len, "min": min, "max": max, "sum": sum}
    env: dict[str, Any] = {"__builtins__": allowed_builtins}
    if sandbox_vars:
        env.update({k: v for k, v in sandbox_vars.items() if k.isidentifier()})
    loc: dict[str, Any] = {}
    exec(code, env, loc)  # nosec B102
    return {k: v for k, v in loc.items() if not k.startswith("__")}
