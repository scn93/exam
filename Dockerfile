# Utiliser une image Python comme base
FROM python:3.9-buster


# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python
RUN python -m pip install --upgrade pip

# Copier tout le code de l'application dans le conteneur
COPY . .

# Exposer le port 5000
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]

