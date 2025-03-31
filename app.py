import streamlit as st
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the trained model
with open("fake_news_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Streamlit UI
st.title("Fake News Detection App")
st.write("Enter a news article below to check if it's Fake or Real.")

# Input Text
news_text = st.text_area("Paste the news content here:")

if st.button("Check News"):
    if news_text:
        # Preprocess input text
        news_tfidf = news_text  # Assuming model can handle raw text
        prediction = model.predict([news_tfidf])
        
        # Display Result
        if prediction[0] == 0:
            st.error("⚠️ This news is Fake!")
        else:
            st.success("✅ This news is Real!")
    else:
        st.warning("Please enter some text to analyze.")