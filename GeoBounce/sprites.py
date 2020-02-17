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

    def collide(self):
        return self._game._canvas.find_overlapping(
            *self._position,
            *[x + y for x, y in zip(self._position, self._dimensions)],
        )


class Obstacle(Sprite):
    def __init__(self, game, position, dimensions, color):
        super().__init__(game, position, dimensions, color)


class Item(Sprite):
    def __init__(self, game, position, dimensions, color):
        super().__init__(game, position, dimensions, color)


class Player(Sprite):
    def __init__(self, game, position, dimensions, color):
        super().__init__(game, position, dimensions, color)
        self.jumping = False
        self.jump_index = 0
        self.jump_path = [
            -15,
            -14,
            -13,
            -12,
            -11,
            -10,
            -9,
            -8,
            -7,
            -6,
            -5,
            -4,
            -3,
            -2,
            -1,
            -0,
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
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
