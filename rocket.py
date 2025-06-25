import logging
import pygame as py
from settings import SPEED_ROCKET

class Rocket(py.sprite.Sprite):
    def __init__(self, app, x, y):
        super().__init__()
        self.app = app

        self.image = py.Surface((50, 50))
        self.image.fill("yellow")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        v = py.math.Vector2(
            self.app.player.rect.centerx - self.rect.centerx,
            self.app.player.rect.centery - self.rect.centery
            )

        self.vx = v.normalize().x * SPEED_ROCKET
        self.vy = v.normalize().y * SPEED_ROCKET

        self.logger = logging.getLogger(__name__)
        self.logger.info("Rocket created")

    def move(self):
        self.rect = self.rect.move((self.vx, self.vy))

    def update(self):
        self.move()

    def show(self):
        self.app.screen.blit(self.image, self.rect)