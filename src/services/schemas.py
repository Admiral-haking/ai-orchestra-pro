from __future__ import annotations

from pydantic import BaseModel


class RunRequest(BaseModel):
    task: str
    options: dict | None = None


class RunResponse(BaseModel):
    draft: str
    iterations: int

