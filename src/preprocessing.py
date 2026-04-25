import numpy as np

def clean_data(df):
    df = df.drop_duplicates()
    df = df[df['num_vertices']>0]
    df = df[df['num_faces']>0]
    
    df = df.fillna(df.median(numeric_only=True))
    
    df = df[df['ave_aspect_ratio']>= 0]
    df = df[df['max_aspect_ratio']>= 0]
    
    skewed_cols = [ 'max_aspect_ratio',
                   'ave_aspect_ratio',
                   'max_area',
                   'total_area']
    for col in skewed_cols:
        if col in df.columns:
            df[col] = np.log1p(df[col])
    return df

def create_target(df):
    df = df.copy()
    
    score = (
        (df['num_self_intersections'] > 0).astype(int) +
        (df['num_boundary_edges'] > 0).astype(int) +
        (df['num_duplicated_faces'] > 0).astype(int) +
        (df['num_geometrical_degenerated_faces'] > 0).astype(int)
    )
    
    df['quality_class'] = score
    
    return df
    