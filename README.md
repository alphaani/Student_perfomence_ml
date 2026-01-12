# Student Performance ML

Small Flask backend + React frontend that predicts a student score using a pre-trained model.

## Run locally

1. Backend (from project root):
   - python -m venv venv
   - .\venv\Scripts\Activate.ps1  (PowerShell)
   - pip install -r requirements.txt
   - python app.py

2. Frontend:
   - cd student-predictor
   - npm install
   - npm start

## Deploy to GitHub & Vercel

1. Create a GitHub repo and push your project (example commands):

```powershell
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo>.git
git push -u origin main
```

2. On Vercel:
   - Connect your GitHub repo to Vercel.
   - Vercel will use `vercel.json` to build the Flask backend (Python) and the React static site.
   - Ensure `requirements.txt` is present (so Python packages install) and `student-predictor/package.json` has the `build` script (it does).

Notes:
- Keep `student_model.pkl` in the repo root so Vercel can bundle it with the backend.
- If the model requires additional Python packages, add them to `requirements.txt`.
