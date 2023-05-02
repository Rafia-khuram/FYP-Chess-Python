from enum import Enum


class MoveEncryptionAttributes(Enum):
    SOURCE_SQUARE = (0b111111, 0)
    TARGET_SQUARE = (0b111111, 6)
    PIECE_NAME = (0b1111, 12)
    PROMOTION_PIECE_NAME = (0b1111, 16)
    CAPTURE_FLAG = (0b1, 20)
    DOUBLE_PUSH_FLAG = (0b1, 21)
    EN_PASSANT_FLAG = (0b1, 22)
    CASTLE_FLAG = (0b1, 23)


class EncryptionPrams(Enum):
    SET_BITS = 0
    SHIFT_BITS = 1
