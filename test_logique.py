import pytest
from main import prendre_decision

def test_ressource_proche():
    etat = {"ressource_proche": True}
    decision = prendre_decision(etat)
    assert decision["action"] == "COLLECT"
    assert decision["move"] in ["UP", "DOWN", "LEFT", "RIGHT", "STAY"]

def test_ennemi_proche():
    etat = {"ennemi_proche": True}
    decision = prendre_decision(etat)
    assert decision["action"] == "ATTACK"
    assert decision["move"] in ["UP", "DOWN", "LEFT", "RIGHT", "STAY"]

def test_bombe_disponible():
    etat = {"bombe_disponible": True}
    decision = prendre_decision(etat)
    assert decision["action"] == "BOMB"
    assert decision["move"] in ["UP", "DOWN", "LEFT", "RIGHT", "STAY"]

def test_aucune_info():
    etat = {}
    decision = prendre_decision(etat)
    assert decision["action"] == "NONE"
    assert decision["move"] in ["UP", "DOWN", "LEFT", "RIGHT", "STAY"]