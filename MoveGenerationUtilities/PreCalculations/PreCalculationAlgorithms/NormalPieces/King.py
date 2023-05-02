from DebugUtilities.GameDependency.BoardDependency.DirectionalDependency.SpecificDirectionDependency import \
    SpecificDirections
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import bitmask, move_bit, unsigned
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import king_attack_maps


def init_king_attacks():
    for position in list(Positions)[:-1]:
        king_attack_maps[position.value] = get_king_attack(position.value)


def get_king_attack(position: int) -> int:
    attacks = 0
    piece_position = bitmask(position)
    # directions are
    # NORTH = 0
    # EAST = 1
    # SOUTH = 2
    # WEST = 3
    # NORTH_EAST = 4
    # NORTH_WEST = 5
    # SOUTH_EAST = 6
    # SOUTH_WEST = 7
    directions = list(SpecificDirections)[:8]
    for direction in directions:
        attacks |= move_bit(piece_position, direction)
    return unsigned(attacks)