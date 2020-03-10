from .game import Game
from .level import LevelOld, Level
from .levels import level1, level2
import sys

def main():
    game = Game()
    if len(sys.argv) == 2 and sys.argv[1] == "lvl1":
        level = Level(game, "Level 1", level1)
    else:
        level = Level(game, "Level 2", level2)
    level.generate()
    level.draw()
    game.play()
    level.run()

if __name__ == "__main__":
    main()
