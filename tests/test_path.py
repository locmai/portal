import pytest
from fastapi.testclient import TestClient
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from ..main import app

client = TestClient(app)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_health_path():
    response = client.get("/")
    assert response.status_code == 200, response.text
    assert response.json() == {"status": "ok"}