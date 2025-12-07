# Quick Deploy Guide

This guide walks you through deploying Task 2 (Django app) and Task 1 (notebook).

## Task 2: Django App Deployment (Render)

Render is free, easy, and auto-deploys from GitHub.

**Steps:**

1. **Push this repo to GitHub** (if not already done):
   ```powershell
   git init
   git add .
   git commit -m "Initial commit with deployment config"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/fynd-assessment.git
   git push -u origin main
   ```

2. **Create a Render account** at https://render.com (free tier available).

3. **Connect Render to your GitHub repo**:
   - Go to Render dashboard → New Web Service.
   - Select "Connect a repository" → authorize GitHub → select your repo.

4. **Configure the service**:
   - Name: `fynd-task2-app`
   - Environment: `Python 3`
   - Build command: `pip install -r requirements.txt && python fynd_task2/manage.py migrate`
   - Start command: `gunicorn fynd_task2.wsgi --log-file -`
   - Plan: Free tier (fine for demos)

5. **Set environment variables** in Render dashboard:
   - `DJANGO_SECRET_KEY` — Use a strong random string (generate one or let Render auto-generate).
   - `OPENROUTER_API_KEY` — Paste your OpenRouter API key.
   - `DJANGO_DEBUG` — Set to `False` (production).
   - `ALLOWED_HOSTS` — Set to your Render domain (e.g., `fynd-task2-app.onrender.com`).

6. **Deploy**:
   - Render will automatically deploy when you push to `main`.
   - Watch the build logs in the Render dashboard.
   - Once live, your app URL will be shown (e.g., `https://fynd-task2-app.onrender.com`).

7. **Update the deployment link**:
   - Copy your live Task 2 URL and replace `<YOUR_TASK2_DASHBOARD_URL>` in `PROJECT_README.md` and `DEPLOYMENT.md`.

---

## Task 1: Notebook Deployment (Binder / Voila)

**Option A: Binder (simplest, no setup)**

- Visit https://mybinder.org.
- Paste your repository URL (e.g., `https://github.com/YOUR_USERNAME/fynd-assessment`).
- Set the branch to `main` and path to `task1_rating_prompting.ipynb`.
- Click "Copy the URL for sharing" — this is your Task 1 deployment link.
- Replace `<YOUR_TASK1_NOTEBOOK_DEPLOY_URL>` in `PROJECT_README.md` and `DEPLOYMENT.md` with this URL.

**Option B: Voila (interactive dashboard)**

- Same as Binder but add `/voila/render/` to the URL to get an interactive dashboard view.

**Option C: NBViewer + GitHub**

- Host the repo on GitHub.
- Visit https://nbviewer.org and paste the raw GitHub URL to your notebook.
- Use the NBViewer URL as your deployment link.

---

## Verify Both Dashboards

After deployment:

1. Visit your Task 2 Django URL (e.g., `https://fynd-task2-app.onrender.com`).
   - You should see the User Dashboard form and Admin Dashboard link.
   - Try submitting a review to test the LLM integration.

2. Visit your Task 1 Binder URL.
   - The notebook should open in a Jupyter session.
   - You can run cells and experiment with prompts.

---

## Update README with Real URLs

Once both are live, update the placeholders in:
- `PROJECT_README.md` — Replace `<YOUR_TASK1_NOTEBOOK_DEPLOY_URL>` and `<YOUR_TASK2_DASHBOARD_URL>`.
- `DEPLOYMENT.md` — Do the same.

Then push to GitHub and Render will auto-redeploy.

---

## Troubleshooting

**"DJANGO_SECRET_KEY is not set"**
- Make sure `DJANGO_SECRET_KEY` is in the Render environment variables (not in the repo).

**"OPENROUTER_API_KEY is not set"**
- Add your OpenRouter key to Render env vars.

**Static files not loading (CSS/JS broken)**
- WhiteNoise should handle this automatically. If not, run:
  ```powershell
  python manage.py collectstatic --noinput
  ```
  locally, commit, and push.

**"Module not found" errors during build**
- Make sure `requirements.txt` is at the root of the repo and contains all imports.

---

## After Deployment

Reply with your live Task 1 and Task 2 URLs, and I'll update the README files with the real links.
