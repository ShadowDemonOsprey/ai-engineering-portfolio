# Text Classification using Naive Bayes

## Overview

This project demonstrates a simple **Natural Language Processing (NLP)** text classification system using **Machine Learning**.

The model learns from text data and predicts the category (label) of new text inputs. It uses:

- **CountVectorizer** to convert text into numerical features
- **Multinomial Naive Bayes** algorithm for text classification

The example uses product reviews as input data and predicts the category of a new review.

---

## Features

- Load text data from a CSV file
- Convert text into numerical vectors
- Train a Naive Bayes classification model
- Predict labels for new text input
- Simple NLP machine learning pipeline

---

## Project Structure

```
text-classification/
│
├── data/
│   └── reviews.csv          # Training dataset
│
├── classifier.py            # Main Python script
│
├── requirements.txt         # Dependencies
│
└── README.md                # Documentation
```

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Natural Language Processing (NLP)
- Multinomial Naive Bayes

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project directory

```bash
cd text-classification
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Requirements

Create a file named:

```
requirements.txt
```

Add the following:

```
pandas
scikit-learn
```

Install:

```bash
pip install -r requirements.txt
```

---

## Dataset

The project uses a CSV dataset:

```
data/reviews.csv
```

The dataset should contain two columns:

| Column | Description |
|--------|-------------|
| text | Review text |
| label | Classification label |

Example:

```csv
text,label
"This product is amazing",positive
"I dislike this product",negative
"Very good quality",positive
"Poor experience",negative
```

---

## How It Works

### 1. Load Dataset

The program loads review data using Pandas.

```python
data = pd.read_csv("data/reviews.csv")
```

---

### 2. Convert Text into Numbers

Machine learning models cannot directly understand text.

`CountVectorizer` converts words into numerical feature vectors.

Example:

Input:

```
This product is wonderful
```

Converted into:

```
Numerical feature vector
```

---

### 3. Train the Model

The project uses the Multinomial Naive Bayes algorithm.

Training process:

```python
model.fit(X, labels)
```

The model learns patterns from the training reviews.

---

### 4. Predict New Text

A new review is transformed into a numerical vector and passed to the trained model.

Example:

```python
test_text = ["This product is wonderful"]
```

Prediction:

```
Prediction: positive
```

---

## Running the Project

Run the Python script:

```bash
python classifier.py
```

Example output:

```
Prediction: positive
```

---

## Machine Learning Concepts

### Natural Language Processing (NLP)

NLP allows computers to process and understand human language.

Applications:

- Sentiment analysis
- Spam detection
- Chatbots
- Search engines
- Document classification

---

### Bag of Words

CountVectorizer uses the Bag-of-Words technique.

It represents text based on the frequency of words.

Example:

Sentence:

```
I like this product
```

Features:

```
I
like
this
product
```

---

### Multinomial Naive Bayes

Multinomial Naive Bayes is a probability-based machine learning algorithm commonly used for text classification.

It is effective for:

- Sentiment analysis
- Email spam filtering
- Document classification

---

## Future Improvements

Possible improvements:

- Add train/test data split
- Measure model accuracy
- Use TF-IDF vectorization
- Add more training examples
- Create an API using FastAPI
- Deploy the model using Docker
- Integrate with a chatbot application

---

## Author

Your Name

---

## License

This project is created for learning and demonstration purposes.