from DebugUtilities.GameDependency.BoardDependency.DirectionalDependency.SpecificDirectionDependency import \
    SpecificDirections
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PlayerDependency.PlayerSideDependency import PlayerSide
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import bitmask, move_bit, unsigned
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import pawn_attack_maps


def init_pawn_attacks():
    for side in list(PlayerSide)[:-1]:
        for position in list(Positions)[:-1]:
            pawn_attack_maps[side.value][position.value] = get_pawn_attack(side, position.value)


def get_pawn_attack(side: PlayerSide, position: int) -> int:
    attacks = 0
    piece_position = bitmask(position)
    # if black side Directions are
    # SOUTH_EAST = 6
    # SOUTH_WEST = 7
    # else
    # NORTH_EAST = 4
    # NORTH_WEST = 5
    directions = list(SpecificDirections)[6:8] \
        if side is PlayerSide.BLACK else \
        list(SpecificDirections)[4:6]
    for pos in directions:
        attacks |= move_bit(piece_position, pos)
    return unsigned(attacks)
