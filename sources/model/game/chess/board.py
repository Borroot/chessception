import chess


class Board(chess.Board):

    def __init__(self, unicode, invert):
        super().__init__()
        self._unicode = unicode
        self._invert = invert

    def __str__(self):
        if self._unicode:
            return self.unicode(invert_color=self._invert)
        else:
            return super().__str__()
