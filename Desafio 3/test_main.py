import main
import pytest
import requests

class MockResponse:
    @staticmethod
    def json():
        return {"currently": {"temperature": 62}}

def test_get_temperature_by_lat_lng(monkeypatch):
    lat = -14.235004
    lng = -51.92528
    expected = 16

    def mock_get(*args):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)
    assert main.get_temperature(lat, lng) == expected
