import pytest

from src.tools.registry import ToolRegistry


def test_tool_registry_allowlist():
    reg = ToolRegistry(["ok"])
    with pytest.raises(PermissionError):
        reg.register("not_ok", lambda: None)

    called = {"v": False}
    reg.register("ok", lambda: called.update(v=True))
    reg.call("ok")
    assert called["v"] is True

