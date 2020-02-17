class Obstacle(object):
    def __init__(self, game, position, dimensions, fill, outline):
        self.game = game
        self.canvas = game._canvas
        self.position = position
        self.dimensions = dimensions
        self.fill = fill
        self.outline = outline
        self.tag = None
        self.collide = False
        self.out = False
        self.draw()

    def draw(self):
        self.tag = self.canvas.create_rectangle(
            *self.position,
            *self.dimensions,
            fill=self.fill,
            outline=self.outline
        )

    def move_by(self, new_position):
        self.position[0] += new_position[0]
        self.position[1] += new_position[1]
        self.canvas.move(self.tag, *new_position)

    def move_to(self, new_position):
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]
        self.canvas.coords(self.tag, *self.position, self.dimensions[0] + self.position[0], self.dimensions[1] + self.position[1])

    def check_out(self):
        if self.position[0] + self.dimensions[0] <= 0 or self.position[1] + self.dimensions[1] <= 0:
            self.out = True
