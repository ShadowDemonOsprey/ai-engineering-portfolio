from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "I love this product",
    "This is amazing",
    "I hate this product",
    "This is terrible"
]

labels = [
    "positive",
    "positive",
    "negative",
    "negative"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

test = ["I love this amazing product"]

test_vector = vectorizer.transform(test)

prediction = model.predict(test_vector)

print("Prediction:", prediction[0])