from main import get_temperature
import pytest

def test_get_temperature_by_lat_lng(monkeypatch):
    lat = -14.235004
    lng = -51.92528
    expected = 16

    def mock(lat, lng):
        return 16

    # x = get_temperature(lat, lng)
    monkeypatch.setattr("main.get_temperature", mock)

    assert get_temperature(lat, lng) == expected
    # assert x == expected
