from ctypes import c_uint64, c_uint32

from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.PreCalculationDependencies import setOccupancy
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.RandomNumbersUtilities import get_64b_rand_no
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Bishop import \
    get_bishop_attack_mask_exc_ends, get_bishop_attack_mask_inc_end_blockers
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Rook import \
    get_rook_attack_mask_inc_end_blockers, get_rook_attack_mask_exc_ends

from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import bitmask, count_set_bits, unsigned
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import *


def init_magic_numbers():
    for position in list(Positions)[:-1]:
        rook_magic_number[position.value] = find_magic_number(bitmask(position.value),
                                                              rook_attack_count[position.value], False)
        bishop_magic_number[position.value] = find_magic_number(bitmask(position.value),
                                                                bishop_attack_count[position.value], True)


def generate_magic_number() -> c_uint64:
    return c_uint64(get_64b_rand_no().value & get_64b_rand_no().value & get_64b_rand_no().value)


def find_magic_number(piece_position: int, relevant_occupancy_bits: int, bishop: bool) -> int:
    occupancies = [0] * 4096
    attacks = [0] * 4096
    attack_mask = get_bishop_attack_mask_exc_ends(piece_position) if bishop else get_rook_attack_mask_exc_ends(
        piece_position)
    occupancy_indexes = bitmask(relevant_occupancy_bits)
    for index in range(occupancy_indexes):
        occupancies[index] = setOccupancy(index, relevant_occupancy_bits, attack_mask)
        attacks[index] = get_bishop_attack_mask_inc_end_blockers(
            piece_position, occupancies[index]) if bishop else get_rook_attack_mask_inc_end_blockers(
            piece_position, occupancies[index])
    for random_count in range(100000000):
        magic_number = generate_magic_number().value
        num_to_multiply = 0xFF00000000000000
        if count_set_bits((attack_mask * magic_number) & num_to_multiply) < 6:
            continue
        used_attacks = [0 for _ in range(4096)]
        fail = False
        for index in range(occupancy_indexes):
            if fail:
                break
            magic_index = c_uint32(
                c_uint64(occupancies[index] * magic_number).value >> (64 - relevant_occupancy_bits)).value
            if used_attacks[magic_index] == 0:
                used_attacks[magic_index] = attacks[index]
            elif used_attacks[magic_index] != attacks[index]:
                fail = True
        if not fail:
            return unsigned(magic_number)
    return 0
