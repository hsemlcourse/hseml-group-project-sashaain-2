from fastapi import FastAPI
import joblib
import numpy as np

from app.schemas import MeshFeatures

app = FastAPI()

model = joblib.load("models/random_forest.pkl")


@app.get("/")
def root():

    return {"message": "Mesh Quality API is running"}


@app.post("/predict")
def predict(features: MeshFeatures):

    X = np.array([[
        features.num_vertices,
        features.num_faces,
        features.num_combinatorial_degenerated_faces,
        features.num_connected_components,
        features.euler_characteristic,
        features.num_coplanar_intersecting_faces,
        features.vertex_manifold,
        features.edge_manifold,
        features.oriented,
        features.total_area,
        features.min_area,
        features.p25_area,
        features.median_area,
        features.p75_area,
        features.p90_area,
        features.p95_area,
        features.max_area,
        features.min_valance,
        features.p25_valance,
        features.median_valance,
        features.p75_valance,
        features.p90_valance,
        features.p95_valance,
        features.max_valance,
        features.min_dihedral_angle,
        features.p25_dihedral_angle,
        features.median_dihedral_angle,
        features.p75_dihedral_angle,
        features.p90_dihedral_angle,
        features.p95_dihedral_angle,
        features.max_dihedral_angle,
        features.min_aspect_ratio,
        features.p25_aspect_ratio,
        features.median_aspect_ratio,
        features.p75_aspect_ratio,
        features.p90_aspect_ratio,
        features.p95_aspect_ratio,
        features.max_aspect_ratio,
        features.PWN,
        features.solid,
        features.ave_area,
        features.ave_valance,
        features.ave_dihedral_angle,
        features.ave_aspect_ratio
    ]])

    prediction = int(model.predict(X)[0])

    probabilities = model.predict_proba(X)[0]

    probability_dict = {
        str(i): float(round(prob, 4))
        for i, prob in enumerate(probabilities)
    }

    return {
        "predicted_quality_class": prediction,
        "probabilities": probability_dict
    }