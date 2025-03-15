import os
from groq import Groq
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env_config file in the parent directory
env_path = os.path.join("..", '.env_config')
load_dotenv(find_dotenv(filename='.env_config'))

client = Groq(
    api_key= os.getenv("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Describe the sun in scientific terms",
        }
    ],
    model="llama-3.3-70b-versatile",
)


print('\n**Message Response Content**:\n', chat_completion.choices[0].message.content)