import streamlit as st
import google.generativeai as genai
import os
import nltk
from transformers import pipeline

# Ensure NLTK tokenizer is available
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# Get API key from environment variable
api_key = os.environ.get("My_API_KEY")
if not api_key:
    st.error("API Key not found. Please set the My_API_KEY environment variable.")
else:
    genai.configure(api_key=api_key)

# Initialize sentiment analysis pipeline
try:
    sentiment_pipeline = pipeline("sentiment-analysis")
except Exception as e:
    sentiment_pipeline = None
    st.warning("Sentiment analysis model could not be loaded. Sentiment analysis will be disabled.")

def healthcare_chatbot(user_input):
    try:
        model = genai.GenerativeModel("gemini-pro")
        
        # Pass chat history for better responses
        history_text = "\n".join([f"{turn['role']}: {turn['message']}" for turn in st.session_state.chat_history[-5:]])
        prompt = f"{history_text}\nUser: {user_input}\nAssistant: "
        
        response = model.generate_content(prompt)
        
        if response and hasattr(response, "text"):
            gemini_response = response.text.strip()
            
            # Sentiment Analysis
            if sentiment_pipeline:
                try:
                    sentiment = sentiment_pipeline(user_input)[0]
                    gemini_response += f"\n\n(Sentiment: {sentiment['label']} - {sentiment['score']:.2f})"
                except Exception as e:
                    st.warning(f"Error performing sentiment analysis: {e}")
            
            return gemini_response
        else:
            return "I couldn't generate a response. Please try again."
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    st.title("🩺 Healthcare Assistant Chatbot")
    
    # Sidebar for Instructions
    with st.sidebar:
        st.header("Instructions")
        st.write("✔ Ask health-related questions.")
        st.write("✔ Chat history improves response quality.")
        st.write("✔ Sentiment analysis detects emotions.")
    
    # Display Chat History
    with st.expander("📜 Chat History"):
        for turn in st.session_state.chat_history:
            role = "👤 User" if turn['role'] == "User" else "🤖 Assistant"
            st.markdown(f"**{role}:** {turn['message']}")
    
    # Input Field
    user_input = st.text_area("Enter your message", height=100, placeholder="Type your health-related question here...")
    
    # Predefined Example Questions
    example_questions = ["What are the symptoms of COVID-19?", "How to reduce stress?", "What is the best diet for heart health?"]
    st.write("Try asking:")
    for question in example_questions:
        if st.button(question):
            user_input = question
    
    if st.button("Submit") and user_input.strip():
        with st.spinner("Processing..."):
            response = healthcare_chatbot(user_input)
            
            # Update session chat history
            st.session_state.chat_history.append({"role": "User", "message": user_input})
            st.session_state.chat_history.append({"role": "Assistant", "message": response})
            
            # Display User & Assistant Messages
            st.markdown(f"**👤 User:** {user_input}")
            st.markdown(f"**🤖 Healthcare Assistant:** {response}")

if __name__ == "__main__":
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    main()
