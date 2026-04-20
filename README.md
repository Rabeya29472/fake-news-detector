Title:  Fake News Detection Using deep learning
This is a  machine learning web application that classifies news articles as real or fake using Natural Language Processing (NLP), neural network and Logistic Regression. The model is deployed using Streamlit .
Live Demo line: https://fake-news-detector-jhgsvybue3bxygtwbzp8mp.streamlit.app/
##Project Overview:
 
This project uses a supervised machine learning approach to detect fake news based on textual content. It combines data preprocessing, feature extraction using TF-IDF, and classification using Logistic Regression and neural network.

Model Details: 
Algorithm: Neural Network,Logistic Regression,
  Feature Extraction: TF-IDF Vectorizer (unigrams + bigrams)
  Text Processing: Lowercasing, punctuation removal, stopword filtering
  Framework: Scikit-learn
Dataset:

The dataset contains news articles labeled as:Fake News and Real News . I labelled it as 0 and 1 later on for the model to learn the pattern properly. 

It includes the following features:Title,Text,Subject,Date,label

Tech Stack: Python,Pandas, NumPy,Scikit-learn,Streamlit,Joblib

