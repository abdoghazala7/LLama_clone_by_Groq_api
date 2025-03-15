import os
from groq import Groq
from dotenv import load_dotenv, find_dotenv

env_path = os.path.join("..", '.env_config')
load_dotenv(find_dotenv(filename='.env_config'))
client = Groq(api_key= os.getenv("GROQ_API_KEY"))


def chat_with_llama_stream(prompt, model="llama-3.3-70b-versatile", temperature=0.7):

    try:
        # Create a chat completion using the Groq client
        stream = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
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
        print("llama: ", end="")
        for chunk in stream:
            #print(chunk or "", end="")
            print(chunk.choices[0].delta.content or "", end="")
        print()


if __name__ == "__main__":
    main()