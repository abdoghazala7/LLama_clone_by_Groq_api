import os
import asyncio
from groq import AsyncGroq
from dotenv import load_dotenv, find_dotenv

env_path = os.path.join("..", '.env_config')
load_dotenv(find_dotenv(filename='.env_config'))
client = AsyncGroq(api_key= os.getenv("GROQ_API_KEY"))

async def main():

    stream = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Can you generate an example json object describing a fruit?",
            }
        ],
        model="llama-3.3-70b-versatile",
        stream=True,
    )

    # Print the incremental deltas returned by the LLM.
    async for chunk in stream:
        print(chunk.choices[0].delta.content, end="")  
 
asyncio.run(main())
