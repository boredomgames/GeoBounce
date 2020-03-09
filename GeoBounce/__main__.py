from .game import Game
from .level import LevelOld, Level
from .levels import level1, level2

def main():
    game = Game()
    # level = Level(game, "Level 1", level1)
    level = Level(game, "Level 2", level2)
    level.generate()
    level.draw()
    game.play()
    level.run()

if __name__ == "__main__":
    main()
