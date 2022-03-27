import pytest

from server import app

@pytest.fixture(scope="class")
def client(request):
    with app.test_client() as client:
        request.cls.client = client


@pytest.fixture(scope="class")
def clubs(request):
    fixture = [
            {
                "name":"TEST_CLUB",
                "email":"TEST_CLUB_EMAIL",
                "points":"13"
            }
        ]
    request.cls.clubs = fixture


@pytest.fixture(scope="class")
def competitions(request):
    fixture = [
            {
                "name": "TEST_COMPETITION",
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "25"
            }
        ]
    request.cls.competitions =  fixture