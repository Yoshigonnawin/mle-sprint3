FROM python:3.11-slim

LABEL author=${AUTHOR}

COPY . ./simple_fast_api

WORKDIR /simple_fast_api 
RUN pip3 install -r requirements.txt
# устанавливаем библиотеки из файла requirements.txt
# который ранее был скопирован инструкцией COPY . ./simple_fast_api
# вместе со всем содержимым текущей директории в simple_fast_api

VOLUME /speeches
EXPOSE ${APP_PORT}

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", ${APP_PORT}]