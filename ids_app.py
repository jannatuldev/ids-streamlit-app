import streamlit as st
import pandas as pd
import joblib
import numpy as np
import pickle

st.set_page_config(page_title="Sharingan Network IDS", layout="wide", initial_sidebar_state="expanded")

# Custom CSS (unchanged)
st.markdown("""
    <style>
        .stApp { background-color: #0E1117; color: white; }
        .main-title { font-size: 42px; font-weight: 800; color: #22C55E; margin-bottom: 10px; }
        section[data-testid="stSidebar"] { background-color: #111827; border-right: 1px solid #1F2933; }
        .stButton button { background-color: #22C55E; color: black; font-weight: 600; border-radius: 6px; border: none; padding: 10px 24px; }
        .stButton button:hover { background-color: #16A34A; color: white; }
        .stDataFrame { background-color: #111827; }
    </style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_artifacts():
    scaler = joblib.load("scaler.pkl")
    model = joblib.load("rf_model.pkl")          # or "xgb_model.pkl"
    with open("label_encoder.pkl", "rb") as f:
        le = pickle.load(f)
    with open("feature_columns.pkl", "rb") as f:
        feature_columns = pickle.load(f)
    return scaler, model, le, feature_columns

scaler, model, le, feature_columns = load_artifacts()

st.sidebar.title("Sharingan Network IDS")
st.sidebar.write("Intrusion Detection System")
st.sidebar.write("---")
st.sidebar.write("Upload network traffic data")
st.sidebar.write("Run detection using trained model")
st.sidebar.write("---")
st.sidebar.write("Project Type: Machine Learning Based IDS")

st.markdown('<div class="main-title">Sharingan Network IDS</div>', unsafe_allow_html=True)
st.write("This system analyzes network traffic features and predicts whether the activity is benign or malicious using a trained classification model.")
st.write("---")

uploaded_file = st.file_uploader("Upload Network Traffic CSV File", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded df shape:", df.shape)

        # Verify columns match exactly
        if list(df.columns) != feature_columns:
            st.error("Uploaded file columns do not match the expected feature columns.")
            st.stop()

        st.subheader("Dataset Preview")
        st.dataframe(df.head())

        if st.button("Run Detection"):
            # Scale features (2D input for sklearn)
            X_scaled = scaler.transform(df)

            # Predict
            y_pred = model.predict(X_scaled)

            # Convert to original attack names
            predicted_labels = le.inverse_transform(y_pred)

            # Count results
            unique, counts = np.unique(predicted_labels, return_counts=True)
            results = pd.DataFrame({"Attack Type": unique, "Count": counts})
            st.subheader("Detection Results")
            st.dataframe(results)

            # Optional: show first 10 predictions
            with st.expander("Show first 10 predictions"):
                sample_df = pd.DataFrame({"Predicted Label": predicted_labels[:10]})
                st.dataframe(sample_df)

    except Exception as e:
        st.error(f"Processing Error: {e}")