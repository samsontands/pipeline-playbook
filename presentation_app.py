import streamlit as st
import joblib
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

MODEL_DIR = Path("models")
FEATURES_PATH = Path("data/processed/features.csv")
FIGURES_DIR = Path("reports/figures")

@st.cache_data
def load_data():
    return pd.read_csv(FEATURES_PATH)

@st.cache_resource
def load_models():
    models = {}
    for file in MODEL_DIR.glob("*.pkl"):
        models[file.stem] = joblib.load(file)
    return models

st.set_page_config(page_title="Pipeline Playbook", layout="wide")
st.title("Pipeline Playbook Explorer")

models = load_models()
df = load_data()

st.sidebar.header("Pick a model")
model_choice = st.sidebar.selectbox("Model", list(models.keys()))

st.sidebar.markdown("### Input preview")
st.sidebar.dataframe(df.head())

selected_model = models[model_choice]

cols = [c for c in df.columns if c != "mpg"]
input_row = {}
with st.form("predict_form"):
    st.subheader("Scenario Builder")
    for col in cols:
        input_row[col] = st.number_input(col, value=float(df[col].median()))
    submitted = st.form_submit_button("Predict MPG")

if submitted:
    X = pd.DataFrame([input_row])[cols]
    pred = selected_model.predict(X)[0]
    st.metric("Predicted MPG", round(pred, 2))

st.markdown("---")
st.subheader("Diagnostics & Figures")
fig_cols = st.columns(3)
images = {
    "residuals": "residuals.png",
    "linear": "linear_regression-predictions.png",
    "random": "random_forest-predictions.png",
}
for idx, (name, file) in enumerate(images.items()):
    path = FIGURES_DIR / file
    if path.exists():
        fig_cols[idx].image(path, caption=name.replace("_", " "))

st.markdown("---")
st.subheader("Feature Insights")
st.markdown("""
- Residual checks confirm baseline behavior.
- Permutation importance (see repo) highlights weight-related features.
- Presentation narrative ties diagnostics, modeling, and CI notes together.
""")
