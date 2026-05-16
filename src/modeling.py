from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier


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

def train_knn(X_train, y_train, n_neighbors=3):
    model = KNeighborsClassifier(n_neighbors=n_neighbors)

    model.fit(X_train, y_train)

    return model

def train_decision_tree(
    X_train,
    y_train,
    max_depth=10
):
    model = DecisionTreeClassifier(
        max_depth=max_depth,
        random_state=42,
        class_weight='balanced'
    )

    model.fit(X_train, y_train)

    return model

def train_gradient_boosting(
    X_train,
    y_train,
    n_estimators=200,
    learning_rate=0.05
):
    model = GradientBoostingClassifier(
        n_estimators=n_estimators,
        learning_rate=learning_rate,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model