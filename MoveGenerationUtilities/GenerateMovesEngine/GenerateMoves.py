from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName
from DebugUtilities.GameDependency.PlayerDependency.PlayerSideDependency import PlayerSide
from MoveGenerationUtilities.Const import before_top_edge, before_bottom_edge
from MoveGenerationUtilities.EncryptionDependency.MoveEncryptions.EncodeMove import encode_move
from MoveGenerationUtilities.GenerateMovesEngine.GenerateMovesDependencies import *
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import unsigned
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import square_bitmask


def getMoves(board_state: int, white_state: int, black_state: int, white_pieces: list, black_pieces: list,
             turn: PlayerSide, white_castle_rights: int, black_castle_rights: int, enpassant_square: Positions,
             previous_move: int) -> list:
    # moves list
    player_moves = []
    # decide opponent and player pieces
    player_pieces, player_side, opponent_pieces, opponent_side = get_player_wise_pieces_and_sides(
        white_pieces=white_pieces, black_pieces=black_pieces, turn=turn)
    # get the bitmask of player's king
    player_king_mask = player_pieces[PieceName.KING.value]
    player_king_pos: Positions = Positions(get_least_bit_index(player_king_mask))
    # king_rays: int = rook
    # get the sliding pieces of opponent
    opponent_sliding_pieces = get_sliding_pieces(piece_list=opponent_pieces)
    # get opponent attack mask, no of checks and the list of attackers as (Name, Position)
    opponent_attacks, check_count, attackers = get_opponent_attacks_and_find_check(opponent_pieces=opponent_pieces,
                                                                                   player_king_mask=player_king_mask,
                                                                                   opponent_side=opponent_side,
                                                                                   board_state=board_state)
    # ===================================white specific moves===================================
    if turn == PlayerSide.WHITE and check_count < 2:
        pawn = white_pieces[int(PieceName.PAWN.value)]
        # ===================================pawn moves===================================
        while pawn:
            # Position and mask of pawn's position
            pawn_position: Positions = Positions(get_least_bit_index(pawn))
            pawn_positional_mask: int = square_bitmask[pawn_position.value]
            # If the move is promotion move
            promotion: bool = bool(pawn_positional_mask & before_top_edge)
            # get pawn attack map and validate it
            pawn_attack_map = pawn_attack_maps[PlayerSide.WHITE.value][pawn_position.value]
            pawn_attack_map &= black_state
            # generate pawn quite move and validate it
            quite_move: int = pawn_positional_mask >> 8
            quite_move &= unsigned(~board_state)
            # generate pawn double push move and validate it
            double_push_move: int = 0
            if pawn_positional_mask & before_bottom_edge:
                double_push_move: int = pawn_positional_mask >> 16
                double_push_move &= unsigned(~board_state)
            # get enpassant move
            enpassant_move: Positions = get_enpassant_move(enpassant_square=enpassant_square,
                                                           previous_move=previous_move)
            # set piece limit if the move is promotion one
            piece_length = list(PieceName)[1:5] if promotion else list(PieceName)[0:1]
            # ===================================pawn attack moves===================================
            while pawn_attack_map:
                # get attack square as Position
                attack_square: Positions = Positions(get_least_bit_index(pawn_attack_map))
                # store moves for attack promotion or normal attack moves
                for piece_name in piece_length:
                    player_moves.append(
                        encode_move(source_square=pawn_position,
                                    target_square=attack_square,
                                    piece_name=PieceName.PAWN,
                                    promotion_piece_name=piece_name if promotion else PieceName.NONE,
                                    capture_flag=True,
                                    double_push_flag=False,
                                    enpassant_flag=False,
                                    castle_flag=False))
                pawn_attack_map &= pawn_attack_map - 1
            # ===================================pawn quite & double push===================================
            # get quite move as Positions
            quite_move: Positions = Positions(get_least_bit_index(quite_move))
            # if quite move exists
            if quite_move != Positions.OUT_OF_BOUNDS:
                # store moves for promotion or quite moves
                for piece_name in piece_length:
                    player_moves.append(
                        encode_move(source_square=pawn_position,
                                    target_square=quite_move,
                                    piece_name=PieceName.PAWN,
                                    promotion_piece_name=piece_name if promotion else PieceName.NONE,
                                    capture_flag=False,
                                    double_push_flag=False,
                                    enpassant_flag=False,
                                    castle_flag=False))
                # get double push as Positions
                double_push_move: Positions = Positions(get_least_bit_index(double_push_move))
                # if double push exists
                if double_push_move != Positions.OUT_OF_BOUNDS:
                    # store move as double push move
                    player_moves.append(
                        encode_move(source_square=pawn_position,
                                    target_square=double_push_move,
                                    piece_name=PieceName.PAWN,
                                    promotion_piece_name=PieceName.NONE,
                                    capture_flag=False,
                                    double_push_flag=True,
                                    enpassant_flag=False,
                                    castle_flag=False))
                # ===================================enpassant move===================================
                # if enpassant exists
                if enpassant_move != Positions.OUT_OF_BOUNDS:
                    possible_opponent_position: Positions = Positions(enpassant_move.value + 8)
                    # create mask of opponent position w.r.t enpassant square
                    possible_opponent_position_mask: int = square_bitmask[possible_opponent_position.value]
                    # if piece exists at location and difference btw opponent and player piece position is 1
                    if (possible_opponent_position_mask & opponent_pieces[
                        PieceName.PAWN.value]) and (
                            abs(pawn_position.value - possible_opponent_position.value) == 1):
                        # add enpassant move into the list
                        player_moves.append(
                            encode_move(source_square=pawn_position,
                                        target_square=enpassant_move,
                                        piece_name=PieceName.PAWN,
                                        promotion_piece_name=PieceName.NONE,
                                        capture_flag=False,
                                        double_push_flag=False,
                                        enpassant_flag=True,
                                        castle_flag=False))
            pawn &= pawn - 1
    return player_moves
