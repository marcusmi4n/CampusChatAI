from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

def save_message(user: str, message: str, response: str):
    data = {
        "user": user,
        "message": message,
        "response": response
    }
    supabase.table("messages").insert(data).execute()
