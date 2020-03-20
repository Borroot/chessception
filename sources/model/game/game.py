import chess


class ResignException(Exception):
    pass


class DrawOfferException(Exception):
    pass


def _winner(board, white, black):
    result = board.result()
    if result == '1-0':
        return white
    if result == '0-1':
        return black
    if result == '1/2-1/2':
        return None


def _other(onturn, white, black):
    return white if onturn == black else black


def _move(self, board, player):
    self._ui.info_onturn(player)
    move = player.move(board)

    if move in board.legal_moves:
        board.push(move)
    else:
        self._ui.info_illegal(move)
        self._move(board, player)

    self._ui.info_board(board)


def _game(self, white, black):
    board = chess.Board()
    onturn = white

    with white, black:
        self._ui.info_board(board)
        while not board.is_game_over():
            try:
                self._move(board, onturn)
                onturn = self._other(onturn, white, black)
            except ResignException:
                return self._other(onturn, white, black)
            except DrawOfferException:
                if self._other(onturn, white, black).draw_offer():
                    return None

    return self._winner(board, white, black)
