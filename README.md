# Chessception
A chess and tic tac toe implementation which can be played using the Dobot robot arm!

Both games can make use of an AI. For chess this defaults to Stockfish, but this can be easily changed. Tic tac toe has its own negamax implementation representating a perfect player. The games can be played using one's microphone, a transcript is gained by using Google's API after which we deduce the move using a regular expression.

The games are either showed in a GUI or a TUI, using either unicode or ascii to represent the chess board state. The Dobot robot arm can make the movements for the games on an actual board, but the games can also be played using just a UI.

```
$ python sources/main.py --help
Usage: main.py [OPTIONS]

  A program to play chess with a robot arm and speech recognition.

Options:
  --ui [gui|tui]         [default: tui]
  --mic / --no-mic       [default: False]
  --arm / --no-arm       [default: False]
  --enc [unicode|ascii]  [default: ascii]
  --help                 Show this message and exit.
```
