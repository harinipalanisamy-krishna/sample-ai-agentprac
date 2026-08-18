# Study Coach (sample-ai-agent)

Practice project: a tiny Streamlit app that sends a study-session description
to Gemini and prints back coaching feedback. Used to rehearse the full
GitHub → Streamlit Cloud deploy flow before the real build sprint.

## Files
- `app.py` — the actual app
- `requirements.txt` — dependencies Streamlit Cloud will install
- `.gitignore` — keeps your real API key out of git
- `.streamlit/secrets.toml.example` — shows the format for your key; copy it to
  `.streamlit/secrets.toml` locally and fill in your real key (that real file
  is git-ignored, never committed)

## Run locally
1. `pip install -r requirements.txt`
2. Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and paste your real Gemini key in
3. `streamlit run app.py`

## Deploy
1. `git init`
2. `git add .`
3. `git commit -m "initial commit"`
4. Create a new repo on GitHub, then:
   - `git remote add origin <your-repo-url>`
   - `git branch -M main`
   - `git push -u origin main`
5. Go to https://share.streamlit.io, sign in with GitHub, click "Create app"
6. Pick this repo, branch `main`, main file `app.py`
7. In Advanced settings (or Settings > Secrets after deploy), add:
   ```
   GEMINI_API_KEY = "your-real-key"
   ```
8. Deploy, then open the live URL in a private/incognito window to confirm it works
