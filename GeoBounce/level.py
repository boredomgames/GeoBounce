from .sprites import Obstacle, Item, Player
from .timer import Timer


level1 = [
    {
        "type": "player",
        "position": [390, 580],
        "dimensions": [20, 20],
        "color": "blue"
    },
    {
        "type": "obstacle",
        "position": [1000, 580],
        "dimensions": [20, 20],
        "color": "black"
    }
]

SPEED = 5


class Level(object):
    def __init__(self, name, things):
        self._name = name
        self._things = things
        self._drawn = []
        self._end = False
        self._timer = Timer()
        self._obstacles = []
        self._player = None
        self._items = []

    def set_up(self, game):
        for item in self._things:
            if item["type"] == "obstacle":
                self._drawn.append(Obstacle(game, position=item["position"], dimensions=item["dimensions"], color=item["color"]))
                self._drawn[-1].draw()
                self._obstacles.append(self._drawn[-1]._tag)
            elif item["type"] == "item":
                self._drawn.append(Item(game, position=item["position"], dimensions=item["dimensions"], color=item["color"]))
                self._drawn[-1].draw()
                self._items.append(self._drawn[-1]._tag)
            elif item["type"] == "player":
                self._drawn.append(Player(game, position=item["position"], dimensions=item["dimensions"], color=item["color"]))
                self._drawn[-1].draw()
                self._player = self._drawn[-1]

    def run(self, game):
        game.play()

        while not self._end:
            if not self._timer.tick(60):
                continue

            for item in self._drawn:
                if item is not self._player:
                    item.move([-SPEED, 0])

            self._player.run_jump()

            game.update()

            self.check_collide(game)

    def check_collide(self, game):
        for item in self._player.collide():
            if item in self._obstacles:
                self._end = True
            elif item in self._items:
                pass
