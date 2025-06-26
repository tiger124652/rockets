import random
import logging
import pygame as py
from settings import SPEED_ROCKET, WIDTH, HEIGHT

class Rocket(py.sprite.Sprite):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.image = py.Surface((50, 50))
        self.image.fill("yellow")

        self.rect = self.image.get_rect()
        self.rect.x = random.choice([10, WIDTH-10])
        self.rect.y = random.choice([10, HEIGHT-10])

        v = py.math.Vector2(
            self.app.player.rect.centerx - self.rect.centerx,
            self.app.player.rect.centery - self.rect.centery
            )

        self.vx = v.normalize().x * SPEED_ROCKET
        self.vy = v.normalize().y * SPEED_ROCKET

        self.logger = logging.getLogger(__name__)
        self.logger.info("Rocket created")

    def show(self):
        self.app.screen.blit(self.image, self.rect)

    def move(self):
        self.rect = self.rect.move((self.vx, self.vy))

    def update(self):
        self.move()
        self.show()

        if not self.rect.colliderect(self.app.screen.get_rect()):
            self.kill()
        elif self.rect.colliderect(self.app.player.rect):
            self.app.player.health -= 10
            self.kill()