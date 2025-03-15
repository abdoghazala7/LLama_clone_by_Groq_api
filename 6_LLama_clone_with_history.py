import os
from groq import Groq
from dotenv import load_dotenv, find_dotenv

env_path = os.path.join("..", '.env_config')
load_dotenv(find_dotenv(filename='.env_config'))
client = Groq(api_key= os.getenv("GROQ_API_KEY"))

# Global variable to store conversation history
conversation_history = []

def chat_with_llama_stream(prompt, model="llama-3.3-70b-versatile", temperature=0.7):

    try:
        # Add the new user message to the conversation history
        conversation_history.append({"role": "user", "content": prompt})

        # Limit the history length based on the environment variable
        max_history = int(os.getenv("MAX_HISTORY_LENGTH", 5))
        messages_to_send = conversation_history[-max_history:]

        # Create a chat completion using the Groq client
        stream = client.chat.completions.create(
            messages=messages_to_send,
            model=model,
            temperature=temperature,
            stream=True,
        )
        # Extract and return the response content
        return stream
    
    except Exception as e:
        # Return the error message if an exception occurs
        return str(e)
    
def main():
    print("Welcome to LLama Clone!")
    model_name = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")
    temperature = float(os.getenv("TEMPERATURE", 0.7))
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting LLama Clone. Goodbye!")
            break

        stream = chat_with_llama_stream(user_input, model=model_name, temperature=temperature)

        if isinstance(stream, str):
            print(f"Error: {stream}")
            continue

        full_response = ""
        print("LLama: ", end="")
        for chunk in stream:
            response_content = chunk.choices[0].delta.content or ""
            full_response += response_content
            print(response_content, end="")
        
        # Add the complete system response to the conversation history
        conversation_history.append({"role": "system", "content": full_response})
        print()
        print()


if __name__ == "__main__":
    main()