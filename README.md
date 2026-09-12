# 📄 AI-Powered Resume Parser

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-teal.svg)
![SpaCy](https://img.shields.io/badge/SpaCy-NLP-blue.svg)

An intelligent API service that extracts structured information (Name, Email, Skills, Experience) from unstructured resumes (PDF/DOCX) using Custom Named Entity Recognition (NER) via SpaCy.

## Features
- ⚡ Blazing fast FastAPI REST API
- 🧠 SpaCy-powered Named Entity Recognition
- 📄 Supports multi-format parsing (PDF, DOCX)
- 🎯 Job Description skill matching functionality

## Quick Start
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
uvicorn app:app --reload
```
