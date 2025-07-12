from module.summarizer import Summarizer
from module.fetcher import Fetcher
from pydantic import BaseModel


class SessionRequest(BaseModel):
    session_id: int


class SummarizerController:
    def __init__(self):
        self._summarizer = Summarizer()
        self._fetcher = Fetcher()

    def summarize(self, body: SessionRequest) -> dict:
        content = self._fetcher.fetch(body.session_id)
        return self._summarizer.summarize(content)
