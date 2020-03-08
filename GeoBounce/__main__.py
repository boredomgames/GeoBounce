from .game import Game
from .level import LevelOld, Level
from .levels import level1


# def main():
#     game = Game()
#     level = LevelOld(game, "Level 1", level1)
#     # level._testmode = True  # FOR TESTING ONLY
#     level.initialize()
#     game.play()
#     level.run()


def main():
    game = Game()
    level = Level(game, "Level 1", level1, legacy=True)
    level.generate()
    level.draw()
    game.play()
    level.run()


if __name__ == "__main__":
    main()
