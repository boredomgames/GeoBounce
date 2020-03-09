from .sprites import (
    RectangleSprite,
    ImageSprite,
    OvalSprite,
    LineSprite,
    PolygonSprite,
)  # new
from .sprites import Obstacle, Surface, Reward, Player  # old
from .timer import Timer

from tkinter import messagebox


# low
# SPEED = 10
# GRAVITY = 30

# high
SPEED = 5
GRAVITY = 15

SPRITE_TYPES = {
    "rectangle": RectangleSprite,
    "image": ImageSprite,
    "oval": OvalSprite,
    "line": LineSprite,
    "polygon": PolygonSprite,
}

JUMP_PATH = (12, 11, 10, 9, 8, 7, 6, 5, 0, 0, 0)

JUMP_FRAMES = len(JUMP_PATH) * 2
FPS = 60


class Level(object):
    def __init__(
        self,
        game,
        name,
        items,
        legacy=False,
        config={"dimensions": [800, 600], "resizable": False},
    ):
        self._game = game
        self._name = name
        self._config = config
        self._items = items

        self._obstacles = []
        self._obstacles_tags = []
        self._surfaces = []
        self._surfaces_tags = []
        self._rewards = []
        self._rewards_tags = []
        self._player = []
        self._player_tag = []

        self._player_jumping = False
        self._player_stuck = False
        self._player_gravity = True
        self._player_points = 0
        self._player_jump_frames = 0
        self._testmode = False

        self._legacy = legacy
        self._end = False
        self._timer = Timer()

    def generate(self):
        if self._legacy:
            for item in self._items:
                self.generate_legacy_sprite(item)
        else:
            for item in self._items:
                self.generate_sprite(item)

    def generate_legacy_sprite(self, item):
        if item["type"] == "obstacle":
            self._obstacles.append(
                RectangleSprite(
                    self._game,
                    coords=item["position"],
                    dimensions=item["dimensions"],
                    fill=item["color"],
                    outline=item["color"],
                )
            )
        elif item["type"] == "surface":
            self._surfaces.append(
                RectangleSprite(
                    self._game,
                    coords=item["position"],
                    dimensions=item["dimensions"],
                    fill=item["color"],
                    outline=item["color"],
                )
            )
        elif item["type"] == "reward":
            self._rewards.append(
                RectangleSprite(
                    self._game,
                    coords=item["position"],
                    dimensions=item["dimensions"],
                    fill=item["color"],
                    outline=item["color"],
                )
            )
        elif item["type"] == "player":
            self._player.append(
                RectangleSprite(
                    self._game,
                    coords=item["position"],
                    dimensions=item["dimensions"],
                    fill=item["color"],
                    outline=item["color"],
                )
            )

    def generate_sprite(self, item):
        types = {
            "obstacle": self._obstacles,
            "surface": self._surfaces,
            "reward": self._rewards,
            "player": self._player,
        }

        if item["sprite_type"] in ("rectangle", "oval"):
            types[item["type"]].append(
                SPRITE_TYPES[item["sprite_type"]](
                    self._game,
                    coords=item["coords"],
                    dimensions=item["dimensions"],
                    fill=item["fill"],
                    outline=item["outline"],
                )
            )
        elif item["sprite_type"] == "image":
            types[item["type"]].append(
                SPRITE_TYPES[item["sprite_type"]](
                    self._game,
                    coords=item["coords"],
                    dimensions=item["dimensions"],
                    image=item["image"],
                )
            )
        elif item["sprite_type"] == "line":
            types[item["type"]].append(
                SPRITE_TYPES[item["sprite_type"]](
                    self._game,
                    coords=item["coords"],
                    width=item["width"],
                    fill=item["fill"],
                )
            )
        elif item["sprite_type"] == "polygon":
            types[item["type"]].append(
                SPRITE_TYPES[item["sprite_type"]](
                    self._game,
                    coords=item["coords"],
                    fill=item["fill"],
                    outline=item["outline"],
                )
            )
        else:
            raise ValueError(f'{item["sprite_type"]} is not a sprite type')

    def draw(self):
        for obstacle in self._obstacles:
            obstacle.draw()
            self._obstacles_tags.append(obstacle._tag)

        for surface in self._surfaces:
            surface.draw()
            self._surfaces_tags.append(surface._tag)

        for reward in self._rewards:
            reward.draw()
            self._rewards_tags.append(reward._tag)

        for player in self._player:
            player.draw()
            self._player_tag.append(player._tag)

    def run(self):
        self._game.name = self._name
        self._game.dimensions = self._config["dimensions"]
        self._game.resizable = self._config["resizable"]

        @self._game.on("<space>")
        def event_space(event):
            self._player_jumping = True

        while not self._end:
            self._timer.begin()
            self.move()
            self.player_jump()
            self.collide()
            self.player_move()
            self._game.update()

            if self._testmode:
                self._end = False

            self._timer.end(FPS)

        while True:
            self._game.update()
            pass

    def move(self):
        for obstacle in self._obstacles:
            obstacle.move((-SPEED, 0))

        for surface in self._surfaces:
            surface.move((-SPEED, 0))

        for reward in self._rewards:
            reward.move((-SPEED, 0))

    def player_jump(self):
        if (
            self._player_jumping == True
            and self._player_jump_frames < JUMP_FRAMES
        ):
            self._player_gravity = False

            if self._player_jump_frames < JUMP_FRAMES / 2:
                self._player[0].move((0, -JUMP_PATH[self._player_jump_frames]))
            else:
                self._player[0].move(
                    (
                        0,
                        JUMP_PATH[
                            int(JUMP_FRAMES / 2) - self._player_jump_frames
                        ],
                    )
                )

            self._player_jump_frames += 1
        else:
            self._player_jump_frames = 0
            self._player_jumping = False

    def player_move(self):
        player = self._player[0]
        player_bbox = player.bbox()
        window_width, window_height = self._game.dimensions

        if (
            self._player_gravity
            and player_bbox[3] < window_height
            and not self._player_jumping
        ):
            player.move([0, GRAVITY])

        if self._player_stuck:
            player.move([-SPEED, 0])

        if player_bbox[3] <= 0:
            self._end = True

        if player_bbox[3] >= window_height:
            player.teleport(
                (
                    player_bbox[0],
                    window_height - (player_bbox[3] - player_bbox[1]),
                )
            )

    def collide(self):
        self._player_stuck = False
        self._player_gravity = True

        for item in self._player[0].collide():
            if item in self._obstacles_tags:
                self._end = True

            if item in self._surfaces_tags:
                surface = self._surfaces[self._surfaces_tags.index(item)].bbox()
                player = self._player[0].bbox()

                if player[2] <= surface[0]:
                    self._player_stuck = True
                elif player[3] >= surface[1]:
                    self._player_gravity = False

                    if not player[3] > surface[3]:
                        self._player[0].teleport(
                            (player[0], surface[1] - (player[3] - player[1]))
                        )
                    else:
                        self._player_jumping = False
                        self._player_gravity = True

            if item in self._rewards_tags:
                reward = self._rewards[self._rewards_tags.index(item)]
                reward.delete()
                self._player_points += 1
                del self._rewards[self._rewards_tags.index(item)]
                del self._rewards_tags[self._rewards_tags.index(item)]


class LevelOld(object):
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
        self._testmode = False
        self._askclose = True
        self._timer = Timer()

    def initialize(self):
        for item in self._items:
            if item["type"] == "obstacle":
                self._sprites["obstacles"].append(
                    Obstacle(
                        self._game,
                        position=item["position"],
                        dimensions=item["dimensions"],
                        color=item["color"],
                    )
                )
                self._sprites["obstacles"][-1].draw()
                self._sprites["obstacles_tags"].append(
                    self._sprites["obstacles"][-1]._tag
                )
            elif item["type"] == "surface":
                self._sprites["surfaces"].append(
                    Surface(
                        self._game,
                        position=item["position"],
                        dimensions=item["dimensions"],
                        color=item["color"],
                    )
                )
                self._sprites["surfaces"][-1].draw()
                self._sprites["surfaces_tags"].append(
                    self._sprites["surfaces"][-1]._tag
                )
            elif item["type"] == "reward":
                self._sprites["rewards"].append(
                    Reward(
                        self._game,
                        position=item["position"],
                        dimensions=item["dimensions"],
                        color=item["color"],
                    )
                )
                self._sprites["rewards"][-1].draw()
                self._sprites["rewards_tags"].append(
                    self._sprites["rewards"][-1]._tag
                )
            elif item["type"] == "player":
                self._sprites["player"] = Player(
                    self._game,
                    position=item["position"],
                    dimensions=item["dimensions"],
                    color=item["color"],
                )
                self._sprites["player"].draw()
                self._sprites["player_tag"] = self._sprites["player"]._tag

        self._points_display = self._game._canvas.create_text(
            720, 20, text=f"Score: {self._player_points}", font="sans-serif"
        )

        def event_close():
            if self._askclose and messagebox.askokcancel(
                "Quit", "Do you want to quit?"
            ):
                self._game.terminate()
            elif not self._askclose:
                self._game.terminate()

        self._game._window.protocol("WM_DELETE_WINDOW", event_close)

    def run(self):
        self._game.play()

        while not self._end or self._testmode:
            self._timer.begin()

            for item in self._sprites["obstacles"]:
                item.move([-SPEED, 0])

            for item in self._sprites["surfaces"]:
                item.move([-SPEED, 0])

            for item in self._sprites["rewards"]:
                item.move([-SPEED, 0])

            self._sprites["player"].run_jump()
            self.check_collide()

            if (
                self._player_gravity == True
                and self._sprites["player"]._coords[1]
                + self._sprites["player"]._dimensions[1]
                < 600
                and self._sprites["player"].jumping == False
            ):  # allow the player to fall if it can fall, is not at the bottom, and is not jumping
                self._sprites["player"].move([0, GRAVITY])

            if (
                self._player_move == False
            ):  # move the player with the obstacles if it is blocked
                self._sprites["player"].move([-SPEED, 0])

            if (
                self._sprites["player"]._coords[0]
                + self._sprites["player"]._dimensions[0]
                <= 0
            ):  # end the game when the player exits the screen
                self._end = True

            if (
                self._sprites["player"]._coords[1]
                + self._sprites["player"]._dimensions[1]
                >= 600
            ):  # move the player back to the ground if it falls through (due to jumping)
                self._sprites["player"].teleport(
                    [
                        self._sprites["player"]._coords[0],
                        600 - self._sprites["player"]._dimensions[1],
                    ]
                )

            for sprite in self._sprites["obstacles"]:
                if sprite._coords[0] + sprite._dimensions[0] <= 0:
                    sprite.delete()

            for sprite in self._sprites["surfaces"]:
                if sprite._coords[0] + sprite._dimensions[0] <= 0:
                    sprite.delete()

            for sprite in self._sprites["rewards"]:
                if sprite._coords[0] + sprite._dimensions[0] <= 0:
                    sprite.delete()

            self._game._canvas.itemconfig(
                self._points_display,
                text=f"Score: {self._player_points}",
                font="sans-serif",
            )

            if len(self._game._canvas.find_all()) == 2:
                break

            self._game.update()

            # low
            # self._timer.end(30)

            # high
            self._timer.end(60)

        while True:
            if self._end == True:
                self._game._canvas.create_text(
                    400, 300, text="YOU LOST", font="sans-serif 72"
                )
            else:
                self._game._canvas.create_text(
                    400, 300, text="YOU WON!", font="sans-serif 72"
                )

                if self._player_points == 1:
                    self._game._canvas.create_text(
                        400,
                        350,
                        text=f"You Earned {self._player_points} Point!",
                        font="sans-serif 24",
                    )
                else:
                    self._game._canvas.create_text(
                        400,
                        350,
                        text=f"You Earned {self._player_points} Points!",
                        font="sans-serif 24",
                    )

            self._game.update()

    def check_collide(self):
        self._player_gravity = True
        self._player_move = True

        for item in self._sprites["player"].collide():
            if item in self._sprites["obstacles_tags"]:
                self._end = (
                    True
                )  # kill the player and end the game with it hits an obstacle
            elif item in self._sprites["surfaces_tags"]:
                collided_surface = self._sprites["surfaces"][
                    self._sprites["surfaces_tags"].index(item)
                ]

                if (
                    self._sprites["player"]._coords[0]
                    + self._sprites["player"]._dimensions[0]
                    <= collided_surface._coords[0]
                ):  # check if the player is in contact with the left side of the collided surface, if it is, prevent the player from moving
                    self._player_move = False
                elif (
                    self._sprites["player"]._coords[1]
                    + self._sprites["player"]._dimensions[1]
                    >= collided_surface._coords[1]
                ):  # check if the player is in contact with the top of the collided surface, if it is, prevent the player from falling
                    self._player_gravity = False
                    self._sprites["player"].teleport(
                        [
                            self._sprites["player"]._coords[0],
                            collided_surface._coords[1]
                            - self._sprites["player"]._dimensions[1],
                        ]
                    )  # move the player on top of the surface if it falls into it slightly (due to jumping)
            elif item in self._sprites["rewards_tags"]:
                collided_surface = self._sprites["rewards"][
                    self._sprites["rewards_tags"].index(item)
                ]
                collided_surface.delete()
                self._player_points += 1
