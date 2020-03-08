from itertools import zip_longest
from PIL import Image as PILImage, ImageTk as PILImageTk


def rgb(red, green, blue):
    hex_digits = "0123456789ABCDEF"
    red1, red2 = divmod(red, 16)
    green1, green2 = divmod(green, 16)
    blue1, blue2 = divmod(blue, 16)

    return f'#{"".join(hex_digits[x] for x in (red1, red2, green1, green2, blue1, blue2))}'


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


class Image(object):
    def __init__(self, path, dimensions=(None, None)):
        self._image = PILImage.open(path)

        if tuple(dimensions) != (None, None):
            self.resize(dimensions)

        self._tkimage = PILImageTk.PhotoImage(self._image)

    def resize(self, dimensions):
        self._image = self._image.resize(dimensions)
        self._tkimage = PILImageTk.PhotoImage(self._image)

    def tkimage(self):
        return self._tkimage


class SpriteNext(object):
    def __init__(self, game, coords):
        self._game = game
        self._coords = list(coords)
        self._tag = None

    def call(self, command):  # unsafe?
        exec(f"self._game._canvas.({self._tag}, {command})")


class RectangleSprite(SpriteNext):
    def __init__(
        self, game, coords, dimensions, fill="#000000", outline="#000000"
    ):
        super().__init__(game, coords)

        self._dimensions = list(dimensions)
        self._fill = fill
        self._outline = outline

    def draw(self):
        self._tag = self._game._canvas.create_rectangle(
            self._coords[0],
            self._coords[1],
            self._dimensions[0] + self._coords[0],
            self._dimensions[1] + self._coords[1],
            fill=self._fill,
            outline=self._outline,
        )

    def move(self, coords):
        self._coords[0] += coords[0]
        self._coords[1] += coords[1]

        self._game._canvas.move(self._tag, *coords)

    def teleport(self, coords):
        self._coords[0] = coords[0]
        self._coords[1] = coords[1]

        self._game._canvas.coords(
            self._tag,
            self._coords[0],
            self._coords[1],
            self._dimensions[0] + self._coords[0],
            self._dimensions[1] + self._coords[1],
        )

    def collide(self):
        return self._game._canvas.find_overlapping(*self.bbox())

    def delete(self):
        self._game._canvas.delete(self._tag)
        self._tag = None

    def position(self):
        return self._coords

    def bbox(self):
        return (
            self._coords[0],
            self._coords[1],
            self._dimensions[0] + self._coords[0],
            self._dimensions[1] + self._coords[1],
        )


class ImageSprite(SpriteNext):
    def __init__(self, game, coords, dimensions, image):
        super().__init__(game, coords)

        self._dimensions = dimensions

        if isinstance(image, str):
            self._image = Image(image, dimensions=self._dimensions)
        else:
            self._image = image

    def draw(self):
        self._tag = self._game._canvas.create_image(
            self._coords,
            image=self._image.tkimage()
            if isinstance(self._image, Image)
            else self._image,
        )

    def move(self, coords):
        self._coords[0] += coords[0]
        self._coords[1] += coords[1]

        self._game._canvas.move(self._tag, *coords)

    def teleport(self, coords):
        self._coords[0] = coords[0]
        self._coords[1] = coords[1]

        self._game._canvas.coords(
            self._tag,
            self._coords[0],
            self._coords[1],
            self._dimensions[0] + self._coords[0],
            self._dimensions[1] + self._coords[1],
        )

    def collide(self):
        return self._game._canvas.find_overlapping(*self.bbox())

    def delete(self):
        self._game._canvas.delete(self._tag)
        self._tag = None

    def position(self):
        return self._coords

    def bbox(self):
        return (
            self._dimensions[0],
            self._dimensions[1],
            self._dimensions[0] + self._coords[0],
            self._dimensions[1] + self._coords[1],
        )


class OvalSprite(SpriteNext):
    def __init__(
        self, game, coords, dimensions, fill="#000000", outline="#000000"
    ):
        super().__init__(game, coords)

        self._dimensions = dimensions
        self._fill = fill
        self._outline = outline

    def draw(self):
        self._tag = self._game._canvas.create_rectangle(
            self._coords,
            [x[0] + x[1] for x in zip(self._dimensions, self._coords)],
            fill=self._fill,
            outline=self._outline,
        )

    def move(self, coords):
        self._coords[0] += coords[0]
        self._coords[1] += coords[1]

        self._game._canvas.move(self._tag, *coords)

    def teleport(self, coords):
        self._coords[0] = coords[0]
        self._coords[1] = coords[1]

        self._game._canvas.coords(
            self._tag,
            self._coords[0],
            self._coords[1],
            self._dimensions[0] + self._coords[0],
            self._dimensions[1] + self._coords[1],
        )

    def collide(self):
        return self._game._canvas.find_overlapping(*self.bbox())

    def delete(self):
        self._game._canvas.delete(self._tag)
        self._tag = None

    def position(self):
        return self._coords

    def bbox(self):
        return (
            self._dimensions[0],
            self._dimensions[1],
            self._dimensions[0] + self._coords[0],
            self._dimensions[1] + self._coords[1],
        )


class LineSprite(SpriteNext):
    def __init__(self, game, coords, width=1, fill="#000000"):
        super().__init__(game, coords)

        self._width = width
        self._fill = fill

    def draw(self):
        self._tag = self._game._canvas.create_line(
            self._coords, fill=self._fill
        )

    def move(self, coords):
        self._coords[0] += coords[0]
        self._coords[1] += coords[1]
        self._coords[2] += coords[0]
        self._coords[3] += coords[1]

        self._game._canvas.move(self._tag, *coords)

    def teleport(self, coords):
        x = min(self._coords[0], self._coords[2])
        y = min(self._coords[1], self._coords[3])

        self._coords[0] += coords[0] - x
        self._coords[1] += coords[1] - y
        self._coords[2] += coords[0] - x
        self._coords[3] += coords[1] - y

        self._game._canvas.move(self._tag, coords[0] - x, coords[1] - y)

    def collide(self):
        return self._game._canvas.find_overlapping(*self.bbox())

    def delete(self):
        self._game._canvas.delete(self._tag)
        self._tag = None

    def position(self):
        x = min(self._coords[0], self._coords[2])
        y = min(self._coords[1], self._coords[3])

        return (x, y)

    def bbox(self):
        x_min = min(self._coords[0], self._coords[2])
        y_min = min(self._coords[1], self._coords[3])
        x_max = max(self._coords[0], self._coords[2])
        y_max = max(self._coords[1], self._coords[3])

        return (x_min, y_min, x_max, y_max)


class PolygonSprite(SpriteNext):
    def __init__(self, game, coords, fill="#000000", outline="#000000"):
        super().__init__(game, coords)

        self._fill = fill
        self._outline = outline

    def draw(self):
        self._tag = self._game._canvas.create_polygon(
            self._coords, fill=self._fill, outline=self._outline
        )

    def move(self, coords):
        coords_new = []

        for x, y in grouper(self._coords, 2):
            coords_new.append(x + coords[0])
            coords_new.append(y + coords[1])

        self._coords = coords_new

        self._game._canvas.move(self._tag, *coords)

    def teleport(self, coords):
        coords_new = []

        x = min(item[0] for item in grouper(self._coords, 2))
        y = min(item[0] for item in grouper(self._coords, 2))

        for x_item, y_item in grouper(self._coords, 2):
            coords_new.append(x_item + (coords[0] - x))
            coords_new.append(y_item + (coords[1] - x))

        self._coords = coords_new

        self._game._canvas.coords(self._tag, *coords_new)

    def collide(self):
        return self._game._canvas.find_overlapping(*self.bbox())

    def position(self):
        x = min(item[0] for item in grouper(self._coords, 2))
        y = min(item[0] for item in grouper(self._coords, 2))

        return (x, y)

    def bbox(self):
        x_min = min(item[0] for item in grouper(self._coords, 2))
        y_min = min(item[0] for item in grouper(self._coords, 2))
        x_max = max(item[0] for item in grouper(self._coords, 2))
        y_max = max(item[0] for item in grouper(self._coords, 2))

        return (x_min, y_min, x_max, y_max)


class Sprite(object):
    def __init__(
        self, game, coords, dimensions, type_="rectangle", color="black"
    ):
        self._game = game
        self._coords = coords
        self._dimensions = dimensions
        self._type = type
        self._color = color
        self._tag = None

    def draw(self):
        self._tag = self._game._canvas.create_rectangle(
            *self._coords,
            *[x + y for x, y in zip(self._coords, self._dimensions)],
            fill=self._color,
            outline=self._color,
        )

    def move(self, new_position):
        self._coords[0] += new_position[0]
        self._coords[1] += new_position[1]
        self._game._canvas.move(self._tag, *new_position)

    def teleport(self, new_position):
        self._coords[0] = new_position[0]
        self._coords[1] = new_position[1]
        self._game._canvas.coords(
            self._tag,
            *self._coords,
            *[x + y for x, y in zip(self._coords, self._dimensions)],
        )

    def collide(self):
        return self._game._canvas.find_overlapping(
            *self._coords,
            *[x + y for x, y in zip(self._coords, self._dimensions)],
        )

    def delete(self):
        self._game._canvas.delete(self._tag)


class Obstacle(Sprite):
    def __init__(self, game, position, dimensions, color):
        super().__init__(game, position, dimensions=dimensions, color=color)


class Surface(Sprite):
    def __init__(self, game, position, dimensions, color):
        super().__init__(game, position, dimensions=dimensions, color=color)


class Reward(Sprite):
    def __init__(self, game, position, dimensions, color):
        super().__init__(game, position, dimensions=dimensions, color=color)


class Player(Sprite):
    def __init__(self, game, position, dimensions, color):
        super().__init__(game, position, dimensions=dimensions, color=color)
        self.jumping = False
        self.jump_index = 0
        # low
        # self.jump_path = [-23, -19, -15, -11, -10, -0, 0, 10, 11, 15, 19, 23]
        # high
        self.jump_path = [
            -12,
            -11,
            -10,
            -9,
            -8,
            -7,
            -6,
            -5,
            -5,
            -5,
            -0,
            0,
            5,
            5,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
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
