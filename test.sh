#!/bin/bash

# Tester l'endpoint /chat avec une requête POST
response=$(curl -s -o /dev/null -w "%{http_code}" -X POST "http://localhost:5000/chat" \
-H "Content-Type: application/json" \
-d '{"prompt": "What is a LLM?"}')

# Vérifier le code de statut de la réponse
if [ $response -eq 200 ]; then
    echo "Test réussi"
else
    echo "Test échoué"
    echo "Code de statut de la réponse: $response"
fi

