# AI Engineering Portfolio

Master's degree in Mathematics.  
Self-studying Artificial Intelligence and Machine Learning.

This repository contains practical AI and Machine Learning projects demonstrating skills in data processing, model development, API creation, Docker deployment, and AI application development.

---

# Repository Structure

```text
FIRST_AI_PROJECT
│
├── project_1_text_classifier
│   ├── Model training
│   ├── Text preprocessing
│   ├── Classification prediction
│   └── Dockerfile
│
├── project_2_sentiment_analysis
│   ├── FastAPI application
│   ├── Sentiment prediction endpoint
│   ├── REST API service
│   └── Dockerfile
│
├── project_3_ml_pipeline
│   ├── Data processing
│   ├── Feature engineering
│   ├── Model training
│   ├── Evaluation
│   └── Dockerfile
│
├── project_4_ai_chatbot
│   ├── FastAPI chatbot API
│   ├── User message processing
│   ├── AI response generation
│   └── Dockerfile
│
├── docker-compose.yml
│
├── .github
│   └── workflows
│       └── python-check.yml
│
├── README.md
├── PROFILE.md
├── PORTFOLIO.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
└── .gitignore

# Project 2: Sentiment Analysis API

## Overview

A simple REST API that analyzes text sentiment.

## Features

- FastAPI web service
- Text prediction endpoint
- JSON response format
- Docker container deployment
- REST API architecture

## Technologies

- Python
- FastAPI
- Uvicorn
- Machine Learning

---

## API Usage

### Endpoint

```text
GET /predict?text=I%20love%20this%20product

# Docker Support

This repository includes Docker support for running AI applications in isolated containers.

## Docker Images

The following projects include Docker support:

- AI Text Classification
- Sentiment Analysis API
- Machine Learning Pipeline
- AI Chatbot Assistant

---

## Build Docker Images

### Project 1: AI Text Classification

```bash
docker build -t text-classifier ./project_1_text_classifier