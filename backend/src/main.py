from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller.notifier import NotifierController
from controller.summarizer import SummarizerController

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

notifier = NotifierController()
summarizer = SummarizerController()


app.add_api_route("/notify/", notifier.create_url, methods=["POST"])
app.add_api_route("/summarize/", summarizer.summarize, methods=["POST"])
