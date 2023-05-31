from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName
from FenUtilities.FenModel import Fen
from MoveGenerationUtilities.GenerateMovesEngine.GenerateMovesDependencies import get_player_wise_pieces_and_sides, \
    get_sliding_pieces, get_opponent_attacks_and_find_check
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import unsigned, get_least_bit_index


class MoveDependencyModel:
    def __init__(self, fen: Fen, previous_move: int):
        self.fen = fen
        self.previous_move = previous_move
        self.board_inverse = unsigned(~fen.game_board)
        # decide opponent and player pieces
        self.player_pieces, self.player_side, self.opponent_pieces, self.opponent_side = get_player_wise_pieces_and_sides(
            white_pieces=fen.white_pieces, black_pieces=fen.black_pieces, turn=fen.player_turn)
        # get the bitmask of player's king
        self.player_king_mask = self.player_pieces[PieceName.KING.value]
        self.player_king_pos: Positions = Positions(get_least_bit_index(self.player_king_mask))
        # king_rays: int = rook
        # get the sliding pieces of opponent
        self.opponent_sliding_pieces = get_sliding_pieces(piece_list=self.opponent_pieces)
        # get opponent attack mask, no of checks and the list of attackers as (Name, Position)
        self.opponent_attacks, self.check_count, self.attackers = get_opponent_attacks_and_find_check(
            opponent_pieces=self.opponent_pieces,
            player_king_mask=self.player_king_mask,
            opponent_side=self.opponent_side,
            board_state=fen.game_board)
