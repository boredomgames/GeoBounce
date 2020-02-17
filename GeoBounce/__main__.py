from .game import Game
from .level import Level, level1


def main():
    game = Game()
    level = Level("Level 1", level1)
    level.set_up(game)
    game.play()
    level.run(game)


if __name__ == "__main__":
    main()
