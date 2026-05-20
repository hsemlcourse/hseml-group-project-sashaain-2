import joblib


def load_model():
    model = joblib.load('models/random_forest.pkl')
    return model