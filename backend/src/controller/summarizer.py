from functools import lru_cache

from module.summarizer import Summarizer
from module.fetcher import Fetcher
from pydantic import BaseModel


class SessionRequest(BaseModel):
    session_id: int


class SummarizerController:
    def __init__(self):
        self._summarizer = Summarizer()
        self._fetcher = Fetcher()

    @lru_cache(maxsize=128)
    def _summarize(self, session_id: str) -> dict:
        content = self._fetcher.fetch(session_id)
        out = self._summarizer.summarize(content)
        return out

    def summarize(self, body: SessionRequest) -> dict:
        return self._summarize(body.session_id)
