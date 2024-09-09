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

with open('C:/Users/HP/OneDrive/Desktop/jupyter Projects/label_encoder.pkl', 'rb') as f:
    lb = pickle.load(f)

with open('C:/Users/HP/OneDrive/Desktop/jupyter Projects/tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

#==================custom function================
stopwords = set(nltk.corpus.stopwords.words('english'))

def clean_text(text):
    stemmer = PorterStemmer()
    text = re.sub("[^a-zA-Z]", " ", text)  # Replace non-alphabet characters with space
    text = text.lower()  # Convert text to lowercase
    text = text.split()  # Split text into words
    text = [stemmer.stem(word) for word in text if word not in stopwords]  # Stem words and remove stopwords
    return " ".join(text)

def predict_emotion(input_text):
    cleaned_text = clean_text(input_text)
    input_vectorized = tfidf_vectorizer.transform([cleaned_text])

    # Predict emotion
    predicted_label = model.predict(input_vectorized)[0]  # Get predicted label
    predicted_emotion = lb.inverse_transform([predicted_label])[0]  # Convert label to emotion name

    return predicted_emotion, predicted_label  # Return both emotion and label


# Main function for emotion detection
def main():
    st.title("Six NLP Emotions Detection App")
    st.write(['Joy', 'Fear', 'Love', 'Anger', 'Sadness', 'Surprise'])

    # Input text
    input_text = st.text_input("Paste your text here")

    # Button to trigger prediction
    if st.button("Predict"):
        predicted_emotion, predicted_label = predict_emotion(input_text)  # Call the function to get prediction
        st.write("Predicted Emotion:", predicted_emotion)
        st.write("Predicted Label:", predicted_label)


# Ensure main() is called when this script is run
if __name__ == '__main__':
    main()
