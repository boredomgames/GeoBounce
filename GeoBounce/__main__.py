from .game import Game
from .level import Level, level1


def main():
    game = Game()
    level = Level(game, "Level 1", level1)
    level.initialize()
    game.play()
    level.run()


if __name__ == "__main__":
    main()
