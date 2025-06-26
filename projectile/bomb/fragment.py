import logging
import pygame as py


class Fragment(py.sprite.Sprite):
    def __init__(self, app, x, y, vx, vy):
        super().__init__()
        self.app = app

        self.image = py.image.load("textures/projectiles/bomb/fragment/model0.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.vx = vx
        self.vy = vy

        self.logger = logging.getLogger(__name__)

    def move(self):
        self.rect = self.rect.move((self.vx, self.vy))

    def show(self):
        self.app.screen.blit(self.image, self.rect)

    def update(self):
        self.move()
        self.show()

        if not self.rect.colliderect(self.app.screen.get_rect()):
            self.kill()
        elif self.rect.colliderect(self.app.player.rect):
            self.app.player.health -= 10
            self.kill()