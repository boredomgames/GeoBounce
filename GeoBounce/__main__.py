import sys

from .game import GAME_NAME, Game
from .gui import GUI, Button, Label
from .level import Level
from .levels import level1, level2


class GeoBounce(object):
    def __init__(self):
        self._game = Game()
        self._gui = GUI(
            self._game,
            coords=(200, 10),
            dimensions=(400, 590),
            widgets=[
                [Label("GeoBounce", style={"font_size": 100})],
                [
                    Button(
                        "Level 1",
                        command=lambda e: self.run_level("Level 1", level1),
                    ),
                    Button(
                        "Level 2",
                        command=lambda e: self.run_level("Level 2", level2),
                    ),
                ],
                [
                    Label(
                        "Please come back later for more levels...",
                        style={"font_size": 20},
                    )
                ],
            ],
        )

    def run(self):
        self._gui.draw()
        self._game.play(loop=True)

    def run_level(self, name, level):
        self._gui.delete()

        level = Level(self._game, name, level)
        level.generate()
        level.draw()
        level.run()
        level.delete()

        self._gui.draw()
        self._game.name = GAME_NAME


if __name__ == "__main__":
    game = GeoBounce()
    game.run()
