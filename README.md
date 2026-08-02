# AI Engineering Portfolio

Master's degree in Mathematics.  
Self-studying Artificial Intelligence and Machine Learning.

## Project 1: AI Text Classification

### Goal
Build a machine learning model that classifies text into categories.

### Tools
- Python
- scikit-learn
- Pandas
- NumPy

### Status
Completed first working version.

## How to Run

1. Create and activate the conda environment:

```bash
conda activate ai-project

---

# Project 2: Sentiment Analysis API

## Overview
A simple REST API that analyzes text sentiment.

## Features
- FastAPI web service
- Text prediction endpoint
- JSON response format
- Ready for future machine learning model integration

## Technologies
- Python
- FastAPI
- Uvicorn
- Machine Learning

## API Example

### Request

Send a GET request to the prediction endpoint:

```text
GET /predict?text=I%20love%20this%20product

### Explanation
GET → HTTP request method
/predict → API endpoint for sentiment prediction
text= → input text sent to the AI system
%20 → represents a space in a URL

#### Example input:
I love this product

The API receives the text, analyzes it, and returns the sentiment prediction.

### Response

{
  "text": "I love this product",
  "sentiment": "positive"
}
