import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_xboard("/home/pi/sunfish/xboard.py")
board = chess.Board()

while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(time=1.0))
    board.push(result.move)
    print(board)

print(board.result())
engine.quit()
