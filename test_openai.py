import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file
load_dotenv()

# Read API Key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Test API
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": "Hello! Please introduce yourself in one sentence."
        }
    ]
)

print(response.choices[0].message.content)