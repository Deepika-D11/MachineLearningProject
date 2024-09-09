#imports====================================
#imports====================================
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import nltk
from nltk.stem import PorterStemmer
import re


# Load Models=================================
# Use pickle.load() to load from files
with open('C:/Users/HP/OneDrive/Desktop/jupyter Projects/logistic_regresion.pkl', 'rb') as f:
    model = pickle.load(f)

with open('label_encoder.pkl', 'rb') as f:
    lb = pickle.load(f)

with open('C:/Users/HP/OneDrive/Desktop/jupyter Projects/tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

#==================custom function================
stopwords = set(nltk.corpus.stopwords.words('english'))
def clean_text(text):
    stemmer = PorterStemmer()
    text = re.sub("[^a-zA-Z]", " ", text)
    text = text.lower()
    text = text.split()
    text = [stemmer.stem(word) for word in text if word not in stopwords]
    return " ".join(text)
def predict_emotion(input_text):
    cleaned_text = clean_text(input_text)
    input_vectorized = tfidf_vectorizer.transform([cleaned_text])

    # Predict emotion
    predicted_label = model.predict(input_vectorized)[0]
    predicted_emotion = lb.inverse_transform([predicted_label])[0]
    label =  np.max(model.predict(input_vectorized))

    return predicted_emotion,label


# app============================================
st.title("SIX NLP EMOTIONS DETECTION APP ")
st.write(['Joy','Fear','Love','Anger', 'sadness','surprise'])
input_text = st.text_input("paste your text here")

if st.button("predict"):
     predict_emotion,lable = predict_emotion(input_text)
     st.write(" Predicted Emotion :",predict_emotion)
     st.write(" Predicted Label :",lable)
