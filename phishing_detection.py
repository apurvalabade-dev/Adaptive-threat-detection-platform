from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate synthetic phishing data
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Phishing/Malware Detection Model
model_phishing = RandomForestClassifier()
model_phishing.fit(X_train, y_train)

# Testing the model
predictions = model_phishing.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Detection Model Accuracy: {accuracy}")
