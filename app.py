import streamlit as st
from textblob import TextBlob
from transformers import pipeline

# Title
st.title("Smart Bot: Sentiment Analysis")

# Text Input
st.header("Enter Your Article")
article = st.text_area("Paste your article here...", height=300)

# Analyze Button
if st.button("Analyze"):
    if article:
        # Sentiment Analysis
        blob = TextBlob(article)
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            sentiment_text = "Positive"
        elif sentiment < 0:
            sentiment_text = "Negative"
        else:
            sentiment_text = "Neutral"

        # Display Sentiment
        st.subheader("Sentiment Analysis")
        st.write(f"Sentiment: **{sentiment_text}** (Polarity: {sentiment})")

        # Summarization
        summarizer = pipeline("summarization")
        summary = summarizer(article, max_length=150, min_length=30, do_sample=False)

        # Display Summary
        st.subheader("Article Summary")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter an article!")
