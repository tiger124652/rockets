import logging
import random
import math
import pygame as py
from .fragment import Fragment
from settings import WIDTH, HEIGHT, SPEED_BOMB, FRAGMENTS, SPEED_FRAGMENTS


class Bomb(py.sprite.Sprite):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.image = py.image.load("textures/projectiles/bomb/bomb/model0.png")

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-70)
        self.rect.y = -70

        self.explode_line = HEIGHT // random.randint(2, 5)

        self.logger = logging.getLogger(__name__)
        self.logger.info("Bomb created")

    def explode(self):
        for i in range(0, 360, 360//FRAGMENTS):
            v = py.math.Vector2(math.cos(math.radians(i)),
                                math.sin(math.radians(i)))
            x = self.rect.centerx
            y = self.rect.centery
            self.app.game_round.fragments.add(Fragment(self.app, x, y,
                                                       v.x * SPEED_FRAGMENTS,
                                                       v.y * SPEED_FRAGMENTS))


    def show(self):
        self.app.screen.blit(self.image, self.rect)

    def move(self):
        self.rect = self.rect.move((0, SPEED_BOMB))

    def update(self):
        if self.rect.y > self.explode_line:
            self.explode()
            self.kill()
        elif self.rect.colliderect(self.app.player.rect):
            self.app.player.health -= 10
            self.explode()
            self.kill()
        self.move()
        self.show()
