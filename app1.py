import streamlit as st
import pickle

# load saved model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

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
