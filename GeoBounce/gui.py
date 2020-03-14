BUTTON_STYLE = {
    "dimensions": [100, 50],
    "fill": "white",
    "outline": "black",
    "color": "black",
    "hover_fill": "gray",
    "hover_outline": "gray",
    "hover_color": "white",
    "active_fill": "black",
    "active_outline": "black",
    "active_color": "white",
    "font_family": "TkDefaultFont",
    "font_size": 14,
}

LABEL_STYLE = {
    "color": "black",
    "font_family": "TkDefaultFont",
    "font_size": 14,
}

class Label(object):
    def __init__(self, text, style={}):
        self._text = text
        self._tag = None
        self._style = {**LABEL_STYLE, **style}

    def draw(self, game, coords):
        color = self._style["color"]
        font_family = self._style["font_family"]
        font_size = self._style["font_size"]

        self._tag = game._canvas.create_text(
            coords,
            fill=color,
            font=f"{font_family} {font_size}",
            text=self._text,
            justify="center",
            anchor="center",
        )

    def delete(self, game):
        game._canvas.delete(self._tag)

        self._tag = None


class Button(object):
    def __init__(self, text, command=lambda: None, style={}):
        self._text = text
        self._command = command
        self._tag = None
        self._tag_text = None
        self._focused = False
        self._style = {**BUTTON_STYLE, **style}

    def draw(self, game, coords):
        fill = self._style["fill"]
        outline = self._style["outline"]
        color = self._style["color"]
        dimensions = self._style["dimensions"]
        hover_fill = self._style["hover_fill"]
        hover_outline = self._style["hover_outline"]
        hover_color = self._style["hover_color"]
        active_fill = self._style["active_fill"]
        active_outline = self._style["active_outline"]
        active_color = self._style["active_color"]
        font_family = self._style["font_family"]
        font_size = self._style["font_size"]

        self._tag = game._canvas.create_rectangle(
            coords[0],
            coords[1],
            coords[0] + dimensions[0],
            coords[1] + dimensions[1],
            fill=fill,
            outline=outline
        )

        self._tag_text = game._canvas.create_text(
            dimensions[0] / 2 + coords[0],
            dimensions[1] / 2 + coords[1],
            fill=color,
            text=self._text,
            font=f"{font_family} {font_size}",
        )

        def hover(event):
            game._canvas.itemconfig(self._tag, fill=hover_fill, outline=hover_outline)
            game._canvas.itemconfig(self._tag_text, fill=hover_color)

            self._focused = True

        game.on("<Enter>", tag=self._tag)(hover)
        game.on("<Enter>", tag=self._tag_text)(hover)

        def active(event):
            game._canvas.itemconfig(self._tag, fill=active_fill, outline=active_outline)
            game._canvas.itemconfig(self._tag_text, fill=active_color)

        game.on("<Button-1>", tag=self._tag)(active)
        game.on("<Button-1>", tag=self._tag_text)(active)

        def blur(event):
            game._canvas.itemconfig(self._tag, fill=fill, outline=outline)
            game._canvas.itemconfig(self._tag_text, fill=color)

            self._focused = False

        game.on("<Leave>", tag=self._tag)(blur)
        game.on("<Leave>", tag=self._tag_text)(blur)

        def press(event):
            if self._focused:
                self._command(event)

        game.on("<ButtonRelease-1>", tag=self._tag)(press)
        game.on("<ButtonRelease-1>", tag=self._tag_text)(press)

    def delete(self, game):
        game._canvas.delete(self._tag)
        game._canvas.delete(self._tag_text)

        self._tag = None
        self._tag_text = None


class GUI(object):
    def __init__(self, game, coords, dimensions, widgets):
        self._game = game
        self._coords = coords
        self._dimensions = dimensions
        self._widgets = widgets

    def add_row(self, row=[]):
        self._widgets.append(row)

    def add_widget(self, row, widget):
        self._widgets[row].append(widget)

    def draw(self):
        # BAD CODE: Cleanup

        row_height = self._dimensions[1] / len(self._widgets)

        for row_number, row in enumerate(self._widgets):
            widget_width = self._dimensions[0] / len(row)

            for widget_number, widget in enumerate(row):
                try:
                    widget.draw(
                        self._game,
                        (
                            widget_width * widget_number + self._coords[0] + ((widget_width / 2) - (widget._style["dimensions"][0] / 2)),
                            row_height * row_number + self._coords[1] + ((row_height / 2) - (widget._style["dimensions"][1] / 2)),
                        )
                    )
                except KeyError:
                    widget.draw(
                        self._game,
                        (
                            widget_width * widget_number + self._coords[0] + (widget_width / 2),
                            row_height * row_number + self._coords[1] + (row_height / 2),
                        )
                    )

    def delete(self):
        for row in self._widgets:
            for widget in row:
                widget.delete(self._game)
