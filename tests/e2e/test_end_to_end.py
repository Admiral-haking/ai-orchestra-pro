import os

import pytest

langgraph = pytest.importorskip("langgraph")
openai = pytest.importorskip("openai")

from src.app import main  # noqa: E402


@pytest.mark.skipif(
    not os.getenv("OPENAI_API_KEY"), reason="requires OPENAI_API_KEY for real call"
)
def test_cli_main_runs():
    # Just ensure it doesn't crash; manual inspection of output in CI logs
    main("سلام دنیا")

