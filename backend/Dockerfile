FROM python:3.12-slim

WORKDIR /usr

ENV PYTHONPATH=/usr/src
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

ENTRYPOINT ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]