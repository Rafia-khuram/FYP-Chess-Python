from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName


#   castle   enpassant   double push  Capture  Promotion piece  piece_name   Target sq  Source sq
#     0          0             0         0          0000           0000       000000     000000
def encode_move(source_square: Positions, target_square: Positions, piece_name: PieceName,
                promotion_piece_name: PieceName, capture_flag: bool,
                double_push_flag: bool, enpassant_flag: bool, castle_flag: bool):
    return source_square.value | \
           (target_square.value << 6) | \
           (piece_name.value << 12) | \
           (promotion_piece_name.value << 16) | \
           (capture_flag << 20) | \
           (double_push_flag << 21) | \
           (enpassant_flag << 22) | \
           (castle_flag << 23)
