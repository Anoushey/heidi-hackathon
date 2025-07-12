from fastapi import FastAPI
from controller.notifier import NotifierController
from controller.summarizer import SummarizerController

app = FastAPI()


notifier = NotifierController()
summarizer = SummarizerController()


app.add_api_route("/notify/", notifier.create_url, methods=["POST"])
app.add_api_route("/summarize/", summarizer.summarize, methods=["POST"])
