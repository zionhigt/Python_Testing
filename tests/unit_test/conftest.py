import pytest
from unittest.mock import patch


import server

def get_clubs():
    return [
            {
                "name":"TEST_CLUB",
                "email":"TEST_CLUB_EMAIL",
                "points":"13"
            }
        ]

def get_competitions():
    return [
            {
                "name": "TEST_COMPETITION",
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "25"
            }
        ]

@pytest.fixture(scope="class")
def clubs(request):
    request.cls.clubs = get_clubs()
    yield

@pytest.fixture(scope="class")
def competitions(request):
    request.cls.competitions =  get_competitions()
    yield

@pytest.fixture(scope="class")
def client(request):
    with patch("server.clubs", get_clubs()):
        with patch("server.competitions", get_competitions()):
            with server.app.test_client() as client:
                request.cls.client = client
                yield