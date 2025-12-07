# Deployment Instructions and Links

This file contains guidance and placeholders for publishing both Task 1 and Task 2 dashboards. Replace the placeholder URLs below with your live deployment links.

## Required links (live dashboards)

- Task 1 Notebook (Binder): https://hub.gesis.mybinder.org/user/manvika1610-fynd-assessment-1a64vda8/doc/tree/task1_rating_prompting.ipynb
- Task 2 Django Dashboard: https://fynd-task2-dashboard.onrender.com/

## Task 1 — Notebook hosting options

Option A: Binder
- Ensure your repository has a `requirements.txt` at the root.
- Visit https://mybinder.org, provide the repository URL and branch.
- Binder will launch a Jupyter session showcasing `task1_rating_prompting.ipynb`.
- Copy the Binder launch URL into the placeholder above.

Option B: Voila (interactive dashboard)
- Use `voila` to render the notebook as an interactive dashboard.
- Deploy to Binder, or a server that can run `voila`.

Option C: NBViewer / GitHub
- Host the notebook on GitHub and link to NBViewer to get a static rendered view.

## Task 2 — Django app deployment options

Option A: Render / Railway / Fly.io / Heroku
- Create a `requirements.txt` (this repo includes one).
- Add a `Procfile` (for Heroku) or follow the host's docs.
- Configure environment variables (set `DJANGO_SECRET_KEY`, `OPENROUTER_API_KEY`, `DJANGO_DEBUG=False`).
- Ensure static files are served (use WhiteNoise or cloud storage as needed).

Sample minimal `Procfile` for Heroku:
```
web: gunicorn fynd_task2.wsgi --log-file -
```

After deployment, copy the public URL into the Task 2 placeholder above.

## Security & Notes
- Do NOT put real secrets in `README.md` or in repo files. Keep them in the host's environment variables or a secure secret manager.
- The app requires `OPENROUTER_API_KEY` to call the LLM. If you want to share a public demo without exposing keys, consider mocking the LLM responses or use a service that supports secure env vars.

---

When you have the live URLs, reply with them and I will update `PROJECT_README.md` and `README.md` with the real deployment links.