import joblib
import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def load_model():

    model = joblib.load(
        "models/random_forest.pkl"
    )

    return model


def get_quality_description(
    predicted_class
):

    descriptions = {
        0: (
            "Excellent mesh quality. "
            "Geometry and topology are clean."
        ),
        1: (
            "Good mesh quality with "
            "minor defects."
        ),
        2: (
            "Moderate mesh quality. "
            "Several issues detected."
        ),
        3: (
            "Poor mesh quality. "
            "Mesh contains significant defects."
        ),
        4: (
            "Critical mesh quality. "
            "Mesh is heavily corrupted."
        )
    }

    return descriptions.get(
        predicted_class,
        "Unknown quality class."
    )


def analyze_key_features(payload):

    analysis = []

    if payload["solid"] == 0:

        analysis.append(
            {
                "Feature": "solid",
                "Your value": 0,
                "Recommended": 1,
                "Impact": (
                    "Mesh is not watertight. "
                    "This strongly decreases "
                    "mesh quality."
                )
            }
        )
    if payload["PWN"] == 0:

        analysis.append(
            {
                "Feature": "PWN",
                "Your value": 0,
                "Recommended": 1,
                "Impact": (
                    "Possible self-intersections "
                    "or inconsistent winding detected."
                )
            }
        )

    if payload["edge_manifold"] == 0:

        analysis.append(
            {
                "Feature": "edge_manifold",
                "Your value": 0,
                "Recommended": 1,
                "Impact": (
                    "Non-manifold edges detected. "
                    "This is a major topological defect."
                )
            }
        )

    if payload["vertex_manifold"] == 0:

        analysis.append(
            {
                "Feature": "vertex_manifold",
                "Your value": 0,
                "Recommended": 1,
                "Impact": (
                    "Non-manifold vertices detected. "
                    "Mesh topology is unstable."
                )
            }
        )

    if payload["oriented"] == 0:

        analysis.append(
            {
                "Feature": "oriented",
                "Your value": 0,
                "Recommended": 1,
                "Impact": (
                    "Mesh normals are inconsistent. "
                    "Rendering and geometry processing "
                    "may fail."
                )
            }
        )

    if payload["min_area"] < 0.001:

        analysis.append(
            {
                "Feature": "min_area",
                "Your value": (
                    f"{payload['min_area']:.6f}"
                ),
                "Recommended": "> 0.001",
                "Impact": (
                    "Very small triangles detected. "
                    "Tiny faces may cause "
                    "numerical instability."
                )
            }
        )

    if payload["max_aspect_ratio"] > 5:

        analysis.append(
            {
                "Feature": "max_aspect_ratio",
                "Your value": (
                    f"{payload['max_aspect_ratio']:.2f}"
                ),
                "Recommended": "< 5",
                "Impact": (
                    "Highly stretched triangles detected. "
                    "This negatively affects "
                    "mesh quality."
                )
            }
        )

    if payload[
        "max_dihedral_angle"
    ] > 160:

        analysis.append(
            {
                "Feature": (
                    "max_dihedral_angle"
                ),
                "Your value": (
                    f"{payload['max_dihedral_angle']:.2f}"
                ),
                "Recommended": "< 160",
                "Impact": (
                    "Extremely sharp angles detected. "
                    "Mesh geometry may be unstable."
                )
            }
        )

    return analysis


def create_radar_chart(payload):
    solid_score = (
        100 if payload["solid"] == 1
        else 40
    )

    pwn_score = (
        100 if payload["PWN"] == 1
        else 35
    )

    edge_score = (
        100 if payload["edge_manifold"] == 1
        else 30
    )

    vertex_score = (
        100 if payload["vertex_manifold"] == 1
        else 30
    )

    orientation_score = (
        100 if payload["oriented"] == 1
        else 40
    )

    max_aspect_ratio = payload[
        "max_aspect_ratio"
    ]

    if max_aspect_ratio <= 5:

        aspect_score = 100

    elif max_aspect_ratio <= 15:

        aspect_score = 75

    elif max_aspect_ratio <= 40:

        aspect_score = 45

    else:

        aspect_score = 15

    min_area = payload["min_area"]

    if min_area >= 0.01:

        area_score = 100

    elif min_area >= 0.001:

        area_score = 70

    elif min_area >= 0.0001:

        area_score = 40

    else:

        area_score = 10

    max_angle = payload[
        "max_dihedral_angle"
    ]

    if max_angle <= 120:

        angle_score = 100

    elif max_angle <= 150:

        angle_score = 70

    elif max_angle <= 170:

        angle_score = 40

    else:

        angle_score = 10

    categories = [
        "Solid",
        "PWN",
        "Edge Manifold",
        "Vertex Manifold",
        "Orientation",
        "Aspect Ratio",
        "Face Area",
        "Dihedral Angle"
    ]

    values = [
        solid_score,
        pwn_score,
        edge_score,
        vertex_score,
        orientation_score,
        aspect_score,
        area_score,
        angle_score
    ]

    values += values[:1]
    categories += categories[:1]

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=categories,
            fill="toself",
            name="Mesh Quality"
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=False,
        height=600
    )

    return fig


def display_prediction_results(
    prediction,
    payload
):

    predicted_class = prediction[
        "predicted_quality_class"
    ]

    probabilities = prediction[
        "probabilities"
    ]

    quality_description = (
        get_quality_description(
            predicted_class
        )
    )

    st.success(
        f"Predicted quality class: "
        f"{predicted_class}"
    )

    st.info(
        f"Mesh quality assessment: "
        f"{quality_description}"
    )

    confidence = max(
        probabilities.values()
    )

    st.metric(
        label="Model confidence",
        value=f"{confidence:.2%}"
    )

    st.subheader(
        "Class probabilities"
    )

    probability_df = pd.DataFrame(
        {
            "Class": list(
                probabilities.keys()
            ),
            "Probability": list(
                probabilities.values()
            )
        }
    )

    st.bar_chart(
        probability_df.set_index(
            "Class"
        )
    )

    st.subheader(
        "Mesh quality radar"
    )

    radar_fig = create_radar_chart(
        payload
    )

    st.plotly_chart(
        radar_fig,
        use_container_width=True
    )

    st.subheader(
        "Important feature analysis"
    )

    analysis = analyze_key_features(
        payload
    )

    if len(analysis) == 0:

        st.success(
            "Key mesh parameters are "
            "within recommended ranges."
        )

    else:

        analysis_df = pd.DataFrame(
            analysis
        )

        st.dataframe(
            analysis_df,
            use_container_width=True
        )

    st.subheader(
        "Mesh statistics"
    )

    stats_df = pd.DataFrame(
        {
            "Metric": [
                "Vertices",
                "Faces",
                "Connected components",
                "Total area",
                "Average aspect ratio",
                "Maximum aspect ratio",
                "Maximum dihedral angle"
            ],
            "Value": [
                payload["num_vertices"],
                payload["num_faces"],
                payload[
                    "num_connected_components"
                ],
                payload["total_area"],
                payload[
                    "ave_aspect_ratio"
                ],
                payload[
                    "max_aspect_ratio"
                ],
                payload[
                    "max_dihedral_angle"
                ]
            ]
        }
    )

    st.dataframe(
        stats_df,
        use_container_width=True
    )