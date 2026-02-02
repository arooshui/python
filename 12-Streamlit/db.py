import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load dataset (cached)
@st.cache_data
def load_data():
    df = pd.read_csv("diabetes.csv")
    return df

df = load_data()

# Split features and target
features = ['Pregnancies', 'Glucose', 'BloodPressure', 'Insulin', 'BMI', 'Age']
X = df[features]
y = df["Outcome"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Sidebar inputs
st.sidebar.title("Input Features")

pregnancies = st.sidebar.slider(
    "Pregnancies",
    int(df["Pregnancies"].min()),
    int(df["Pregnancies"].max())
)

glucose = st.sidebar.slider(
    "Glucose",
    int(df["Glucose"].min()),
    int(df["Glucose"].max())
)

blood_pressure = st.sidebar.slider(
    "Blood Pressure",
    int(df["BloodPressure"].min()),
    int(df["BloodPressure"].max())
)

insulin = st.sidebar.slider(
    "Insulin",
    int(df["Insulin"].min()),
    int(df["Insulin"].max())
)

bmi = st.sidebar.slider(
    "BMI",
    float(df["BMI"].min()),
    float(df["BMI"].max())
)

age = st.sidebar.slider(
    "Age",
    int(df["Age"].min()),
    int(df["Age"].max())
)

# Prepare input for prediction
input_data = [[pregnancies, glucose, blood_pressure, insulin, bmi, age]]

# Prediction
prediction = model.predict(input_data)

# Output
st.write("### Prediction Result")
if prediction[0] == 1:
    st.error("Diabetic")
else:
    st.success("Not Diabetic")
