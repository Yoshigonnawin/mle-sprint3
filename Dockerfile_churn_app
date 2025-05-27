FROM python:3.11-slim
# возьмём образ, который мы скачали ранее и в котором уже установлен Python

LABEL author="mle-student"

COPY app ./app

WORKDIR /app

RUN pip3 install -r requirements.txt

VOLUME /models
EXPOSE 1702

CMD ["uvicorn", "churn_app:app","--reload","--port","1702","host","0.0.0.0"]
