# Fynd Assessment Repository

This repository contains two tasks bundled in one project:

- **Task 1**: Prompt engineering and evaluation for review-to-star classification (interactive notebook).
- **Task 2**: A Django application providing a feedback dashboard with LLM-powered review analysis.

## 📊 Live Dashboards (Deploy Links)

- **Task 1 — Interactive Notebook** (Binder): https://mybinder.org/v2/gh/Manvika1610/fynd-assessment/main?urlpath=%2Fdoc%2Ftree%2Ftask1_rating_prompting.ipynb
- **Task 2 — Feedback Dashboard** (Django on Render): https://fynd-task2-dashboard.onrender.com/

## 📁 Repository Structure

```
.
├── task1_rating_prompting.ipynb       # Task 1: Notebook with prompt experiments
├── task1_scripts/                     # Supporting scripts for Task 1
│   ├── prompts.py                     # Prompt templates (direct, chain-of-thought, few-shot)
│   ├── llm_client.py                  # LLM API client (OpenRouter)
│   ├── evaluate_prompts.py            # Prompt evaluation harness
│   └── utils.py                       # Utilities (JSON extraction, data loading)
├── data/                              # Sample datasets
│   └── sample_yelp_200.csv            # Yelp reviews for evaluation
├── fynd_task2/                        # Task 2: Django project
│   ├── manage.py
│   ├── fynd_task2/                    # Django settings
│   └── feedback/                      # Main app
│       ├── models.py                  # Review model
│       ├── views.py                   # User & admin dashboards
│       ├── forms.py                   # Review form
│       ├── llm_client.py              # LLM integration
│       ├── templates/                 # HTML templates
│       └── migrations/
├── requirements.txt                   # Python dependencies
├── runtime.txt                        # Python version (for Render)
├── Procfile                           # Heroku/Render process file
├── start.sh                           # Startup script
├── build.sh                           # Build script for Render
├── .env.example                       # Template for environment variables
└── README.md                          # This file
```

## 🚀 Quick Start (Local)

1. **Clone the repository**:
   ```powershell
   git clone https://github.com/Manvika1610/fynd-assessment.git
   cd fynd-assessment
   ```

2. **Set up environment**:
   ```powershell
   # Copy .env.example to .env and fill in values
   Copy-Item .env.example .env
   # Edit .env with your OPENROUTER_API_KEY and DJANGO_SECRET_KEY
   ```

3. **Install dependencies**:
   ```powershell
   python -m pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```powershell
   cd fynd_task2
   python manage.py migrate
   python manage.py runserver
   ```

5. **Access**:
   - User Dashboard: http://localhost:8000
   - Admin Dashboard: http://localhost:8000/admin-dashboard/

## 📝 Task 1: Prompt Engineering

The notebook (`task1_rating_prompting.ipynb`) demonstrates prompt engineering techniques:

- **Direct Prompt**: Simple classification without reasoning.
- **Chain-of-Thought**: Step-by-step reasoning before classification.
- **Few-Shot Learning**: Providing examples to guide the model.

Evaluate each approach against a sample of 200 Yelp reviews and compare accuracy and JSON parsing rates.

**Live Binder Link**: https://mybinder.org/v2/gh/Manvika1610/fynd-assessment/main?urlpath=%2Fdoc%2Ftree%2Ftask1_rating_prompting.ipynb

## 💬 Task 2: Feedback Dashboard

A Django app that:

1. Users submit reviews with ratings (1-5 stars).
2. An LLM analyzes the review and returns:
   - **Summary**: 1–2 sentence summary of the review.
   - **Action**: Recommended business action.
   - **Reply**: Friendly response to the user.
3. Admin dashboard displays:
   - Total reviews and average rating.
   - Rating distribution (bar chart).
   - Table of all reviews with AI-generated insights.

**Live Dashboard**: https://fynd-task2-dashboard.onrender.com/

## 🔑 Environment Variables

Copy `.env.example` to `.env` and fill in:

```dotenv
OPENROUTER_API_KEY=your_openrouter_api_key_here
DJANGO_SECRET_KEY=your_secure_secret_key_here
DJANGO_DEBUG=False  # Set to False in production
```

The app will auto-load from `.env` using `python-dotenv`.

## 🌐 Deployment

Both tasks are deployed:

- **Task 1**: Binder (free, no setup needed — click the link and run).
- **Task 2**: Render (free tier, auto-deploys from GitHub on push).

For manual deployment details, see `DEPLOYMENT.md` and `QUICK_DEPLOY_GUIDE.md`.

## 📊 Key Technologies

- **Task 1**: Python, Jupyter, pandas, requests, LangChain (optional).
- **Task 2**: Django 6.0, SQLite, Bootstrap, Chart.js, WhiteNoise, gunicorn.
- **LLM API**: OpenRouter (supports multiple models; currently uses Mistral for Task 2, Gemma for Task 1).

## 📄 Documentation

- `PROJECT_README.md` — Project overview and structure.
- `DEPLOYMENT.md` — Detailed deployment instructions and troubleshooting.
- `QUICK_DEPLOY_GUIDE.md` — Quick start for deploying to Render and Binder.

## ✅ Notes

- The repository includes `.env` in `.gitignore` to prevent committing real secrets.
- All API keys and secrets should be set via environment variables.
- The Django app requires `OPENROUTER_API_KEY` at runtime to call the LLM.

---

**Happy coding!** 🎉
