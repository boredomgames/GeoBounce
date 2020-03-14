from .game import Game
from .level import Level
from .levels import level1, level2
from .gui import GUI, Button, Label

import sys

GUI_DRAWN = False
GAME_RUNNING = False

def level_runner(gui, game, name, level):
    global GAME_RUNNING, GUI_DRAWN
    gui.delete()
    GUI_DRAWN = False

    level = Level(game, name, level)
    level.generate()
    level.draw()
    level.run()
    level.delete()

    GAME_RUNNING = False

def main():
    global GUI_DRAWN

    game = Game()
    game.play()
    gui = GUI(game, (200, 10), (400, 590), widgets=[
        [
            Label("GeoBounce", style={"font_size": 100})
        ],
        [
            Button("Level 1", command=lambda e: level_runner(gui, game, "Level 1", level1)),
            Button("Level 2", command=lambda e: level_runner(gui, game, "Level 2", level2)),
        ]
    ])

    while True:
        if not GAME_RUNNING:
            game.update()

            if not GUI_DRAWN:
                GUI_DRAWN = True
                gui.draw()

if __name__ == "__main__":
    main()
