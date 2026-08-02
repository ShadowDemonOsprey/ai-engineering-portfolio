# Machine Learning Pipeline

## Goal

Build a complete machine learning workflow from data preparation to model evaluation.

## Pipeline Steps

1. Data loading
2. Data cleaning
3. Feature engineering
4. Model training
5. Model evaluation
6. Prediction

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn

## Status

Planning stage.

---

## Run with Docker

### Build Docker Image

From this folder:

```bash
docker build -t ml-pipeline .
```

### Run Container

```bash
docker run ml-pipeline
```

The container will execute the machine learning pipeline workflow.

## Pipeline Execution

The pipeline performs:

1. Data loading
2. Data preprocessing
3. Feature engineering
4. Model training
5. Model evaluation
6. Prediction

Example output:

```text
Data processing completed.
Model training completed.
Evaluation completed.
```