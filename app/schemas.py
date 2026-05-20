from pydantic import BaseModel


class MeshFeatures(BaseModel):
    num_vertices: float

    num_faces: float

    num_combinatorial_degenerated_faces: float

    num_connected_components: float

    euler_characteristic: float

    num_coplanar_intersecting_faces: float

    vertex_manifold: float

    edge_manifold: float

    oriented: float

    total_area: float

    min_area: float

    p25_area: float

    median_area: float

    p75_area: float

    p90_area: float

    p95_area: float

    max_area: float

    min_valance: float

    p25_valance: float

    median_valance: float

    p75_valance: float

    p90_valance: float

    p95_valance: float

    max_valance: float

    min_dihedral_angle: float

    p25_dihedral_angle: float

    median_dihedral_angle: float

    p75_dihedral_angle: float

    p90_dihedral_angle: float

    p95_dihedral_angle: float

    max_dihedral_angle: float

    min_aspect_ratio: float

    p25_aspect_ratio: float

    median_aspect_ratio: float

    p75_aspect_ratio: float

    p90_aspect_ratio: float

    p95_aspect_ratio: float

    max_aspect_ratio: float

    PWN: float

    solid: float

    ave_area: float

    ave_valance: float

    ave_dihedral_angle: float

    ave_aspect_ratio: float