import os
from groq import Groq
from dotenv import load_dotenv, find_dotenv

env_path = os.path.join("..", '.env_config')
load_dotenv(find_dotenv(filename='.env_config'))

client = Groq(
    api_key= os.getenv("GROQ_API_KEY"),
)

completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Can you generate an example json object describing a fruit?",
        }
    ],
    model="llama-3.3-70b-versatile",
    response_format={"type": "json_object"},
)


print('\n**Message Response Content**:\n', completion.choices[0].message.content)