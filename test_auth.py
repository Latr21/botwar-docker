import pytest

def test_login_simulation():
    # Simulation d'une réponse HTTP 200 après une connexion réussie
    status_code = 200
    print(f"Connexion testée : {status_code} OK")
    assert status_code == 200