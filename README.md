# AI Chat Application with Streamlit and Groq API

This project is a Streamlit-based web application that allows users to interact with an AI model powered by the **Groq API**. The application supports multiple AI models, chat history, user feedback, and streaming responses for a seamless conversational experience.

---

## Features

- **Multiple AI Models**: Choose from a variety of AI models (e.g., LLama, Gemma, Mixtral) for different use cases.
- **Streaming Responses**: Real-time streaming of AI-generated responses for a smooth user experience.
- **Chat History**: Maintains a conversation history with adjustable length.
- **User Feedback**: Collects user feedback (thumbs up/down) to improve the AI's performance.
- **Customizable Settings**: Adjust temperature and max history length for tailored interactions.
- **Asynchronous Support**: Includes async implementations for efficient API calls.

---

## File Structure

Here’s an overview of the project's file structure:

- **.streamlit/** # Folder containing secrets app file.
- **venv/** # Virtual environment for dependencies.
- **.env_config** # Environment configuration file.
- **1_Groq_api.py** # Main Groq API implementation.
- **2_1_groq_api_dotenv.py** # Groq API with .env configuration.
- **2_2_groq_api_dotenv_with.json** # Groq API with .env and JSON configuration.
- **3_async_groq_api.py** # Asynchronous Groq API implementation.
- **4_async_groq_stream.py** # Async streaming with Groq API.
- **5_Llama_clone.py** # Basic LLaMA model implementation.
- **6_Llama_clone_with_history.py** # LLaMA model with chat history.
- **7_streamlit_llama_clone_userfeedback.py** # Streamlit app with user feedback.
- **requirements.txt** # List of dependencies.

---

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/abdoghazala7/AI_Chat_With_Groq_API_Models.git
   cd AI_Chat_With_Groq_API_Models

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Set up environment variables**:
   ```bash
   Create a .env file in the root directory.
   Add your Groq API key:
   GROQ_API_KEY=your_api_key_here

5. **Run the Streamlit app**:
   ```bash
   7_streamlit_llama_clone_userfeedback.py

## Usage
- Choose a Model: Select an AI model from the sidebar.

- Adjust Settings: Set the temperature and max history length for the conversation.

- Start Chatting: Enter your message in the chat input box and interact with the AI.

- Provide Feedback: Use the thumbs-up/thumbs-down buttons to rate the AI's responses.   
   
## Technologies Used

- **Python**: The primary programming language.
- **Streamlit**: For building the web interface.
- **Groq API**: For interacting with AI models.
- **Asyncio**: For asynchronous API calls and streaming.
- **Dotenv**: For managing environment variables.
