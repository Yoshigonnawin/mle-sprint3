import numpy as np
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from prometheus_client import Counter, Histogram
from prometheus_fastapi_instrumentator import Instrumentator

# создание экземпляра FastAPI приложения
app = FastAPI()

# инициализируем и запускаем экпортёр метрик
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

main_app_predictions = Histogram(
    # имя метрики
    "main_app_predictions",
    # описание метрики
    "Histogram of predictions",
    # указываем корзины для гистограммы
    buckets=(1, 2, 4, 5, 10),
)

above_zeros = Counter("abover_zeros", "Predictions more then zeros")


# предсказания
@app.get("/predict")
def predict(x: int, y: int):
    # print(x)
    np.random.seed(int(abs(x)))
    prediction = x + y + np.random.normal(0, 1)
    main_app_predictions.observe(prediction)
    if prediction > 0:
        above_zeros.inc()
    return {"prediction": prediction}
