# Cosa Nostraa Dashboard

Flask inventory & sales dashboard.

## Deploy on Render (free)

1. Upload all files to a GitHub repo (app.py, requirements.txt, Procfile, runtime.txt, render.yaml, .gitignore).
2. Render.com -> New + -> Web Service -> connect the repo.
3. Render auto-reads render.yaml. If filling manually:
   - Runtime: Python 3
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120`
   - Plan: Free
4. Create Web Service. Wait for "Live".

IMPORTANT: keep `--workers 1` (free tier 512MB; more workers = out of memory).

## Logins
- Admin: Mayuresh / Cosanostraa@123
- Employee: cosanostraa2026 / cn2026
