import os
import requests
from dotenv import load_dotenv

load_dotenv()

def ask_openrouter(prompt: str):
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "deepseek/deepseek-r1-0528:free",  # or "mistralai/mistral-7b"
        "messages": [{"role": "user", "content": prompt}]
    }
    res = requests.post("https://openrouter.ai/api/v1/chat/completions", json=body, headers=headers)
    try:
        return res.json()['choices'][0]['message']['content']
    except:
        return "Sorry, I couldn't get a response."
