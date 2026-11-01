# ❤️ Heart Disease Prediction Using Machine Learning

### My First Machine Learning Model! 🎉

I am excited to share my first Machine Learning project, **Heart Disease Prediction**, built using Python and Streamlit. As a beginner in Machine Learning, this project is an important milestone in my journey toward becoming a Data Scientist.

This project uses a trained **Logistic Regression model** to predict the risk of heart disease based on user-provided health parameters. I developed an interactive web application where users can enter their health information and receive a model-generated prediction.

## 🚀 Project Overview

The application collects health-related parameters, processes the input data, scales the features, and passes them to a trained machine learning model to generate a prediction.

This project helped me understand how to integrate a machine learning model into a web application using Streamlit.

## 🛠️ Technologies Used

- **Python** – Programming language
- **Pandas** – Data manipulation and preprocessing
- **Streamlit** – Interactive web application
- **Scikit-learn** – Machine learning model and feature scaling
- **Joblib** – Saving and loading machine learning models

## 📊 Features

- ❤️ User-friendly interface
- 👤 Age and sex selection
- 🩺 Chest pain type selection
- 🩸 Blood pressure and cholesterol inputs
- 💓 Maximum heart rate input
- 📈 Resting ECG and ST slope selection
- ⚙️ Feature alignment with the model's expected input columns
- 🤖 Logistic Regression-based predictions
- ✅ Interactive prediction results

## 🧠 Machine Learning Model

**Algorithm:** Logistic Regression

The application uses three saved files:

- `Logistic_heart.pkl` – Trained Logistic Regression model
- `scaler.pkl` – Saved feature scaler
- `columns.pkl` – Expected model input columns

The application aligns the input features with the expected columns, applies the saved scaler, and generates a prediction.

## 📈 Model Performance

The Logistic Regression model achieved the following evaluation results:

| Evaluation Metric | Score |
|---|---:|
| Accuracy | **86.96%** |
| F1-Score | **88.46%** |

These metrics provide an initial evaluation of the model's classification performance. Actual performance may vary depending on the evaluation dataset and how well the model generalizes to new data.

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

*Note: This is the suggested repository structure. Ensure the listed files are included in your repository.*

## ⚙️ How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

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

- Building a classification model using Logistic Regression.
- Understanding feature scaling and data preprocessing.
- Handling categorical variables and one-hot encoded features.
- Loading saved models using Joblib.
- Integrating Scikit-learn with Streamlit.
- Creating an interactive machine learning web application.
- Evaluating model performance using accuracy and F1-score.

## 🔮 Future Improvements

I plan to improve this project by:

- Comparing Logistic Regression with other classification algorithms.
- Evaluating precision, recall, and the confusion matrix.
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
