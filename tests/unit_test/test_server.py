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

    def test_sould_connect_with_email_exists(self):
        for cl in self.clubs:
            response = self.client.post("/showSummary", data={'email': cl.get('email')})
            self.assertEqual(response.status_code, 200)

    def test_sould_no_connect_with_email_does_not_exists(self):
        response = self.client.post("/showSummary", data={'email': "not_exists_email@test.com"})
        self.assertEqual(response.status_code, 401)
    
    def test_sould_not_purshase_more_than_I_own(self):
        for com in self.competitions:
            for cl in self.clubs:
                mock = {
                    "club": cl.get('name'),
                    "competition": com.get('name'),
                    "places": int(cl.get('points')) + 1
                }
                
                response = self.client.post('/purchasePlaces', data=mock)
                self.assertIn("You haven&#39;t enough of points to purshase this!", response.data.decode())
                self.assertEqual(response.status_code, 403)
    
    def test_sould_not_purshase_more_than_12_places(self):
        response = self.client.post('/purchasePlaces', data={
            "club": "TEST_CLUB",
            "competition": "TEST_COMPETITION",
            "places": 13
        })
        self.assertIn("You cannot required more than 12 places!", response.data.decode())
        self.assertEqual(response.status_code, 403)
