import main
import pytest

def test_get_temperature_by_lat_lng(monkeypatch):
    lat = -14.235004
    lng = -51.92528
    expected = 16

    def mock(lat, lng):
        return 16

    monkeypatch.setattr("main.get_temperature", mock)
    assert main.get_temperature(lat, lng) == expected

def test_get_no_temperature(monkeypatch):
    lat = -14.235004
    lng = -51.92528
    expected = 16

    def mock(lat, lng):
        return

    monkeypatch.setattr("main.get_temperature", mock)
    assert main.get_temperature(lat, lng) == None

