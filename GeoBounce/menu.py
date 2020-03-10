class StartMenu(object):
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

class MenuItem(object):
    def __init__(self, title, action, location, size):
        self._title = action
        self._action = action
        self._location = location
        self._size = size
    def on_click(self, click_pos):
        if self._location[0] < click_pos[0] < (self._location[0] + self._size[0]) and self._location[1] < click_pos[1] < (self._location[1] + self._size[1]):
            self._action()
            return True
        else:
            return False