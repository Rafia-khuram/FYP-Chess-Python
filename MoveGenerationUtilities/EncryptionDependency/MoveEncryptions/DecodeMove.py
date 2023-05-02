from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName
from MoveGenerationUtilities.EncryptionDependency.MoveEncryptionDependencies.MoveEncryptionDependency import \
    MoveEncryptionAttributes, EncryptionPrams


def decode_move(move: int, attribute_name: MoveEncryptionAttributes) -> int:
    return int(move >> attribute_name.value[EncryptionPrams.SHIFT_BITS.value]) \
           & \
           int(attribute_name.value[EncryptionPrams.SET_BITS.value])


def decode_move_all(move: int) -> [PieceName, Positions, Positions, PieceName, bool, bool, bool, bool]:
    piece_name: PieceName = PieceName(decode_move(move, MoveEncryptionAttributes.PIECE_NAME))
    source_square: Positions = Positions(decode_move(move, MoveEncryptionAttributes.SOURCE_SQUARE))
    target_square: Positions = Positions(decode_move(move, MoveEncryptionAttributes.TARGET_SQUARE))
    promotion_piece_name: PieceName = PieceName(decode_move(move, MoveEncryptionAttributes.PROMOTION_PIECE_NAME))
    capture: bool = bool(decode_move(move, MoveEncryptionAttributes.CAPTURE_FLAG))
    double_push: bool = bool(decode_move(move, MoveEncryptionAttributes.DOUBLE_PUSH_FLAG))
    enpassant: bool = bool(decode_move(move, MoveEncryptionAttributes.EN_PASSANT_FLAG))
    castle: bool = bool(decode_move(move, MoveEncryptionAttributes.CASTLE_FLAG))
    return piece_name, source_square, target_square, promotion_piece_name, capture, double_push, enpassant, castle
