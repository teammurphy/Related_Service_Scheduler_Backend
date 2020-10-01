FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . /app

RUN python -m pip install -r requirements.txt
