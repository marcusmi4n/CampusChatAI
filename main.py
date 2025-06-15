from fastapi import FastAPI
from models import ChatRequest
from supabase_client import save_message
from router_openai import ask_openrouter

app = FastAPI(title="CampusChat AI")

@app.post("/chat")
def chat(req: ChatRequest):
    ai_response = ask_openrouter(req.message)
    save_message(req.user, req.message, ai_response)
    return {"reply": ai_response}
