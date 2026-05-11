
from pydantic import BaseModel


class RunState(BaseModel):
    task: str
    research: str | None = None
    analysis: str | None = None
    draft: str | None = None
    critique: str | None = None
    iterations: int = 0

