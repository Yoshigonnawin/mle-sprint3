from pathlib import Path

from catboost import CatBoostClassifier


def load_churn_model(model_path: str) -> CatBoostClassifier:
    """Загружаем обученную модель оттока.
    Args:
        model_path (str): Путь до модели.
    """
    try:
        model = CatBoostClassifier()
        model.load_model(model_path)
    except Exception as e:
        print(f"Failed to load model: {e}")
    else:
        return model


if __name__ == "__main__":
    pth = Path(__file__).parent.parent / "models" / "catboost_churn_model.bin"

    model = load_churn_model(pth.resolve().__str__())

    # выведите параметры модели через print(f"Model parameter names: {}")
    print(f'Model parameter names: {model.feature_names_}')
