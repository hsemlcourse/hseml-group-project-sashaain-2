import streamlit as st
import requests


def render_manual_input():

    st.subheader("Basic mesh features")
    
    solid = st.selectbox(
        "Solid mesh",
        [0, 1],
        index=1
    )

    min_area = st.number_input(
        "Minimum face area",
        min_value=0.0,
        value=0.1
    )

    PWN = st.selectbox(
        "PWN",
        [0, 1],
        index=1
    )

    edge_manifold = st.selectbox(
        "Edge manifold",
        [0, 1],
        index=1
    )

    num_vertices = st.number_input(
        "Number of vertices",
        min_value=0,
        value=1000
    )

    num_faces = st.number_input(
        "Number of faces",
        min_value=0,
        value=2000
    )

    total_area = st.number_input(
        "Total area",
        min_value=0.0,
        value=100.0
    )

    ave_aspect_ratio = st.number_input(
        "Average aspect ratio",
        min_value=0.0,
        value=1.8
    )


# ADVANCED 

    show_all = st.checkbox("Specify all 44 features")
    num_combinatorial_degenerated_faces = 0
    num_connected_components = 1
    euler_characteristic = 2
    num_coplanar_intersecting_faces = 0
    vertex_manifold = 1
    oriented = 1

    p25_area = 0.5
    median_area = 1.0
    p75_area = 1.5
    p90_area = 2.0
    p95_area = 2.5
    max_area = 5.0

    min_valance = 3
    p25_valance = 4
    median_valance = 5
    p75_valance = 6
    p90_valance = 7
    p95_valance = 8
    max_valance = 10

    min_dihedral_angle = 10
    p25_dihedral_angle = 20
    median_dihedral_angle = 30
    p75_dihedral_angle = 40
    p90_dihedral_angle = 50
    p95_dihedral_angle = 60
    max_dihedral_angle = 90

    min_aspect_ratio = 1.0
    p25_aspect_ratio = 1.2
    median_aspect_ratio = 1.5
    p75_aspect_ratio = 2.0
    p90_aspect_ratio = 2.5
    p95_aspect_ratio = 3.0
    max_aspect_ratio = 5.0

    ave_area = 1.2
    ave_valance = 5
    ave_dihedral_angle = 35

    if show_all:

        st.subheader("All mesh features")

        num_combinatorial_degenerated_faces = st.number_input(
            "Degenerated faces",
            min_value=0,
            value=0
        )

        num_connected_components = st.number_input(
            "Connected components",
            min_value=1,
            value=1
        )

        euler_characteristic = st.number_input(
            "Euler characteristic",
            value=2
        )

        num_coplanar_intersecting_faces = st.number_input(
            "Coplanar intersecting faces",
            min_value=0,
            value=0
        )

        vertex_manifold = st.selectbox(
            "Vertex manifold",
            [0, 1],
            index=1
        )

        oriented = st.selectbox(
            "Oriented",
            [0, 1],
            index=1
        )
        p25_area = st.number_input(
            "25th percentile area",
            min_value=0.0,
            value=0.5
        )

        median_area = st.number_input(
            "Median area",
            min_value=0.0,
            value=1.0
        )

        p75_area = st.number_input(
            "75th percentile area",
            min_value=0.0,
            value=1.5
        )

        p90_area = st.number_input(
            "90th percentile area",
            min_value=0.0,
            value=2.0
        )

        p95_area = st.number_input(
            "95th percentile area",
            min_value=0.0,
            value=2.5
        )

        max_area = st.number_input(
            "Maximum area",
            min_value=0.0,
            value=5.0
        )
        
        min_valance = st.number_input(
            "Minimum valance",
            min_value=0,
            value=3
        )

        p25_valance = st.number_input(
            "25th percentile valance",
            min_value=0,
            value=4
        )

        median_valance = st.number_input(
            "Median valance",
            min_value=0,
            value=5
        )

        p75_valance = st.number_input(
            "75th percentile valance",
            min_value=0,
            value=6
        )

        p90_valance = st.number_input(
            "90th percentile valance",
            min_value=0,
            value=7
        )

        p95_valance = st.number_input(
            "95th percentile valance",
            min_value=0,
            value=8
        )

        max_valance = st.number_input(
            "Maximum valance",
            min_value=0,
            value=10
        )

        min_dihedral_angle = st.number_input(
            "Minimum dihedral angle",
            min_value=0.0,
            value=10.0
        )

        p25_dihedral_angle = st.number_input(
            "25th percentile dihedral angle",
            min_value=0.0,
            value=20.0
        )

        median_dihedral_angle = st.number_input(
            "Median dihedral angle",
            min_value=0.0,
            value=30.0
        )

        p75_dihedral_angle = st.number_input(
            "75th percentile dihedral angle",
            min_value=0.0,
            value=40.0
        )

        p90_dihedral_angle = st.number_input(
            "90th percentile dihedral angle",
            min_value=0.0,
            value=50.0
        )

        p95_dihedral_angle = st.number_input(
            "95th percentile dihedral angle",
            min_value=0.0,
            value=60.0
        )

        max_dihedral_angle = st.number_input(
            "Maximum dihedral angle",
            min_value=0.0,
            value=90.0
        )

        min_aspect_ratio = st.number_input(
            "Minimum aspect ratio",
            min_value=0.0,
            value=1.0
        )

        p25_aspect_ratio = st.number_input(
            "25th percentile aspect ratio",
            min_value=0.0,
            value=1.2
        )

        median_aspect_ratio = st.number_input(
            "Median aspect ratio",
            min_value=0.0,
            value=1.5
        )

        p75_aspect_ratio = st.number_input(
            "75th percentile aspect ratio",
            min_value=0.0,
            value=2.0
        )

        p90_aspect_ratio = st.number_input(
            "90th percentile aspect ratio",
            min_value=0.0,
            value=2.5
        )

        p95_aspect_ratio = st.number_input(
            "95th percentile aspect ratio",
            min_value=0.0,
            value=3.0
        )

        max_aspect_ratio = st.number_input(
            "Maximum aspect ratio",
            min_value=0.0,
            value=5.0
        )

        ave_area = st.number_input(
            "Average area",
            min_value=0.0,
            value=1.2
        )

        ave_valance = st.number_input(
            "Average valance",
            min_value=0.0,
            value=5.0
        )

        ave_dihedral_angle = st.number_input(
            "Average dihedral angle",
            min_value=0.0,
            value=35.0
        )

    if st.button("Predict quality"):

        payload = {
            "num_vertices": num_vertices,
            "num_faces": num_faces,
            "num_combinatorial_degenerated_faces": num_combinatorial_degenerated_faces,
            "num_connected_components": num_connected_components,
            "euler_characteristic": euler_characteristic,
            "num_coplanar_intersecting_faces": num_coplanar_intersecting_faces,
            "vertex_manifold": vertex_manifold,
            "edge_manifold": edge_manifold,
            "oriented": oriented,
            "total_area": total_area,
            "min_area": min_area,
            "p25_area": p25_area,
            "median_area": median_area,
            "p75_area": p75_area,
            "p90_area": p90_area,
            "p95_area": p95_area,
            "max_area": max_area,
            "min_valance": min_valance,
            "p25_valance": p25_valance,
            "median_valance": median_valance,
            "p75_valance": p75_valance,
            "p90_valance": p90_valance,
            "p95_valance": p95_valance,
            "max_valance": max_valance,
            "min_dihedral_angle": min_dihedral_angle,
            "p25_dihedral_angle": p25_dihedral_angle,
            "median_dihedral_angle": median_dihedral_angle,
            "p75_dihedral_angle": p75_dihedral_angle,
            "p90_dihedral_angle": p90_dihedral_angle,
            "p95_dihedral_angle": p95_dihedral_angle,
            "max_dihedral_angle": max_dihedral_angle,
            "min_aspect_ratio": min_aspect_ratio,
            "p25_aspect_ratio": p25_aspect_ratio,
            "median_aspect_ratio": median_aspect_ratio,
            "p75_aspect_ratio": p75_aspect_ratio,
            "p90_aspect_ratio": p90_aspect_ratio,
            "p95_aspect_ratio": p95_aspect_ratio,
            "max_aspect_ratio": max_aspect_ratio,
            "PWN": PWN,
            "solid": solid,
            "ave_area": ave_area,
            "ave_valance": ave_valance,
            "ave_dihedral_angle": ave_dihedral_angle,
            "ave_aspect_ratio": ave_aspect_ratio
        }

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        prediction = response.json()

        st.success(
            f"Predicted quality class: "
            f"{prediction['predicted_quality_class']}"
        )