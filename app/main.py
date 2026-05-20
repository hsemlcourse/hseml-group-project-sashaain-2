from fastapi import FastAPI
import pandas as pd

from app.schemas import MeshFeatures
from app.utils import load_model


app = FastAPI()

model = load_model()


@app.get("/")
def root():
    return {"message": "Mesh Quality API is running"}


@app.post("/predict")
def predict(data: MeshFeatures):

    input_df = pd.DataFrame([data.dict()])

    prediction = model.predict(input_df)

    return {
        "predicted_quality_class": int(prediction[0])
    }