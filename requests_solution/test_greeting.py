"""Module"""

import requests

URL = "http://127.0.0.1:61673"

def test_response():
    """Method"""
    response = requests.get(URL,timeout=60)
    assert response.status_code == 200
    assert "<h1>Hello from the Backend!</h1>" in response.text

def test_content():
    """Method"""
    response = requests.get(URL,timeout=60)
    assert "<h1>Hello from the Backend!</h1>" == response.text
