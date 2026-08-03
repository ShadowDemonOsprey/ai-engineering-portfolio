import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


data = pd.read_csv("data/reviews.csv")

X_train, X_test, y_train, y_test = train_test_split(
    data["text"],
    data["label"],
    test_size=0.2,
    random_state=42
)

vectorizer = CountVectorizer()

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

model = MultinomialNB()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model Evaluation")
print("----------------")
print(f"Accuracy: {accuracy:.2f}")