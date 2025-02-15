# app.py
import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def initialize_session_state():
    """Initialize session state variables"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []

def get_groq_response(messages):
    """Get response from Groq API"""
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=True,
            stop=None
        )
        
        # Initialize response string
        response_string = ""
        
        # Create a placeholder for streaming response
        message_placeholder = st.empty()
        
        # Stream the response
        for chunk in completion:
            content = chunk.choices[0].delta.content or ""
            response_string += content
            message_placeholder.markdown(response_string + "▌")
        
        # Replace placeholder with final response
        message_placeholder.markdown(response_string)
        
        return response_string
    
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

def main():
    # Set page config
    st.set_page_config(
        page_title="Groq Chatbot",
        page_icon="🤖",
        layout="centered"
    )
    
    # Initialize session state
    initialize_session_state()
    
    # Custom CSS for chat interface
    st.markdown("""
        <style>
        .stTextInput {
            position: fixed;
            bottom: 20px;
            width: calc(100% - 4rem);
        }
        .main {
            margin-bottom: 80px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.title("💬Chatbot")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("What's on your mind?"):
        # Add user message to chat
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Get bot response
        messages = [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ]
        
        with st.chat_message("assistant"):
            response = get_groq_response(messages)
            if response:
                st.session_state.messages.append({"role": "assistant", "content": response})
                
                # Update conversation history with timestamp
                st.session_state.conversation_history.append({
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "user": prompt,
                    "assistant": response
                })

if __name__ == "__main__":
    main()
