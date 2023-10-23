import streamlit as st
import openai
import langchain
import pandas as pd
import os

# Set up the OpenAI API key
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

st.title("OpenAI GPT-3 Integration with Streamlit")

# Text input for user query
user_input = st.text_input("Ask a question:")

# When the user inputs a question and hits 'Enter', generate a response
if user_input:
    # Use the OpenAI API to get a response
    response = openai.Completion.create(
        engine="davinci",  # You can use other engines too
        prompt=user_input,
        max_tokens=150  # Limit the response to 150 tokens
    )
    
    # Display the model's response
    st.text_area("GPT-3 Response:", value=response.choices[0].text, height=200, max_chars=None)







