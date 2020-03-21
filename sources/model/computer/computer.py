class Computer:
    """
    This abstract class describes a computer player.
    """

    def __init__(self):
        self._level = None

    def set_level(self, level):
        self._level = level

    def move(self, board):
        raise NotImplementedError("Please implement this method.")

    def close(self):
        raise NotImplementedError("Please implement this method.")
