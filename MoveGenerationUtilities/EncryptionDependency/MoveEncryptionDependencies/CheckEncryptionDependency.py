from enum import Enum


class CheckEncryptionAttributes(Enum):
    CHECK = 0
    DOUBLE_CHECK = 1
    BOTH_CHECK = 2
    KNIGHT_CHECK = 3
    ATTACKER_POSITION = 4
    ATTACKER_PIECE_NAME = 5