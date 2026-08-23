import joblib

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Load dataset
iris = load_iris()

X = iris.data
y = iris.target


# Same split used in training
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Load trained model
model = joblib.load("models/model.pkl")


# Prediction
predictions = model.predict(X_test)


# Accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy}")


# Pipeline quality gate
MIN_ACCURACY = 0.80

if accuracy < MIN_ACCURACY:
    raise Exception(
        f"Model accuracy {accuracy} is below required threshold "
        f"{MIN_ACCURACY}"
    )

print("Model validation successful")