import serial
import time

class Dobot:
    """
    This class represents the direct connection and communication between Arduino/Dobot and RPI
    """
    _SERIAL_PORT_PATH = '/dev/ttyACM0'

    def __init__(self, id):
        self._serial_port = serial.Serial('/dev/ttyACM0', 115200)
        self._init_serial(id)

    def send_all(self, moves):
        """
        Send all moves to Dobot/Arduino that need to be executed in this turn.
        Before sending the moves, first send the number of moves that are going to be sent.
        """
        sendMoves = "<" + str(len(moves)) + ">"
        movesProcessed = False
        self._serial_port.write(sendMoves.encode())
        for move in moves:
            self.send_one(move)
        # wait for arduino to process the move(s)
        while not movesProcessed:
            if self._serial_port.in_waiting > 0:
                line = self._serial_port.readline().decode('ascii').rstrip()
                if line == "Finished":
                    print("Move processed")
                    movesProcessed = True

    def send_one(self, move):
        """
        Send a pairs of coordinates the dobot arm should move pieces to and from.
        """
        print(move)
        # Example input: [((0,3),(0,5))] = 'a2a4'.
        for i in range(0, 2):
            for j in range(0, 2):
                moveString = "<" + str(move[i][j]) + ">"
                self._serial_port.write(moveString.encode('ascii'))

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

    def _init_serial(self, gameID):
        """
        Initialize serial communication with Arduino.
        """
        arduinoReady = False
        print("Starting serial initialization")
        while not arduinoReady:
            if self._serial_port.in_waiting > 0:
                line = self._serial_port.readline().decode('ascii').rstrip()
                print(line)
                if line == "Ready":
                    arduinoReady = True
        firstContact = "<" + str(gameID) + ">"
        self._serial_port.write(firstContact.encode('ascii'))
        time.sleep(4)
