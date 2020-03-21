from .gui import GUI, Button, Label
from .sprites import (
    ImageSprite,
    LineSprite,
    OvalSprite,
    PolygonSprite,
    RectangleSprite,
)
from .timer import Timer

SPEED = 5
GRAVITY = 15

SPRITE_TYPES = {
    "rectangle": RectangleSprite,
    "image": ImageSprite,
    "oval": OvalSprite,
    "line": LineSprite,
    "polygon": PolygonSprite,
}

JUMP_PATH = (12, 11, 10, 9, 8, 7, 6, 5, 0, 0)

JUMP_FRAMES = len(JUMP_PATH) * 2
FPS = 60


class Level(object):
    def __init__(
        self,
        game,
        name,
        items,
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
        self._goal = []
        self._goal_tag = []

        self._player_jumping = False
        self._player_stuck = False
        self._player_gravity = True
        self._player_points = 0
        self._player_jump_frames = 0
        self._player_dead = False
        self._player_points_display = Label(f"Points: {self._player_points}")
        self._gui = GUI(
            self._game,
            coords=(700, 10),
            dimensions=(100, 10),
            widgets=[[self._player_points_display]],
        )

        self._testmode = False
        self._end = False
        self._timer = Timer()

    def generate(self):
        for item in self._items:
            self.generate_sprite(item)

    def generate_sprite(self, item):
        types = {
            "obstacle": self._obstacles,
            "surface": self._surfaces,
            "reward": self._rewards,
            "player": self._player,
            "goal": self._goal,
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

        for goal in self._goal:
            goal.draw()
            self._goal_tag.append(goal._tag)

        self._gui.draw()

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
            self.player_move()
            self.player_jump()
            self.collide()
            self.update_points()
            self._game.update()

            if self._player_dead and self._testmode:
                self._end = False
                self._player_dead = False

            self._timer.end(FPS)

        self.end_screen()

        while not self._end:
            self._game.update()

    def end_screen(self):
        self._end = False
        self._gui.delete()

        # needed for "Continue" button
        def exit_level(event):
            self._end = True

        self._gui = GUI(
            self._game,
            coords=(50, 125),
            dimensions=(700, 200),
            widgets=[
                [
                    Label(
                        "You Died" if self._player_dead else "You Won",
                        style={"font_size": 75},
                    )
                ],
                [
                    Label(
                        f"""You earned {self._player_points} {
                            "point" if self._player_points == 1 else "points"
                        }""",
                        style={"font_size": 20},
                    )
                ],
                [Button("Continue", command=exit_level)],
            ],
        )

        self._gui.draw()

    def update_points(self):
        self._player_points_display.update(
            self._game, text=f"Points: {self._player_points}"
        )

    def delete(self):
        for obstacle in self._obstacles:
            obstacle.delete()

        for surface in self._surfaces:
            surface.delete()

        for reward in self._rewards:
            reward.delete()

        for goal in self._goal:
            goal.delete()

        self._player[0].delete()
        self._gui.delete()

    def move(self):
        for obstacle in self._obstacles:
            obstacle.move((-SPEED, 0))

        for surface in self._surfaces:
            surface.move((-SPEED, 0))

        for reward in self._rewards:
            reward.move((-SPEED, 0))

        for goal in self._goal:
            goal.move((-SPEED, 0))

    def player_jump(self):
        # when player is jumping and is not finished
        if self._player_jumping and self._player_jump_frames < JUMP_FRAMES:
            # turn off gravity
            self._player_gravity = False

            if self._player_jump_frames < JUMP_FRAMES / 2:
                # move player up if it is less than halfway through
                self._player[0].move((0, -JUMP_PATH[self._player_jump_frames]))
            else:
                # otherwise move player down
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

        # when gravity is on, player is in the air, and is not jumping
        if (
            self._player_gravity
            and player_bbox[3] < window_height
            and not self._player_jumping
        ):
            # make the player fall by GRAVITY pixels
            player.move((0, GRAVITY))

        # when player is stuck
        if self._player_stuck:
            # move it with the rest of the sprites
            player.move((-SPEED, 0))

        # when player is below the bottom of the window
        if player_bbox[3] > window_height:
            # move it up to to bottom
            player.teleport(
                (
                    player_bbox[0],
                    window_height - (player_bbox[3] - player_bbox[1]),
                )
            )

        # when the player exits the screen from the right
        if player_bbox[2] <= 0:
            # end the game
            self._end = True
            # player is dead
            self._player_dead = True

    def collide(self):
        # reset player gravity
        self._player_stuck = False
        # reset player stuck
        self._player_gravity = True

        for item in self._player[0].collide():
            # end the game when player collides into an obstacle
            if item in self._obstacles_tags:
                self._player_dead = True
                self._end = True

            if item in self._surfaces_tags:
                # bounding box for the collided surface
                surface = self._surfaces[self._surfaces_tags.index(item)].bbox()
                # bounding box for player
                player = self._player[0].bbox()

                if player[2] >= surface[0] and player[0] < surface[0]:
                    # player is blocked by the surface and not completely in it

                    # make sure player is not in surface by moving it out
                    self._player[0].teleport(
                        (surface[0] - (player[2] - player[0]), player[1])
                    )

                    # player is stuck
                    self._player_stuck = True
                elif player[3] >= surface[1]:
                    # player is on the surface

                    # turn off gravity to prevent falling
                    self._player_gravity = False

                    if player[3] < surface[3] and player[1] < surface[1]:
                        # player is on top of surface

                        # make sure player is not in surface by moving it up
                        self._player[0].teleport(
                            (player[0], surface[1] - (player[3] - player[1]))
                        )
                    else:
                        # player is below or completely inside surface

                        # stop jumping if player was below
                        self._player_jumping = False
                        # then turn on gravity
                        self._player_gravity = True

                        # make sure player is not in surface by moving it down
                        self._player[0].teleport((player[0], surface[3]))

            if item in self._rewards_tags:
                # destroy reward if player collided with it
                reward = self._rewards[self._rewards_tags.index(item)]
                reward.delete()
                # give the player one point
                self._player_points += 1
                # remove the reward from rewards
                del self._rewards[self._rewards_tags.index(item)]
                # remove the reward tag form reward tags
                del self._rewards_tags[self._rewards_tags.index(item)]

            if item in self._goal_tag:
                # end game on contact with the goal
                self._end = True
