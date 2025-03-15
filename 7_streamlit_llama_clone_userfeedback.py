from groq import Groq
import streamlit as st
from streamlit_feedback import streamlit_feedback

# Setting Up st.secrets:
# In your local development environment, you can create a file named secrets.toml in your Streamlit project directory with the following content: toml
# secrets.toml should be in a folder named .streamlit
# GROQ_API_KEY = "your_GROQ_API_KEY_here"

# On Streamlit Cloud, you can use the app settings to securely add your secrets.
# https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-managementAPI_KEY 

# Initialize the GROQ_API client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def stream_chat_response(message, chat_history, model_name, temperature, max_history_length):
    chat_history.append({"role": "user", "content": message})

    if len(chat_history) > max_history_length:
        chat_history = chat_history[-max_history_length:]

    stream = client.chat.completions.create(
        messages=chat_history,
        model=model_name,
        temperature=temperature,
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content

def clear_chat():
    st.session_state.chat_history = []

# Streamlit web interface setup
def main():
    st.title("💬 Chat with AI")

    # Sidebar controls
    model_name = st.sidebar.selectbox("Choose the Model", ["llama-3.3-70b-versatile", "gemma2-9b-it", "mixtral-8x7b-32768", "whisper-large-v3"], index=0)
    temperature = st.sidebar.slider("Set Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.1)
    max_history_length = int(st.sidebar.number_input("Max History Length", min_value=1, max_value=10, value=3))
    if st.sidebar.button("Clear Chat"):
        clear_chat()

    # Session state to store chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    for msg in st.session_state.chat_history:
        st.chat_message(msg["role"]).write(msg["content"])

    user_input = st.chat_input("Enter your message:", key="user_input")
    
    if user_input:
        st.chat_message("user").write(user_input)
        with st.spinner("AI is generating a response..."):
            try:
                accumulated_response = ""
                placeholder = st.chat_message("AI").empty()
                for response_chunk in stream_chat_response(user_input, st.session_state.chat_history, model_name, temperature, max_history_length):
                    accumulated_response += response_chunk
                    placeholder.markdown(accumulated_response)
                st.session_state.chat_history.append({"role": "assistant", "content": accumulated_response})
            except Exception as e:
                st.error(f"An error occurred: {e}")
        
        feedback = streamlit_feedback(
            feedback_type="thumbs",
            optional_text_label="[Optional] Please provide an explanation",
            key=f"feedback_{len(st.session_state.chat_history)}",
        )
        
        if feedback:
            st.write(f"Feedback received: {feedback}")
            # You can log the feedback or send it to a database here

# Running the Streamlit app
if __name__ == "__main__":
    main()