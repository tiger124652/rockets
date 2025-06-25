import time
import random
import logging
import pygame as py
from rocket import Rocket
from settings import ROUNDS, ROCKETS, WIDTH, HEIGHT


class GameRound:
    def __init__(self, app):
        self.app = app
        self.rounds = ROUNDS

        self.count_rockets = ROCKETS
        self.rockets = py.sprite.Group()

        self.timer_rocket = time.time()
        self.time_rocket_interval = random.randint(5, 20) / 10

        self.logger = logging.getLogger(__name__)
        self.logger.info("GameRound initialized")


    def create_rockets(self):
        self.count_rockets -= 1

        x = random.choice([0, WIDTH])
        y = random.choice([0, HEIGHT])
        self.rockets.add(Rocket(self.app, x, y))

    def update(self):
        self.rockets.update()

        if time.time() - self.timer_rocket >= self.time_rocket_interval:
            self.create_rockets()
            self.timer_rocket = time.time()
            self.time_rocket_interval = random.randint(5, 20) / 10

        if self.count_rockets == 0:
            self.rounds -= 1
            self.count_rockets = ROCKETS
        if self.rounds == 0:
            self.app.is_running = False
            self.logger.info("The Player won")

    def show_shells(self):
        [rocket.show() for rocket in self.rockets]