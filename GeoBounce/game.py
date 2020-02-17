from tkinter import Tk, Canvas

GAME_DIMENSIONS = [800, 600]
GAME_RESIZABLE = False
GAME_NAME = "GeoBounce"


class Game(object):
    def __init__(self):
        # variables are to be synced with Tk window, DO NOT CHANGE DIRECTLY
        self._name = GAME_NAME
        self._dimensions = GAME_DIMENSIONS
        self._resizable = GAME_RESIZABLE

        # initialize tkinter window
        self._window = Tk()
        # self._window.overrideredirect(True)  # probably not needed
        self._window.withdraw()
        self._window.title(self._name)
        self._window.geometry(f"{self._dimensions[0]}x{self._dimensions[1]}")
        self._window.resizable(self._resizable, self._resizable)

        # initialize canvas to fill window
        self._canvas = Canvas(self._window, highlightthickness=0)
        self._canvas.pack(anchor="center", fill="both", expand=True)

        # watch window resize
        @self.on(event="<Configure>")
        def resize(*args):
            x = []
            y = []
            append_to = "x"

            for item in self._window.geometry():
                if item == "x":
                    append_to = "y"
                    continue
                elif not item.isdigit():
                    break

                if append_to == "x":
                    x.append(item)
                elif append_to == "y":
                    y.append(item)

            self._dimensions = [int("".join(x)), int("".join(y))]

        # make sure everything is drawn
        self.update()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        try:
            # make sure the name can be stringified
            self._name = str(value)
            # set the window title to name automatically
            self._window.title(self._name)
        except ValueError:
            raise ValueError("name must be a string") from None

        self.update()

    @property
    def dimensions(self):
        return self._dimensions

    @dimensions.setter
    def dimensions(self, value):  # value is width by height
        if value[0] < 0 or value[1] < 0:  # make sure value is positive
            raise ValueError("dimensions cannot be negative")

        try:
            # make sure value is an integer
            self._dimensions = [int(str(value[0])), int(str(value[1]))]
            # set the window dimensions automatically
            self._window.geometry(
                f"{self._dimensions[0]}x{self._dimensions[1]}"
            )
        except ValueError:
            raise ValueError("dimensions must be integers") from None

        self.update()

    @property
    def resizable(self):
        return self._resizable

    @resizable.setter
    def resizable(self, value):
        try:
            # make sure value is a boolean
            self._resizable = bool(value)
            # set the window resizable automatically
            self._window.resizable(self._resizable, self._resizable)
        except ValueError:
            raise ValueError("resizable must be booleans") from None

        self.update()

    def update(self):
        self._window.update_idletasks()
        self._window.update()

    def play(self, loop=False):
        # self._window.overrideredirect(False)  # probably not needed
        self._window.deiconify()
        self._canvas.focus_set()
        self.update()

        if loop:
            self._window.mainloop()

    def terminate(self):
        self._window.destroy()

    def on(self, event, tag=None):
        def bind_event(function):
            if tag is None:
                self._canvas.bind(event, function)
            else:
                self._canvas.tag_bind(tag, event, function)

        return bind_event
