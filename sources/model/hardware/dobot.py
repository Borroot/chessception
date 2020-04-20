

class Dobot:

    def __init__(self):
        pass  # TODO: Initialize the connection with the Arduino.

    def send_all(self, moves):
        for move in moves:
            self.send_one(move)

    def send_one(self, move):
        """
        Send a pairs of coordinates the dobot arm should move pieces to and from.
        """
        print(move)
        # Example input: [((0,3),(0,5))] = 'a2a4'.
        pass  # TODO: Send the coordinates to the Arduino.

    def move(self, game):
        """
        Receive a game and make the last move which correspond to the updated position, send these to the Arduino.
        Note that every game should have a stack with all the moves which can be used for this purpose.
        """
        raise NotImplementedError("Please implement this method.")

    def reset(self, game):
        """
        Move all the pieces back to their starting position.
        """
        raise NotImplementedError("Please implement this method.")
