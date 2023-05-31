class Fen:
    def __init__(self, game_board, player_turn, white_pieces, white_board, white_castle, black_pieces, black_board,
                 black_castle, enpassant_square_position):
        self.game_board = game_board
        self.player_turn = player_turn
        self.white_pieces = white_pieces
        self.white_board = white_board
        self.white_castle = white_castle
        self.black_pieces = black_pieces
        self.black_board = black_board
        self.black_castle = black_castle
        self.enpassant_square_position = enpassant_square_position
