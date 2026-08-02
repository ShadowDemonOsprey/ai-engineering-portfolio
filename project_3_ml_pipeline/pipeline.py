import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


# Load data
data = pd.DataFrame({
    "text": [
        "I love this product",
        "This is amazing",
        "I hate this product",
        "This is terrible",
        "Very good experience",
        "Very bad experience"
    ],
    "label": [
        "positive",
        "positive",
        "negative",
        "negative",
        "positive",
        "negative"
    ]
})


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    data["text"],
    data["label"],
    test_size=0.33,
    random_state=42
)


# Convert text to features
vectorizer = CountVectorizer()

X_train_vector = vectorizer.fit_transform(X_train)
X_test_vector = vectorizer.transform(X_test)


# Train model
model = MultinomialNB()

model.fit(X_train_vector, y_train)


# Evaluate model
predictions = model.predict(X_test_vector)

accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)


# Test prediction
new_text = ["This is a great product"]

new_vector = vectorizer.transform(new_text)

result = model.predict(new_vector)

print("Prediction:", result[0])

