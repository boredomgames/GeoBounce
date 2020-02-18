class Sprite(object):
    def __init__(self, game, position, dimensions, color):
        self._game = game
        self._position = position
        self._dimensions = dimensions
        self._color = color
        self._tag = None

    def draw(self):
        self._tag = self._game._canvas.create_rectangle(
            *self._position,
            *[x + y for x, y in zip(self._position, self._dimensions)],
            fill=self._color,
            outline=self._color,
        )

    def move(self, new_position):
        self._position[0] += new_position[0]
        self._position[1] += new_position[1]
        self._game._canvas.move(self._tag, *new_position)

    def teleport(self, new_position):
        self._position[0] = new_position[0]
        self._position[1] = new_position[1]
        self._game._canvas.coords(
            self._tag,
            *self._position,
            *[x + y for x, y in zip(self._position, self._dimensions)],
        )

    def collide(self):
        return self._game._canvas.find_overlapping(
            *self._position,
            *[x + y for x, y in zip(self._position, self._dimensions)],
        )

    def delete(self):
        self._game._canvas.delete(self._tag)


class Obstacle(Sprite):
    def __init__(self, game, position, dimensions, color):
        super().__init__(game, position, dimensions, color)


class Surface(Sprite):
    def __init__(self, game, position, dimensions, color):
        super().__init__(game, position, dimensions, color)


class Reward(Sprite):
    def __init__(self, game, position, dimensions, color):
        super().__init__(game, position, dimensions, color)


class Player(Sprite):
    def __init__(self, game, position, dimensions, color):
        super().__init__(game, position, dimensions, color)
        self.jumping = False
        self.jump_index = 0
        self.jump_path = [
            -23,
            -19,
            -15,
            -11,
            -10,
            -0,
            0,
            10,
            11,
            15,
            19,
            23,
        ]

        self._game.on("<space>")(lambda x: self.jump())

    def jump(self):
        self.jumping = True

    def run_jump(self):
        try:
            if self.jumping:
                self.move([0, self.jump_path[self.jump_index]])
                self.jump_index += 1
        except IndexError:
            self.jumping = False
            self.jump_index = 0
