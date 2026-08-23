import os
import joblib

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def train_model():

    # Load dataset
    iris = load_iris()

    X = iris.data
    y = iris.target

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Create model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    # Train
    model.fit(X_train, y_train)

    # Create model directory
    os.makedirs("models", exist_ok=True)

    # Save model
    joblib.dump(
        model,
        "models/model.pkl"
    )

    print("Training completed")
    print("Model saved to models/model.pkl")


if __name__ == "__main__":
    train_model()