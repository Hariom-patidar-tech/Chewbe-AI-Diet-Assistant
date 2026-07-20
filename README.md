# 🥗 Chew AI - Intelligent Diet Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![AI](https://img.shields.io/badge/AI-Powered-orange?style=for-the-badge)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

### 🍎 AI-Powered Personalized Nutrition & Diet Recommendation System

*Helping users achieve healthier lifestyles through intelligent meal planning, nutrition analysis, and AI-driven dietary recommendations.*

</div>

---

# 📌 Table of Contents

- Introduction
- Features
- Demo
- System Architecture
- Tech Stack
- Project Structure
- Installation
- Environment Variables
- Running the Project
- API Endpoints
- AI Workflow
- Machine Learning Pipeline
- Database Schema
- Future Improvements

- Author

---

# 📖 Introduction

**Chew AI** is an AI-powered Diet Assistant designed to provide personalized nutrition recommendations based on user health information, dietary preferences, lifestyle, fitness goals, allergies, and medical conditions.

Unlike traditional calorie calculators, Chew AI uses intelligent AI models to understand user requirements and generate customized meal plans while considering nutritional balance.

The application aims to make healthy eating simple, personalized, and accessible.

---

# ✨ Features

## 👤 User Features

- Personalized Profile
- Daily Calorie Calculation
- BMI Calculator
- BMR Calculator
- AI Meal Recommendations
- Weekly Meal Planner
- Nutrition Breakdown
- Weight Tracking
- Fitness Goal Tracking
- Allergy Detection
- Food Preference Selection
- Vegetarian / Vegan Support
- Keto Diet Support
- High Protein Plans
- Low Carb Plans
- Diabetic Friendly Plans
- Heart Healthy Diet Suggestions

---

## 🤖 AI Features

- Personalized Meal Recommendation
- Nutrition Analysis
- Smart Food Suggestions
- Portion Size Recommendation
- Goal-Based Meal Planning
- AI Food Chat Assistant
- Healthy Food Alternatives
- Recipe Recommendation
- Daily Nutrition Insights
- AI Health Tips

---

## 📊 Analytics

- Calories Consumed
- Calories Burned
- Protein Intake
- Carbohydrates Intake
- Fat Intake
- Water Consumption
- Weekly Reports
- Monthly Reports
- Progress Visualization

---

# 🚀 Demo

## User Flow

```
User Registration
        │
        ▼
Complete Health Profile
        │
        ▼
AI Analysis
        │
        ▼
Personalized Diet Plan
        │
        ▼
Meal Tracking
        │
        ▼
Nutrition Analytics
        │
        ▼
Progress Report
```

---

# 🏗 System Architecture

```
                ┌──────────────────────────┐
                │      Frontend (React)    │
                └────────────┬─────────────┘
                             │
                             ▼
                    FastAPI Backend
                             │
     ┌───────────────────────┼──────────────────────┐
     ▼                       ▼                      ▼
Authentication         AI Recommendation       Nutrition Engine
     │                       │                      │
     └───────────────┬───────┴───────────────┬──────┘
                     ▼                       ▼
              Machine Learning          Food Database
                     │
                     ▼
                  PostgreSQL
```

---

# 🛠 Tech Stack

## Backend

- Python
- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy

---

## AI / Machine Learning

- Scikit-learn
- TensorFlow
- PyTorch
- Hugging Face Transformers
- OpenAI / Groq API
- LangChain

---

## Database

- SQLite (Development)

---

## DevOps

- GitHub Actions
- Render

---

# 📂 Project Structure

```text
Chew-AI/
│
├── backend/
│   ├── api/
│   ├── models/
│   ├── services/
│   ├── database/
│   ├── routers/
│   ├── utils/
│   ├── ai/
│   ├── config/
│   └── main.py
├── datasets/
│
├── notebooks/
│
├── models/
│
├── docs/
│
├── tests/
│
├── requirements.txt
│
│
├── .env
│
└── README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/Hariom-patidar-tech/Chewbe-AI-Diet-Assistant
.git
```

```bash
cd Chewbe-AI-Diet-Assistant

```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
DATABASE_URL=

SECRET_KEY=

OPENAI_API_KEY=

GROQ_API_KEY=

JWT_SECRET=

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# ▶ Running the Project

## Backend

```bash
uvicorn main:app --reload
```

---


---

# 🌐 API Endpoints


## Nutrition

```
POST /nutrition-analysis
GET  /nutrition-report
```

---

## AI Chat

```
POST /chat
```

---

# 🧠 AI Workflow

```
User Input
      │
      ▼
Profile Analysis
      │
      ▼
BMI & BMR Calculation
      │
      ▼
Goal Detection
      │
      ▼
AI Nutrition Engine
      │
      ▼
Meal Recommendation
      │
      ▼
Diet Plan Generation
      │
      ▼
Progress Tracking
```

---

# 🤖 Machine Learning Pipeline

```
Dataset Collection
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Model Training
        │
        ▼
Evaluation


---

# 📊 Database Schema

## Users

| Field | Type |
|--------|------|
| id | Integer |
| name | String |
| email | String |
| password | String |
| age | Integer |
| gender | String |
| weight | Float |
| height | Float |
| goal | String |

---

## Meals

| Field | Type |
|--------|------|
| meal_id | Integer |
| meal_name | String |
| calories | Integer |
| protein | Float |
| carbs | Float |
| fats | Float |

---

## Progress

| Field | Type |
|--------|------|
| date | Date |
| calories | Integer |
| weight | Float |
| water | Float |

---


---

# 🎯 Future Improvements

- Voice-Based Diet Assistant
- Food Image Recognition
- Barcode Scanner
- Smart Grocery List
- Smart Kitchen Integration
- Wearable Device Integration
- Apple Health Integration
- Google Fit Integration
- AI Recipe Generator
- Multi-language Support
- OCR Food Label Scanner
- AI Health Coach
- Community Support
- Personalized Workout Plans

---


---



### Render

```bash
Build Command

pip install -r requirements.txt
```

```bash
Start Command

uvicorn main:app --host 0.0.0.0 --port 8000
```

---



# 📈 Roadmap

- AI Nutrition Engine
- Meal Recommendation
- Weekly Planner
- Food Recognition
- Smart Analytics
- Mobile Application
- Community Features

---


---

# 👨‍💻 Author

**Hariom Patidar**

AI & Machine Learning Engineer

- 💼 AI Developer
- 🤖 Machine Learning Enthusiast
- 📊 Data Science
- 🧠 NLP & LLM Applications
- ⚡ FastAPI Developer

---

<div align="center">

## ⭐ If you like this project, don't forget to Star the repository!

</div>
