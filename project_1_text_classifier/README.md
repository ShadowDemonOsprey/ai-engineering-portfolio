# AI Text Classification

## Overview

A machine learning project that classifies text into categories using Natural Language Processing (NLP) techniques.

This project demonstrates a complete machine learning workflow:

- Data loading
- Text preprocessing
- Feature extraction
- Model training
- Prediction

---

## Project Structure

```text
project_1_text_classifier
│
├── src
│   └── text_classifier.py
│
├── data
│   └── reviews.csv
│
├── models
│
├── tests
│   └── test_classifier.py
│
├── logs
│
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Technologies

- Python
- NumPy
- Pandas
- Scikit-learn

---

## Dataset

Example dataset:

```text
text,label
"I love this product",positive
"This is amazing",positive
"I hate this product",negative
"This is terrible",negative
"The quality is excellent",positive
"The service was bad",negative
```

---

## Machine Learning Workflow

1. Load dataset
2. Clean and preprocess text
3. Convert text into numerical features
4. Train machine learning model
5. Evaluate model
6. Generate predictions

---

## Installation

Activate the environment:

```bash
conda activate ai-project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Project

Run the classifier:

```bash
python src/text_classifier.py
```

Example output:

```text
Prediction: positive
```

---

## Testing

Run tests:

```bash
pytest
```

---

## Docker

Build Docker image:

```bash
docker build -t text-classifier .
```

Run Docker container:

```bash
docker run text-classifier
```

Example output:

```text
Prediction: positive
```

---

## Future Improvements

- Save trained model using joblib
- Add model evaluation metrics
- Add REST API endpoint
- Add automated testing pipeline
- Deploy machine learning service