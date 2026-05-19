

import os
import requests
from dotenv import load_dotenv

# 1. Load the variables from your .env file
load_dotenv()

# 2. Define the api_key variable by fetching it from the environment
api_key = os.getenv("OPENROUTER_API_KEY")

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

query = input("enter your question: ")
data = {
    "model": "openai/gpt-4o-mini",
    "max_tokens": 200,
    "messages": [
        {"role": "user", "content": query}
    ]
}

response = requests.post(url, headers=headers, json=data)
result = response.json()
answer = result['choices'][0]['message']['content']
print("\nAI Response:")
print(answer)

