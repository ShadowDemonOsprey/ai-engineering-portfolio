from model_utils import save_model
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv("data/reviews.csv")

texts = data["text"]
labels = data["label"]

# Convert text into numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Test prediction
test_text = ["This product is wonderful"]

test_vector = vectorizer.transform(test_text)

prediction = model.predict(test_vector)

print("Prediction:", prediction[0])
save_model(model, "models/model.pkl")