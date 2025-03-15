import os
import asyncio
from groq import AsyncGroq
from dotenv import load_dotenv, find_dotenv

env_path = os.path.join("..", '.env_config')
load_dotenv(find_dotenv(filename='.env_config'))


async def main():
    client = AsyncGroq(api_key= os.getenv("GROQ_API_KEY"))

    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Can you generate an example json object describing a fruit?",
            }
        ],
        model="llama-3.3-70b-versatile",
    )
     
    print(chat_completion.choices[0].message.content)
 
asyncio.run(main())
