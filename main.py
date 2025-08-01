from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import random

# Création de l'application FastAPI
app = FastAPI()

# 🔐 Autorisation CORS uniquement pour le simulateur officiel
origins = [
    "https://bot.gogokodo.com",
]

# Configuration CORS : le simulateur doit pouvoir interroger ton API
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,             # Autorise uniquement le simulateur
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔁 Route de base pour vérifier si le bot est en ligne
@app.get("/")
def root():
    return {"message": "Bot OK"}

# 🧠 Fonction de logique du bot : décision en fonction de l'état du jeu
def prendre_decision(etat_jeu: dict) -> dict:
    # Déplacements possibles
    directions = ["UP", "DOWN", "LEFT", "RIGHT", "STAY"]
    action_possibles = ["COLLECT", "ATTACK", "BOMB", "NONE"]

    # Mouvement aléatoire pour l'instant
    move = random.choice(directions)

    # Logique simple en fonction de l'état du jeu
    if etat_jeu.get("ennemi_proche"):
        action = "ATTACK"
    elif etat_jeu.get("bombe_disponible"):
        action = "BOMB"
    elif etat_jeu.get("ressource_proche"):
        action = "COLLECT"
    else:
        action = "NONE"

    # Retourne la décision finale
    return {
        "move": move,
        "action": action
    }

# 📡 Route appelée par le simulateur toutes les 10 secondes
@app.get("/action")
async def action(request: Request):
    try:
        # Récupération de l'état du jeu (JSON envoyé par le simulateur)
        etat_jeu = await request.json()
    except:
        # Si le JSON est vide ou malformé, on agit par défaut
        etat_jeu = {}

    print("État reçu :", etat_jeu)  # Debug dans la console

    # Appel de la fonction logique pour décider
    reponse = prendre_decision(etat_jeu)

    print("Réponse envoyée :", reponse)  # Debug

    # Envoi de la réponse au simulateur
    return JSONResponse(content=reponse)