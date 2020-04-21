class ResignException(Exception):
    pass


class DrawOfferException(Exception):
    pass


class Game:

    NUM_LEVELS = NotImplementedError("Please implement this variable.")
    NUM_PLAYERS = NotImplementedError("Please implement this variable.")

    def show_state(self):
        raise NotImplementedError("Please implement this method.")

    def state(self):
        raise NotImplementedError("Please implement this method.")

    def move(self, move):
        """
        Make the move and update the state.
        :param move: The move to be made.
        :raises ValueError: If the move is invalid.
        """
        raise NotImplementedError("Please implement this method.")

    def next(self, onturn, players):
        return (onturn + 1) % len(players)
    
    def game_over(self):
        raise NotImplementedError("Please implement this method.")

    def winner(self, players):
        """
        This function assumes that it is already checked that the game is over.
        :return: The winner (Player) or None.
        """
        raise NotImplementedError("Please implement this method.")

    def get_ai(self, color, level):
        raise NotImplementedError("Please implement this method.")

    def get_speech(self):
        raise NotImplementedError("Please implement this method.")

    def get_dobot(self):
        raise NotImplementedError("Please implement this method.")
