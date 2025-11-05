import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_random_word_by_level():
    response = client.get("/v1/random/a1")
    assert response.status_code == 200
    data = response.json()
    assert "word" in data
    assert "definitions" in data
    assert "level" in data

def test_random_word():
    response = client.get("/v1/random/a1")
    assert response.status_code == 200
    data = response.json()
    assert "word" in data
    assert "definitions" in data

def test_invalid_level():
    response = client.get("/v1/random/b5")
    assert response.status_code == 404