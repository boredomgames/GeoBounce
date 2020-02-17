from .game import Game


PLAYAREA_DIMENSIONS = [800, 600]

class PlayArea(Game):
    def __init__(self):
        super().__init__(dimensions=PLAYAREA_DIMENSIONS)
