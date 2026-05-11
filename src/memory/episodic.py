from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Episode:
    id: str
    messages: list[str] = field(default_factory=list)


class EpisodicMemory:
    def __init__(self):
        self._episodes: dict[str, Episode] = {}

    def start(self, run_id: str):
        self._episodes[run_id] = Episode(id=run_id, messages=[])

    def add(self, run_id: str, text: str):
        self._episodes.setdefault(run_id, Episode(id=run_id)).messages.append(text)

    def get(self, run_id: str) -> Episode | None:
        return self._episodes.get(run_id)

