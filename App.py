import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the saved model and tokenizer
model = load_model('cnn_lstm_toxic_comment_model.h5')  # Path to your saved model
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

# Set the maximum length of input sequences and maximum words for tokenization
MAX_LENGTH = 150
MAX_WORDS = 5000

# Function to clean the input text
def clean_text(text):
    import re
    text = text.lower()
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "cannot ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub('\W', ' ', text)
    text = re.sub('\s+', ' ', text).strip()
    return text

# Streamlit App Layout
st.title("Toxic Comment Classifier")

# User input text box
user_input = st.text_area("Enter a comment to classify as Toxic or Not Toxic:")

if user_input:
    # Clean the input text
    cleaned_text = clean_text(user_input)

    # Tokenize and pad the input text
    seq = tokenizer.texts_to_sequences([cleaned_text])
    padded_seq = pad_sequences(seq, maxlen=MAX_LENGTH)

    # Predict using the trained model
    prediction = model.predict(padded_seq)
    prediction_label = "Toxic" if prediction > 0.5 else "Not Toxic"
    confidence_score = prediction[0][0] * 100

    # Display the result
    st.write(f"The entered comment is labelled as {prediction_label}")
    st.write(f"Toxicity Score is {confidence_score:.2f}%")


