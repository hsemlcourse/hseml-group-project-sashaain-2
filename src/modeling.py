from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


def train_logistic_regression(X_train, y_train):
    scaler = StandardScaler()
    
    X_train_scaled = scaler.fit_transform(X_train)
    
    model = LogisticRegression(
        max_iter=1000,
        class_weight='balanced'
    )
    
    model.fit(X_train_scaled, y_train)
    
    return model, scaler

from sklearn.ensemble import RandomForestClassifier


def train_random_forest(X_train, y_train):
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
    
    model.fit(X_train, y_train)
    
    return model

def predict_logistic(model, scaler, X):
    X_scaled = scaler.transform(X)
    return model.predict(X_scaled)


def predict_model(model, X):
    return model.predict(X)