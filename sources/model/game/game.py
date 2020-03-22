class ResignException(Exception):
    pass


class DrawOfferException(Exception):
    pass


class Game:

    def state(self):
        raise NotImplementedError("Please implement this method.")

    def move(self, move):
        raise NotImplementedError("Please implement this method.")

    def other(self, onturn, white, black):
        return white if onturn == black else black
    
    def game_over(self):
        raise NotImplementedError("Please implement this method.")

    def winner(self, white, black):
        raise NotImplementedError("Please implement this method.")
