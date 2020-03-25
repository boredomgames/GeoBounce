from kivy.app import App

GAME_DIMENSIONS = [800, 600]
GAME_RESIZABLE = False
GAME_NAME = "GeoBounce"


class Game(object):
    def __init__(self):
        self._name = GAME_NAME
        self._dimensions = GAME_DIMENSIONS
        self._resizable = GAME_RESIZABLE

        self._window = App()

    def play(self):
        self._window.build()
        self._window.run()
