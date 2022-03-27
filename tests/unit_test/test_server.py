from unittest.mock import patch
from unittest import TestCase

from pytest import mark

from server import loadClubs, loadCompetitions


@mark.usefixtures('client', 'clubs', 'competitions')
class TestServer(TestCase):

    def test_loadClubs(self):
        self.assertListEqual(loadClubs("./tests/unit_test/mocks_files/fixture_load.json"), self.clubs)

    def test_loadCompetitions(self):
        self.assertListEqual(loadCompetitions("./tests/unit_test/mocks_files/fixture_load.json"), self.competitions)

    def test_sould_login_in_out(self):
        response = self.client.get("/logout")
        self.assertEqual(response.status_code, 302)
