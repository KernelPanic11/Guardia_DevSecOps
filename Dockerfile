FROM python:3.13.7-alpine

# RUN adduser --disabled-password --gecos "" dailycatfacts_user
# USER dailycatfacts_user

WORKDIR /mon_site

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "app/main.py"]


















# TP Guardia : 
# # Choisir une image Python
# FROM python:3.11-slim

# # Définir le dossier de travail dans le container
# WORKDIR /app

# # Copier les fichiers requirements
# COPY requirements.txt .

# # Installer les dépendances
# RUN pip install --no-cache-dir -r requirements.txt

# # Copier le reste du code
# COPY . .

# # Exposer le port de Flask
# EXPOSE 5000

# # Commande pour lancer l'application
# CMD ["python", "app.py"]


# Build / Run : 
# docker build -t tamagotchi-api .
# docker run -p 5000:5000 tamagotchi-api

# Volume : 
# docker run -p 5000:5000 -v $(pwd)/data:/app/data tamagotchi-api

