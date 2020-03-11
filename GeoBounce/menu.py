class Menu(object):
    def __init__(self, items, is_open=True):
        self._items = items
        self.is_open = is_open
    def on_click(self, click_pos):
        if self.is_open: # Double check that the menu is open
            for item in self._items:
                if item.on_click(click_pos):
                    break
    def menu_focus(self):
        self.is_open = True
    def menu_defocus(self):
        self.is_open = False
    def draw(self):
        # Fill background color
        for item in self._items:
            item.draw()

class MenuItem(object):
    def __init__(self, game, title, action, coords, dimensions, fill="#00ff00", color="#000000", outline="#000000", font=("Monospace",12,"")):
        self._game = game
        self._title = action
        self._action = action
        self._coords = coords
        self._dimensions = dimensions
        self._fill = fill
        self._color = color
        self._outline = outline
        self._font = font
        self._tag = None
    def on_click(self, click_pos):
        if self._coords[0] < click_pos[0] < (self._coords[0] + self._dimensions[0]) and self._coords[1] < click_pos[1] < (self._coords[1] + self._dimensions[1]):
            self._action()
            return True
        else:
            return False
    def draw(self):
        self._tag = self._game._canvas.create_rectangle(
            self._coords[0],
            self._coords[1],
            self._dimensions[0] + self._coords[0],
            self._dimensions[1] + self._coords[1],
            fill=self._fill,
            outline=self._outline
        )
        # Draw text (Don't have time today, have to commit changes
        )