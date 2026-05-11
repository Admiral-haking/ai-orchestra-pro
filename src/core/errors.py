class ProviderError(Exception):
    """Raised when an LLM provider call fails."""


class ToolNotAllowedError(PermissionError):
    """Raised when a tool is not on the allowlist."""


class InvalidOutputError(ValueError):
    """Raised when an agent output violates the expected schema."""

