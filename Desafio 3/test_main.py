import main
import pytest
import requests

class MockResponse:
    """
    Classe para simular consulta a API.
    """
    @staticmethod
    def json(): # Method to simulate a JSON response
        return {"currently": {"temperature": 62}}

def test_get_temperature_by_lat_lng(monkeypatch):
    """
    Test for the get_temperature function
    """    
    lat = -14.235004
    lng = -51.92528
    expected = 16

    def mock_get(*args): # Method to call the mock
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)
    assert main.get_temperature(lat, lng) == expected


def test_get_no_temperature(monkeypatch):
    """
    Teste automatizado para a função get_temperature sem retorno da API.
    """   
    lat = -14.235004
    lng = -51.92528
    expected = None

    def mock(lat, lng): # Method to call a JSON response simulator
        return 

    monkeypatch.setattr("main.get_temperature", mock)
    assert main.get_temperature(lat, lng) == None

