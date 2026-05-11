from __future__ import annotations

from collections.abc import Callable

from src.core.errors import ToolNotAllowedError


class ToolRegistry:
    def __init__(self, allowlist: list[str]):
        self.allow = set(allowlist)
        self.tools: dict[str, Callable] = {}

    def register(self, name: str, fn: Callable):
        if name not in self.allow:
            raise ToolNotAllowedError(f"Tool {name} not allowed")
        self.tools[name] = fn

    def call(self, name: str, **kwargs):
        if name not in self.tools:
            raise KeyError(f"Tool {name} not registered")
        return self.tools[name](**kwargs)

