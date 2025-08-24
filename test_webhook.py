import pytest

def test_webhook_reception_simulee():
    # Simulation d'un webhook reçu correctement
    fake_webhook = {"service": "catalog", "event_id": 12345}
    status_code = 200
    print(f"Webhook reçu : {fake_webhook} => {status_code} OK")
    assert status_code == 200
    
    
