import logging
import pygame as py
from settings import WIDTH, HEIGHT
from player import Player
from gameround import GameRound


class Game:
    def __init__(self):
        py.init()

        self.screen = py.display.set_mode((WIDTH, HEIGHT))
        self.clock = py.time.Clock()
        self.is_running = True

        logging.basicConfig(
            level=logging.DEBUG,
            format = "[%(asctime)s] #%(levelname)-8s %(filename)s:"
            "%(lineno)d - %(name)s - %(message)s"
            )
        self.logger = logging.getLogger(__name__)

        self.player = Player(self, WIDTH//2, HEIGHT//2)
        self.game_round = GameRound(self)

        self.logger.info("Game initialized")

    def update(self):
        self.player.update()
        self.game_round.update()

    def handle_events(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                self.is_running = False
            self.player.handle_event(event)

    def render(self):
        self.screen.fill("black")

        self.player.show()
        self.game_round.show_shells()

        py.display.flip()

    def start(self):
        while self.is_running:
            self.handle_events()
            self.render()
            self.update()

if __name__ == "__main__":
    game = Game()
    game.start()
