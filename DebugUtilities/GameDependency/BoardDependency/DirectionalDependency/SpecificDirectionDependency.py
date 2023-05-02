from enum import Enum


class SpecificDirections(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    NORTH_EAST = 4
    NORTH_WEST = 5
    SOUTH_EAST = 6
    SOUTH_WEST = 7
    NORTH_EAST_EAST = 8
    NORTH_WEST_WEST = 9
    NORTH_NORTH_EAST = 10
    NORTH_NORTH_WEST = 11
    SOUTH_EAST_EAST = 12
    SOUTH_WEST_WEST = 13
    SOUTH_SOUTH_EAST = 14
    SOUTH_SOUTH_WEST = 15
    NOT_ALIGNED = 16

    def __str__(self) -> int:
        return self._value_