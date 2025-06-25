import logging
import pygame as py
from settings import PLAYER_HEALTH, PLAYER_SPEED, WIDTH, HEIGHT


class Player:
    def __init__(self, app, x, y):
        self.app = app

        self.health = PLAYER_HEALTH
        self.speed = PLAYER_SPEED

        self.image = py.Surface((100, 100))
        self.image.fill("red")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.init_flags()

        self.logger = logging.getLogger(__name__)
        self.logger.info("Player initialized")

    def init_flags(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def handle_event(self, event):
        if event.type == py.KEYDOWN:
            if event.unicode == "w":
                self.up = True
            elif event.unicode == "s":
                self.down = True
            elif event.unicode == "a":
                self.left = True
            elif event.unicode == "d":
                self.right = True
        elif event.type == py.KEYUP:
            if event.unicode == "w":
                self.up = False
            elif event.unicode == "s":
                self.down = False
            elif event.unicode == "a":
                self.left = False
            elif event.unicode == "d":
                self.right = False

    def move(self):
        if self.up and self.rect.top > 0:
            self.rect = self.rect.move((0, -self.speed))
        if self.down and self.rect.bottom < HEIGHT:
            self.rect = self.rect.move((0, self.speed))
        if self.left and self.rect.left > 0:
            self.rect = self.rect.move((-self.speed, 0))
        if self.right and self.rect.right < WIDTH:
            self.rect = self.rect.move((self.speed, 0))

    def update(self):
        self.move()

        if self.health <= 0:
            self.app.is_running = False
            self.logger.info("The Player lost")

    def show(self):
        self.app.screen.blit(self.image, self.rect)
