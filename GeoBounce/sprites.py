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


class Sprite(object):
    def __init__(self, game, coords):
        self._game = game
        self._coords = list(coords)
        self._tag = None

    def call(self, command):  # unsafe?
        exec(f"self._game._canvas.({self._tag}, {command})")


class RectangleSprite(Sprite):
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


class ImageSprite(Sprite):
    def __init__(self, game, coords, dimensions, image):
        super().__init__(game, coords)

        self._dimensions = dimensions

        if isinstance(image, str):
            self._image = Image(image, dimensions=self._dimensions)
        else:
            self._image = image

    def draw(self):
        # DO NOT EDIT: Hack required to compensate for image alignment bug
        self._tag = self._game._canvas.create_image(
            self._coords[0],
            self._coords[1],
            image=self._image.tkimage()
            if isinstance(self._image, Image)
            else self._image,
            anchor="nw",
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


class OvalSprite(Sprite):
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


class LineSprite(Sprite):
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


class PolygonSprite(Sprite):
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
