from unittest import TestCase
from pytest import mark
import json

with open("./tests/mocks_files/fixture_load.json", 'r') as FILE_CURSOR:
    FILE = json.load(FILE_CURSOR)
competitions = FILE.get("competitions")
clubs = FILE.get("clubs")
@mark.usefixtures('client')
class INTServer(TestCase):

    def test_scenario(self):
        ## Test login
        response_club = self.client.post("/showSummary", data={'email': clubs[0].get('email')})
        self.assertEqual(response_club.status_code, 200)
        ## Test get book
        response_book = self.client.get(f'/book/{competitions[0].get("name")}/{clubs[0].get("name")}')
        self.assertEqual(response_book.status_code, 200)
        ## Test purchase places
        body = {
            "club": clubs[0].get("name"),
            "competition": competitions[1].get("name"),
            "places": 1
        }
        response_purchase = self.client.post("/purchasePlaces", data=body)
        self.assertEqual(response_purchase.status_code, 200)
        ## Test login in out
        response_out = self.client.get("/logout")
        self.assertEqual(response_out.status_code, 302)