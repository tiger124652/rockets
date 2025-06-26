import time
import random
import logging
import pygame as py
from projectile.rocket import Rocket
from projectile.bomb.bomb import Bomb
from settings import ROUNDS, ROCKETS, BOMBS


class GameRound:
    def __init__(self, app):
        self.app = app
        self.rounds = ROUNDS

        self.count_rockets = ROCKETS
        self.rockets = py.sprite.Group()
        self.count_bombs = BOMBS
        self.bombs = py.sprite.Group()
        self.fragments = py.sprite.Group()

        self.timer_rocket = time.time()
        self.time_rocket_interval = random.randint(5, 20) / 10
        self.timer_bomb = time.time()
        self.time_bomb_interval = random.randint(3, 5)

        self.logger = logging.getLogger(__name__)
        self.logger.info("GameRound initialized")


    def create_rocket(self):
        self.count_rockets -= 1
        self.rockets.add(Rocket(self.app))

    def create_bomb(self):
        self.count_bombs -= 1
        self.bombs.add(Bomb(self.app))

    def update(self):
        self.rockets.update()
        self.bombs.update()
        self.fragments.update()

        if time.time() - self.timer_rocket >= self.time_rocket_interval and self.count_rockets > 0:
            self.create_rocket()
            self.timer_rocket = time.time()
        if time.time() - self.timer_bomb >= self.time_bomb_interval and self.count_bombs > 0:
            self.create_bomb()
            self.timer_bomb = time.time()

        if self.count_rockets <= 0 and self.count_bombs <= 0:
            self.rounds -= 1
            self.count_rockets = ROCKETS
            self.count_bombs = BOMBS
            self.logger.info(f"start round №{ROUNDS-self.rounds+1}")

        if self.rounds == 0:
            self.app.is_running = False
            self.logger.info("The Player won")