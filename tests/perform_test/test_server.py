import time
from random import randint
from locust import HttpUser, task, between

from server import loadClubs, loadCompetitions

competitions = loadCompetitions()
clubs = loadClubs()

class User(HttpUser):
    wait_time = between(1, 5)

    @task
    def home(self):
        self.client.get("/")

    def logout(self):
        self.client.get("/logout")

    @task
    def connect(self):
        club = clubs[randint(0, len(clubs) - 1)]
        self.client.post("/showSummary", {"email":club.get("email")})
        self.client.post("/showSummary", {"email":"not_exist@test.com"})

    @task(3)
    def getBooking(self):
        competition = competitions[randint(0, len(competitions) - 1)]
        club = clubs[randint(0, len(clubs) - 1)]
        self.client.get(f'/book/{competition.get("name")}/{club.get("name")}')

    @task
    def purchasePlaces(self):
        competition = competitions[randint(0, len(competitions) - 1)]
        club = clubs[randint(0, len(clubs) - 1)]
        body = {
            "club": club.get("name"),
            "competition": competition.get("name"),
            "places": randint(1, 13)
        }
        self.client.post("/purchasePlaces", body)
    