class ResignException(Exception):
    pass


class DrawOfferException(Exception):
    pass


class Game:

    def state(self):
        raise NotImplementedError("Please implement this method.")

    def move(self, move):
        """
        Make the move and update the state.
        :param move: The move to be made.
        :raises ValueError: If the move is invalid.
        """
        raise NotImplementedError("Please implement this method.")

    def other(self, onturn, white, black):
        return white if onturn == black else black
    
    def game_over(self):
        raise NotImplementedError("Please implement this method.")

    def winner(self, white, black):
        raise NotImplementedError("Please implement this method.")

    def get_ai(self, color, level):
        raise NotImplementedError("Please implement this method.")

    def get_speech(self):
        raise NotImplementedError("Please implement this method.")

    def get_dobot(self):
        raise NotImplementedError("Please implement this method.")
