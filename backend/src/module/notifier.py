import json
from datetime import datetime
import urllib.parse
from google import genai


PROMPT = """
Today is {now}

I'll give you an event prompt, I want you to extract the title, description, start and end dates. If no duration specified, just make it as 1 hour as default
Return a json format with this key
1. title (string): is a title event
2. start_time (string): format in %Y%m%dT%H%M%S
3. end_time (string): format in %Y%m%dT%H%M%S
4. description (string): the event description

```
{content}
```
"""


class Notifier:
    def __init__(self):
        self._client = genai.Client()
        self._model = "gemini-2.5-flash"
        self._base_url = "https://calendar.google.com/calendar/render?action=TEMPLATE&"

    def _create_url(self, params: dict[str, any]) -> str:
        calendar_params = {
            "text": params["title"],
            "dates": f"{params['start_time']}/{params['end_time']}",
            "details": params["description"],
        }
        return self._base_url + urllib.parse.urlencode(calendar_params)

    def create(self, content: str):
        data = PROMPT.format(
            content=content, now=datetime.now().strftime("%Y-%m-%d (%A)")
        )
        params = self._client.models.generate_content(model=self._model, contents=data)
        params = params.text.strip("```").strip("json")
        params = json.loads(params)

        return self._create_url(params)
