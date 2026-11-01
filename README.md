# ❤️ Heart Disease Prediction Using Machine Learning

My first Machine Learning model! 🎉

I am excited to share my first machine learning project, **Heart Disease Prediction**, built using Python and Streamlit. As a beginner in Machine Learning, this project is an important step in my journey toward becoming a Data Scientist.

The project uses a trained Logistic Regression model to predict the risk of heart disease based on user-provided health parameters. I developed a simple, interactive web application where users can enter their health information and receive a model-generated prediction.

## 🚀 Project Overview

The application collects different health-related parameters, processes the input data, scales the features, and passes them to a trained machine learning model to generate a prediction.

This project helped me understand how to integrate a machine learning model into a web application and make it interactive using Streamlit.

## 🛠️ Technologies Used

- **Python** – Programming language
- **Pandas** – Data manipulation and preprocessing
- **Streamlit** – Interactive web application
- **Scikit-learn** – Machine learning model and feature scaling
- **Joblib** – Loading saved machine learning models

## 📊 Features

- ❤️ User-friendly interface
- 👤 Age and sex selection
- 🩺 Chest pain type selection
- 🩸 Blood pressure and cholesterol inputs
- 💓 Maximum heart rate input
- 📈 Resting ECG and ST slope selection
- ⚙️ Automatic feature alignment with the model's expected input columns
- 🤖 Logistic Regression-based prediction
- ✅ Interactive prediction results

## 🧠 Machine Learning Model

**Algorithm:** Logistic Regression

The application uses three saved files:

- `Logistic_heart.pkl` – Trained Logistic Regression model
- `scaler.pkl` – Saved feature scaler
- `columns.pkl` – Expected model input columns

The application aligns the input features with the expected columns, applies the saved scaler, and generates a prediction using the trained model.

## 📂 Project Structure

```text
Heart-Disease-Prediction/
│
├── app.py
├── Logistic_heart.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
└── README.md
```

*Note: The structure above is a suggested repository layout. Add `requirements.txt` and the other files if they are not already present in your project.*

## ⚙️ How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd Heart-Disease-Prediction
```

### 3. Install the required libraries

```bash
pip install streamlit pandas scikit-learn joblib
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🎯 What I Learned

While building my first machine learning model, I learned about:

- Integrating a trained ML model with a web application.
- Using Logistic Regression for classification.
- Understanding feature scaling and preprocessing.
- Handling categorical variables and one-hot encoded features.
- Loading saved models using Joblib.
- Building an interactive application with Streamlit.
- Connecting Python, Pandas, and Scikit-learn in a practical project.

## 🔮 Future Improvements

I plan to improve this project by:

- Comparing Logistic Regression with other classification algorithms.
- Evaluating model performance using accuracy, precision, recall, F1-score, and a confusion matrix.
- Improving the user interface.
- Adding model performance visualizations.
- Deploying the application online.
- Improving input validation and prediction reliability.

## ⚠️ Disclaimer

This project is developed for educational purposes only. Its predictions are not a medical diagnosis and must not be used to make healthcare decisions. Always consult a qualified healthcare professional for medical advice.

## 👨‍💻 About Me

I am a BCA student at The Neotia University, learning Python, Data Analytics, and Machine Learning while building practical projects.

This is my **first machine learning model**, and I am excited to continue learning, experimenting, and developing more projects in Data Science.

Thank you for visiting my repository! ⭐

If you find this project interesting, feel free to explore the code and share your feedback.
