# Presentation Layer

The `presentation_app.py` Streamlit app walks stakeholders through the pipeline:

1. **Model selection** – choose between the linear regression and Random Forest artifacts saved under `models/`.
2. **Scenario builder** – adjust engineered predictor values and observe the predicted MPG in real time.
3. **Diagnostics gallery** – view the residuals plot and prediction vs actual snapshots created in earlier sprints.
4. **Narrative recap** – the app repeats the highlights from the Markdown presentation and connects them back to the repo story.

Run the app with `streamlit run presentation_app.py` after installing `requirements.txt` (or use a virtual env). This gives anyone a quick UI to explore the ingestion → features → modeling story without opening code or notebooks.