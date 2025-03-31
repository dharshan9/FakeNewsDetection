📰 Fake News Detection Using Machine Learning
📌 Project Overview
In an era where misinformation spreads rapidly, detecting fake news is crucial for maintaining trust in media. This project leverages Natural Language Processing (NLP) and Machine Learning (ML) techniques to analyze and classify news articles as Fake or Real. The analysis helps in combating misinformation by providing an automated tool for verifying news authenticity.

This repository contains a fully implemented and deployed AI model capable of classifying news articles based on textual content.

🎯 Key Features
✔ Text Preprocessing: Tokenization, stopword removal, and lemmatization to clean text data.
✔ Feature Extraction: TF-IDF (Term Frequency-Inverse Document Frequency) vectorization for numerical representation.
✔ Machine Learning Model: Trained using Multinomial Naïve Bayes, optimized for accuracy and efficiency.
✔ Statistical Analysis: Evaluating model performance using precision, recall, F1-score, and confusion matrices.
✔ Deployment: Fully functional Flask API, hosted on Render for real-time news classification.

📊 Scope of the Project
1️⃣ Data Processing & Preparation
Merging real and fake news datasets.

Cleaning and preprocessing text data.

Encoding labels for model training.

2️⃣ Exploratory Data Analysis (EDA)
Understanding the distribution of fake vs. real news.

Visualizing word frequency and common terms using Seaborn and Matplotlib.

3️⃣ Feature Engineering & Model Training
Applying TF-IDF vectorization to extract meaningful textual features.

Training a Multinomial Naïve Bayes model for classification.

4️⃣ Model Evaluation
Computing accuracy, precision, recall, and F1-score.

Validating model effectiveness using confusion matrices.

5️⃣ Deployment & API Integration
Implementing a Flask API to accept news articles as input and return predictions.

Hosted on Render, making it accessible via a public endpoint.

🛠️ Technologies Used
✅ Programming Language: Python 🐍
✅ Libraries:

pandas, numpy – Data Processing

nltk – Natural Language Processing

scikit-learn – Machine Learning Model

matplotlib, seaborn – Data Visualization
✅ Model: TF-IDF + Multinomial Naïve Bayes
✅ Deployment: Flask API
