import streamlit as st
import pandas as pd
import joblib

# ----------------------------------
# 1. Page Configuration
# ----------------------------------
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

# ----------------------------------
# 2. Load Saved Model and Files
# ----------------------------------
@st.cache_resource
def load_files():
    model = joblib.load("Logistic_heart.pkl")
    scaler = joblib.load("scaler.pkl")
    expected_columns = joblib.load("columns.pkl")
    return model, scaler, expected_columns


try:
    model, scaler, expected_columns = load_files()
except Exception as e:
    st.error(f"Unable to load model files: {e}")
    st.stop()


# ----------------------------------
# 3. Application Title
# ----------------------------------
st.title("❤️ Heart Disease Prediction")
st.subheader("Developed by Subhadeep")
st.write(
    "Enter the details below to obtain a prediction from the trained "
    "machine learning model."
)


# ----------------------------------
# 4. User Inputs
# ----------------------------------
st.header("Patient Information")

age = st.slider(
    "Age",
    min_value=18,
    max_value=100,
    value=40
)

sex = st.selectbox(
    "Sex",
    ["M", "F"]
)

chest_pain = st.selectbox(
    "Chest Pain Type",
    ["ATA", "NAP", "TA", "ASY"]
)

resting_BP = st.number_input(
    "Resting Blood Pressure (mm Hg)",
    min_value=80,
    max_value=200,
    value=120
)

cholesterol = st.number_input(
    "Cholesterol (mg/dL)",
    min_value=100,
    max_value=600,
    value=200
)

fasting_BS = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dL",
    [0, 1],
    format_func=lambda x: "Yes (1)" if x == 1 else "No (0)"
)

resting_ecg = st.selectbox(
    "Resting ECG",
    ["Normal", "ST", "LVH"]
)

max_hr = st.slider(
    "Maximum Heart Rate",
    min_value=60,
    max_value=220,
    value=150
)

exercise_angina = st.selectbox(
    "Exercise-Induced Angina",
    ["Y", "N"]
)

oldpeak = st.slider(
    "Oldpeak (ST Depression)",
    min_value=0.0,
    max_value=6.0,
    value=1.0,
    step=0.1
)

st_slope = st.selectbox(
    "ST Slope",
    ["Up", "Flat", "Down"]
)


# ----------------------------------
# 5. Prediction Function
# ----------------------------------
if st.button("Predict", type="primary", use_container_width=True):

    try:
        # Numerical features
        raw_input = {
            "Age": age,
            "RestingBP": resting_BP,
            "Cholesterol": cholesterol,
            "FastingBS": fasting_BS,
            "MaxHR": max_hr,
            "Oldpeak": oldpeak
        }

        # Categorical features
        categorical_features = {
            "Sex": sex,
            "ChestPainType": chest_pain,
            "RestingECG": resting_ecg,
            "ExerciseAngina": exercise_angina,
            "ST_Slope": st_slope
        }

        # Apply one-hot encoding using the saved model columns
        for feature, value in categorical_features.items():

            column_name = f"{feature}_{value}"

            if column_name in expected_columns:
                raw_input[column_name] = 1

        # Create a DataFrame
        input_df = pd.DataFrame([raw_input])

        # Add missing columns
        for col in expected_columns:
            if col not in input_df.columns:
                input_df[col] = 0

        # Remove unexpected columns and preserve feature order
        input_df = input_df.reindex(
            columns=expected_columns,
            fill_value=0
        )

        # ----------------------------------
        # 6. Scale Input Features
        # ----------------------------------
        scaled_input = scaler.transform(input_df)

        # ----------------------------------
        # 7. Make Prediction
        # ----------------------------------
        prediction = model.predict(scaled_input)[0]

        st.divider()
        st.header("Prediction Result")

        # Display predicted probabilities when available
        if hasattr(model, "predict_proba"):

            probabilities = model.predict_proba(scaled_input)[0]
            classes = list(model.classes_)

            probability_df = pd.DataFrame({
                "Class": classes,
                "Model Probability": [
                    f"{p:.2%}" for p in probabilities
                ]
            })

            st.write("Model prediction probabilities:")
            st.dataframe(
                probability_df,
                hide_index=True,
                use_container_width=True
            )

        # ----------------------------------
        # 8. Display Result
        # ----------------------------------
        if prediction == 1:

            st.error(
                "⚠️ The model predicts a higher likelihood "
                "of heart disease."
            )

        else:

            st.success(
                "✅ The model predicts a lower likelihood "
                "of heart disease."
            )

        st.caption(
            "This application is an educational machine learning project. "
            "Its predictions are not a medical diagnosis or a substitute "
            "for professional medical evaluation."
        )

    except Exception as e:

        st.error(f"Prediction failed: {e}")

        st.info(
            "Check whether the saved model, scaler, feature columns, "
            "and input encoding match the original training pipeline."
        )
