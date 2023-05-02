from DebugUtilities.BeautifyDependency.GameBeautify import white_pieces_char, black_pieces_char
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PlayerDependency.PlayerSideDependency import PlayerSide
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import square_bitmask


def decryptFen(fen: str) -> [int, PlayerSide, list, int, int, list, int, int, Positions]:
    positional_fen, player_turn, castle_rights, enpassant_square, _, _ = fen.split(' ')
    game_board, white_board, white_pieces, black_board, black_pieces = __decrypt_boards(positional_fen)
    player_turn = __decrypt_player_turn(player_turn)
    white_castle, black_castle = __decrypt_castle_rights(castle_rights)
    enpassant_square_position = __decrypt_enpassant_square(enpassant_square)
    return game_board, player_turn, white_pieces, white_board, white_castle, black_pieces, black_board, black_castle, enpassant_square_position


def __decrypt_player_turn(player_turn: str) -> PlayerSide:
    return PlayerSide.WHITE if 'w' in player_turn.lower() else PlayerSide.BLACK


def __decrypt_castle_rights(castle_rights_str: str) -> [int, int]:
    white_castle, black_castle = 0, 0
    if '-' in castle_rights_str:
        return white_castle, black_castle
    for right in castle_rights_str:
        if right == 'K':
            white_castle = 0b1
        elif right == 'Q':
            white_castle |= 0b10
        elif right == 'k':
            black_castle = 0b1
        elif right == 'q':
            black_castle |= 0b10
    return white_castle, black_castle


def __decrypt_enpassant_square(enpassant_square: str) -> Positions:
    enpassant_square_position = Positions.OUT_OF_BOUNDS
    if '-' not in enpassant_square:
        enpassant_square_position = Positions.__members__[enpassant_square]
    return enpassant_square_position


def __decrypt_boards(fen: str) -> [int, int, list, int, int]:
    row, col = 0, 0
    game_board = 0
    white_board, white_pieces = 0, [0 for _ in range(6)]
    black_board, black_pieces = 0, [0 for _ in range(6)]

    for c in fen:
        if c == '/':
            row += 1
            col = 0
        elif c.isdigit():
            col += int(c)
        else:
            square_mask = square_bitmask[row * 8 + col]
            game_board |= square_mask
            col += 1
            if c in white_pieces_char:
                white_board |= square_mask
                white_pieces[white_pieces_char.index(c)] |= square_mask
            else:
                black_board |= square_mask
                black_pieces[black_pieces_char.index(c)] |= square_mask
    return game_board, white_board, white_pieces, black_board, black_pieces
