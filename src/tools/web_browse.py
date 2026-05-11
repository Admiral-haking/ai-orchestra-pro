from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any

import requests


@dataclass
class RateLimiter:
    rpm: int
    _tokens: float = 0
    _last: float = time.time()

    def acquire(self):
        now = time.time()
        elapsed = now - self._last
        refill = (self.rpm / 60.0) * elapsed
        self._tokens = min(self.rpm, self._tokens + refill)
        self._last = now
        if self._tokens < 1:
            # sleep to next token
            to_wait = (1 - self._tokens) * (60.0 / self.rpm)
            time.sleep(max(0.0, to_wait))
            self._tokens = 0
        else:
            self._tokens -= 1


def search(query: str, max_results: int = 3, limiter: RateLimiter | None = None) -> list[dict[str, Any]]:
    """Naive search stub: returns placeholders.
    Replace with a real search API if available.
    """
    if limiter:
        limiter.acquire()
    # Without external search, return structured placeholders
    return [
        {"title": f"نتیجه جستجو برای: {query}", "url": "https://example.com", "snippet": "..."}
        for _ in range(max_results)
    ]


def fetch(url: str, timeout: int = 10, limiter: RateLimiter | None = None) -> str:
    if limiter:
        limiter.acquire()
    headers = {"User-Agent": "AI-Orchestra-Pro/1.0"}
    r = requests.get(url, timeout=timeout, headers=headers)
    r.raise_for_status()
    # naive cleanup
    text = r.text
    return " ".join(text.split())[:5000]

