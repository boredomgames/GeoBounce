from .game import Game
from .level import Level
from .levels import level1


def main():
    game = Game()
    level = Level(game, "Level 1", level1)
    # level._testmode = True  # FOR TESTING ONLY
    level._askclose = False
    level.initialize()
    game.play()
    level.run()


if __name__ == "__main__":
    main()
