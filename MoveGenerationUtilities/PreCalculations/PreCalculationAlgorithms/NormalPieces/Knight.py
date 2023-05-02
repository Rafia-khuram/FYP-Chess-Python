from DebugUtilities.GameDependency.BoardDependency.DirectionalDependency.SpecificDirectionDependency import \
    SpecificDirections
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import bitmask, move_bit, unsigned
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import knight_attack_maps


def init_knight_attacks():
    from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
    for position in list(Positions)[:-1]:
        knight_attack_maps[position.value] = get_knight_attack(position.value)


def get_knight_attack(position: int) -> int:
    attacks = 0
    piece_position = bitmask(position)
    # Directions are
    # NORTH_EAST_EAST = 8
    # NORTH_WEST_WEST = 9
    # NORTH_NORTH_EAST = 10
    # NORTH_NORTH_WEST = 11
    # SOUTH_EAST_EAST = 12
    # SOUTH_WEST_WEST = 13
    # SOUTH_SOUTH_EAST = 14
    # SOUTH_SOUTH_WEST = 15
    directions = list(SpecificDirections)[8:16]
    for direction in directions:
        attacks |= move_bit(piece_position, direction)
    return unsigned(attacks)
