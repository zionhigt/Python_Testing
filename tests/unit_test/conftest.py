import pytest
from unittest.mock import patch

import server

clubs_obj = [
            {
                "name":"TEST_CLUB_1",
                "email":"TEST_CLUB_EMAIL_1",
                "points":"10"
            },
            {
                "name":"TEST_CLUB_2",
                "email":"TEST_CLUB_EMAIL_2",
                "points":"10"
            }
        ]

competitions_obj = [
            {
                "name": "TEST_COMPETITION_1",
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "25"
            },
            {
                "name": "TEST_COMPETITION_2",
                "date": "2025-03-27 10:00:00",
                "numberOfPlaces": "25"
            }
        ]


@pytest.fixture(scope="class")
def clubs(request):
    request.cls.clubs = clubs_obj
    yield

@pytest.fixture(scope="class")
def competitions(request):
    request.cls.competitions = competitions_obj
    yield

@pytest.fixture(scope="class")
def client(request):
    with patch("server.clubs", clubs_obj):
        with patch("server.competitions", competitions_obj):
            with server.app.test_client() as client:
                request.cls.client = client
                request.cls.cost = server.cost
                yield