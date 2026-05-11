import pytest

openai = pytest.importorskip("openai")

from src.providers.openai_provider import OpenAIClient  # noqa: E402


def test_openai_client_name():
    c = OpenAIClient("gpt-4o")
    assert c.name().startswith("openai:")

