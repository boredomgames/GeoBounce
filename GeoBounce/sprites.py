class GeoBox(object):
    def __init__(self, canvas, position):
        self.canvas = canvas
        self.position = list(position)
        self.tag = None
        self.draw()

    def draw(self):
        self.tag = self.canvas.create_rectangle(
            *self.position,
            50,
            50,
            fill="blue",
            outline="blue",
        ) # x, y, width, height

    def move_by(self, new_position):
        self.position[0] += new_position[0]
        self.position[1] += new_position[1]
        self.canvas.move(self.tag, *new_position)

    def move_to(self, new_position):
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]
        self.canvas.coords(self.tag, *self.position, 50, 50)
