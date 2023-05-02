from ctypes import c_uint64
from math import log2

from DebugUtilities.GameDependency.BoardDependency.DirectionalDependency.SpecificDirectionDependency import \
    SpecificDirections
from MoveGenerationUtilities.Const import *


def count_set_bits(bitboard: int) -> int:
    count = 0
    while bitboard:
        bitboard &= bitboard - 1
        count += 1
    return count


def get_least_bit_index(bitboard: int) -> int:
    if not bitboard:
        return -1
    else:
        return int(log2(bitboard & -bitboard))


def unsigned(signed_number: int) -> int:
    return c_uint64(signed_number).value


def bitmask(position: int) -> int:
    return unsigned(1 << position)


def get_row_col(position: int) -> [int, int]:
    row = 7 - int(position / 8)
    col = 7 - int(position % 8)
    return row, col


def move_bit(bitmap: int, direction: SpecificDirections):
    if not bitmap:
        return 0
    elif direction is SpecificDirections.EAST:
        return (bitmap >> 1) & unsigned(~left_edge)
    elif direction is SpecificDirections.WEST:
        return (bitmap << 1) & unsigned(~right_edge)
    elif direction is SpecificDirections.NORTH:
        return bitmap << 8 if bitmap & unsigned(~top_edge) else 0
    elif direction is SpecificDirections.SOUTH:
        return bitmap >> 8 if bitmap & unsigned(~bottom_edge) else 0
    elif direction is SpecificDirections.NORTH_EAST:
        return (bitmap << 7) & unsigned(~left_edge)
    elif direction is SpecificDirections.NORTH_WEST:
        return (bitmap << 9) & unsigned(~right_edge)
    elif direction is SpecificDirections.SOUTH_EAST:
        return (bitmap >> 9) & unsigned(~left_edge)
    elif direction is SpecificDirections.SOUTH_WEST:
        return (bitmap >> 7) & unsigned(~right_edge)
    elif direction is SpecificDirections.NORTH_EAST_EAST:
        return (bitmap << 6) & unsigned(~(left_edge | before_left_edge))
    elif direction is SpecificDirections.NORTH_WEST_WEST:
        return (bitmap << 10) & unsigned(~(right_edge | before_right_edge))
    elif direction is SpecificDirections.SOUTH_EAST_EAST:
        return (bitmap >> 10) & unsigned(~(left_edge | before_left_edge))
    elif direction == SpecificDirections.SOUTH_WEST_WEST:
        return (bitmap >> 6) & unsigned(~(right_edge | before_right_edge))
    elif direction == SpecificDirections.NORTH_NORTH_EAST:
        return (bitmap << 15) & unsigned(~left_edge)
    elif direction == SpecificDirections.NORTH_NORTH_WEST:
        return (bitmap << 17) & unsigned(~right_edge)
    elif direction == SpecificDirections.SOUTH_SOUTH_EAST:
        return (bitmap >> 17) & unsigned(~left_edge)
    elif direction == SpecificDirections.SOUTH_SOUTH_WEST:
        return (bitmap >> 15) & unsigned(~right_edge)
    return 0
