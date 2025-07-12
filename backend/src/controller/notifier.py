from module.notifier import Notifier
from pydantic import BaseModel


class ContentRequest(BaseModel):
    content: str


class NotifierController:
    def __init__(self):
        self._notifier = Notifier()

    def create_url(self, body: ContentRequest) -> dict:
        return {"url": self._notifier.create(body.content)}
