import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from ..main import app
from fastapi.testclient import TestClient

client = TestClient(app)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_health_path():
    response = client.get("/")
    assert response.status_code == 200, response.text
    assert response.json() == {"status": "ok"}

def test_404_path():
    response = client.get("/404")
    assert response.status_code == 404, response.text
    assert response.json() == {"detail":"Not Found"}
