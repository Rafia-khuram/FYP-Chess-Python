from DebugUtilities.GameDependencies import Positions, PieceName, PlayerSide
from MoveGenerationUtilities.Encryptions.EnumAttributes import MoveDecodeAttributes
from MoveGenerationUtilities.Encryptions.moveEncryption import decode_move
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Bishop import get_bishop_attacks
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Queen import get_queen_attacks
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Rook import get_rook_attacks
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import get_least_bit_index

from MoveGenerationUtilities.PreCalculations.PreCalculationsData import pawn_attack_maps, knight_attack_maps, \
    king_attack_maps


def get_opponent_attacks_and_find_check(opponent_pieces: list, player_king_mask: int, opponent_side: int,
                                        board_state: int) -> [int, int, list]:
    opponent_attacks: int = 0
    attackers = []
    check_count: int = 0
    for piece_name in list(PieceName)[:-1]:
        opponent_piece_mask: int = opponent_pieces[piece_name.value]
        while opponent_piece_mask:
            piece_position: Positions = Positions(get_least_bit_index(opponent_piece_mask))
            piece_attacks: int = 0
            if piece_name == PieceName.PAWN.value:
                piece_attacks: int = pawn_attack_maps[opponent_side][piece_position.value]
            elif piece_name == PieceName.KNIGHT.value:
                piece_attacks: int = knight_attack_maps[piece_position.value]
            elif piece_name == PieceName.BISHOP.value:
                piece_attacks: int = get_bishop_attacks(piece_position.value, board_state)
            elif piece_name == PieceName.ROOK.value:
                piece_attacks: int = get_rook_attacks(piece_position.value, board_state)
            elif piece_name == PieceName.QUEEN.value:
                piece_attacks: int = get_queen_attacks(piece_position.value, board_state)
            elif piece_name == PieceName.KING.value:
                piece_attacks: int = king_attack_maps[piece_position.value]
            opponent_attacks |= piece_attacks
            if piece_attacks & player_king_mask:
                check_count += 1
                attackers.append((piece_position, piece_name))
            opponent_piece_mask &= opponent_piece_mask - 1
    return opponent_attacks, check_count, attackers


def get_sliding_pieces(piece_list: list) -> int:
    return piece_list[PieceName.BISHOP.value] | piece_list[PieceName.ROOK.value] | \
           piece_list[PieceName.QUEEN.value]


def get_player_wise_pieces_and_sides(white_pieces: list, black_pieces: list, turn: PlayerSide) -> [list, PlayerSide,
                                                                                                   list, PlayerSide]:
    return [black_pieces, PlayerSide.BLACK, white_pieces, PlayerSide.WHITE] if turn == PlayerSide.BLACK else \
        [white_pieces, PlayerSide.WHITE, black_pieces, PlayerSide.BLACK]


def get_enpassant_move(enpassant_square: Positions, previous_move: int) -> Positions:
    if enpassant_square != Positions.OUT_OF_BOUNDS:
        return enpassant_square
    if decode_move(previous_move, MoveDecodeAttributes.DOUBLE_PUSH_FLAG):
        source_square = decode_move(previous_move, MoveDecodeAttributes.SOURCE_SQUARE)
        target_square = decode_move(previous_move, MoveDecodeAttributes.TARGET_SQUARE)
        return Positions((source_square + target_square) / 2)
    return Positions.OUT_OF_BOUNDS
