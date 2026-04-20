import streamlit as st


# load saved model and vectorizer
import joblib

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


st.title(" Fake News Detection App")

st.write("Enter a news article below:")

text = st.text_area("News Text")

def clean_text(text):
    text = text.lower()
    text = ''.join([char if char.isalpha() else ' ' for char in text])
    return text

if st.button("Predict"):
    cleaned = clean_text(text)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]

    if prediction == 1:
        st.success("REAL NEWS ")
    else:
        st.error("FAKE NEWS ")
