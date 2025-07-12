import os
import json
import requests


class Fetcher:
    def __init__(self):
        self._url = os.environ["HEIDI_URL"]
        self._headers = {"Authorization": os.environ["JWT_KEY"]}
        self._body = {
            "generation_method": "TEMPLATE",
            "addition": "",
            "template_id": "65bdb4aeecb06561b42f703b",
            "voice_style": "GOLDILOCKS",
            "brain": "LEFT",
        }

    def fetch(self, session_id: int) -> str:
        with requests.post(
            self._url.format(session_id=session_id),
            headers=self._headers,
            json=self._body,
            stream=True,
        ) as response:
            out = ""
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    line = chunk.decode("utf-8")
                    if not line.startswith("data: "):
                        continue
                    data = json.loads(line[6:])["data"]
                    out += data
            return out
