import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "It seems like you're experiencing symptoms. Please consult Doctor for accurate advice"
    elif "appointment" in user_input:
        return "Would you like me to schedule appointment with the Doctor?"
    elif "medication" in user_input:
        return "it's important to take prescribed medicatations regularly.If you have concerns, consults your Doctor. "
    else: response = chatbot(user_input,max_length=500,num_return_sequences=1)
    
    return response[0]['generated_text']


def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?")
    if st.button("Submit"):
        st.write("User : ", user_input)
        with st.spinner("Processing your query, Please wait......"):
            response = healthcare_chatbot(user_input)
        st.write("Healthcare Assistant : ",response)
    else:
        st.warning("Please enter a message to get a response")


main()