import os

# Vérifiez si la variable est accessible
api_key = os.getenv("GROQ_API_KEY")
if api_key:
    print("Variable GROQ_API_KEY est définie :", api_key)
else:
    print("Variable GROQ_API_KEY n'est pas définie.")

# Votre code Groq ici
from groq import Groq

client = Groq(
    api_key=api_key,
)
