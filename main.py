import os
import groq
from groq import Groq
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env (optionnel)
load_dotenv()

app = FastAPI()

# Vérifier si l'API Key est définie dans les variables d'environnement
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("La clé API GROQ_API_KEY n'est pas définie. Vérifiez vos variables d'environnement.")

# Configure the default client for all requests
client = Groq(
    api_key=api_key,
    timeout=20.0,  # Temps d'attente par défaut : 20 secondes
    max_retries=1  # Nombre maximum de tentatives
)

class Prompt(BaseModel):
    prompt: str

@app.get("/status")
async def get_status():
    return {"message": "OK"}

@app.post("/chat")
async def post_chat(prompt: Prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": prompt.prompt,
                },
            ],
            model="mixtral-8x7b-32768",  # Spécifiez le modèle souhaité
        )
        return {"response": chat_completion.choices[0].message.content}

    except groq.APIConnectionError as e:
        print("The server could not be reached")
        print(e.__cause__)  # Cause sous-jacente, probablement levée dans httpx.
        raise HTTPException(status_code=500, detail="API Connection Error")

    except groq.RateLimitError as e:
        print("A 429 status code was received; we should back off a bit.")
        raise HTTPException(status_code=429, detail="Rate Limit Exceeded")

    except groq.APIStatusError as e:
        print("Another non-200-range status code was received")
        print(e.status_code)
        print(e.response)
        raise HTTPException(status_code=e.status_code, detail="API Status Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)

