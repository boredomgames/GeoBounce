from .sprites import Obstacle, Surface, Player, Reward
from .timer import Timer


level1 = [
    {
        "type": "player",
        "position": [390, 380],
        "dimensions": [20, 20],
        "color": "blue",
    },
    {
        "type": "surface",
        "position": [0, 400],
        "dimensions": [800, 200],
        "color": "black",
    },
    {
        "type": "obstacle",
        "position": [900, 580],
        "dimensions": [20, 20],
        "color": "red",
    },
    {
        "type": "surface",
        "position": [1200, 580],
        "dimensions": [50, 20],
        "color": "black",
    },
    {
        "type": "reward",
        "position": [1220, 560],
        "dimensions": [10, 10],
        "color": "yellow",
    },
]

SPEED = 10
GRAVITY = 30


class Level(object):
    def __init__(self, game, name, items):
        self._name = name
        self._items = items
        self._game = game
        self._sprites = {
            "obstacles": [],
            "obstacles_tags": [],
            "surfaces": [],
            "surfaces_tags": [],
            "rewards": [],
            "rewards_tags": [],
            "player": None,
            "player_tag": None,
        }

        self._points_display = None
        self._player_gravity = True
        self._player_move = True
        self._player_points = 0
        self._end = False
        self._timer = Timer()

    def initialize(self):
        for item in self._items:
            if item["type"] == "obstacle":
                self._sprites["obstacles"].append(Obstacle(
                        self._game,
                        position=item["position"],
                        dimensions=item["dimensions"],
                        color=item["color"],
                ))
                self._sprites["obstacles"][-1].draw()
                self._sprites["obstacles_tags"].append(self._sprites["obstacles"][-1]._tag)
            elif item["type"] == "surface":
                self._sprites["surfaces"].append(Surface(
                        self._game,
                        position=item["position"],
                        dimensions=item["dimensions"],
                        color=item["color"],
                ))
                self._sprites["surfaces"][-1].draw()
                self._sprites["surfaces_tags"].append(self._sprites["surfaces"][-1]._tag)
            elif item["type"] == "reward":
                self._sprites["rewards"].append(Reward(
                        self._game,
                        position=item["position"],
                        dimensions=item["dimensions"],
                        color=item["color"],
                ))
                self._sprites["rewards"][-1].draw()
                self._sprites["rewards_tags"].append(self._sprites["rewards"][-1]._tag)
            elif item["type"] == "player":
                self._sprites["player"] = Player(
                        self._game,
                        position=item["position"],
                        dimensions=item["dimensions"],
                        color=item["color"],
                )
                self._sprites["player"].draw()
                self._sprites["player_tag"] = self._sprites["player"]._tag

        self._points_display = self._game._canvas.create_text(720, 20, text=f"Score: {self._player_points}", font="sans-serif")

    def run(self):
        self._game.play()

        while not self._end:
            self._timer.begin()

            for item in self._sprites["obstacles"]:
                item.move([-SPEED, 0])

            for item in self._sprites["surfaces"]:
                item.move([-SPEED, 0])

            for item in self._sprites["rewards"]:
                item.move([-SPEED, 0])

            self._sprites["player"].run_jump()
            self._game.update()
            self.check_collide()

            if self._player_gravity == True and self._sprites["player"]._position[1] + self._sprites["player"]._dimensions[1] < 600 and self._sprites["player"].jumping == False: # allow the player to fall if it can fall, is not at the bottom, and is not jumping
                self._sprites["player"].move([0, GRAVITY])

            if self._player_move == False: # move the player with the obstacles if it is blocked
                self._sprites["player"].move([-SPEED, 0])

            if self._sprites["player"]._position[0] + self._sprites["player"]._dimensions[0] <= 0: # end the game when the player exits the screen
                self._end = True

            if self._sprites["player"]._position[1] + self._sprites["player"]._dimensions[1] >= 600: # move the player back to the ground if it falls through (due to jumping)
                self._sprites["player"].teleport([self._sprites["player"]._position[0], 600 - self._sprites["player"]._dimensions[1]])

            for sprite in self._sprites["obstacles"]:
                if sprite._position[0] + sprite._dimensions[0] <= 0:
                    sprite.delete()

            for sprite in self._sprites["surfaces"]:
                if sprite._position[0] + sprite._dimensions[0] <= 0:
                    sprite.delete()

            for item in self._sprites["rewards"]:
                if sprite._position[0] + sprite._dimensions[0] <= 0:
                    sprite.delete()

            self._game._canvas.itemconfig(self._points_display, text=f"Score: {self._player_points}", font="sans-serif")

            self._game.update()

            self._timer.end(30)

    def check_collide(self):
        self._player_gravity = True
        self._player_move = True

        for item in self._sprites["player"].collide():
            if item in self._sprites["obstacles_tags"]:
                self._end = True # kill the player and end the game with it hits an obstacle
            elif item in self._sprites["surfaces_tags"]:
                collided_surface = self._sprites["surfaces"][self._sprites["surfaces_tags"].index(item)]

                if self._sprites["player"]._position[0] + self._sprites["player"]._dimensions[0] <= collided_surface._position[0]: # check if the player is in contact with the left side of the collided surface, if it is, prevent the player from moving
                    self._player_move = False
                elif self._sprites["player"]._position[1] + self._sprites["player"]._dimensions[1] >= collided_surface._position[1]: # check if the player is in contact with the top of the collided surface, if it is, prevent the player from falling
                    self._player_gravity = False
                    self._sprites["player"].teleport([self._sprites["player"]._position[0], collided_surface._position[1] - self._sprites["player"]._dimensions[1]]) # move the player on top of the surface if it falls into it slightly (due to jumping)
            elif item in self._sprites["rewards_tags"]:
                collided_surface = self._sprites["rewards"][self._sprites["rewards_tags"].index(item)]
                collided_surface.delete()
                self._player_points += 1
