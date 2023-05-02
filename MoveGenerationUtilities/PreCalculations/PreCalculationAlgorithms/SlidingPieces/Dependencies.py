from ctypes import c_uint32, c_uint64

from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.PreCalculationDependencies import setOccupancy
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Bishop import \
    get_bishop_attack_mask_inc_end_blockers
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Rook import \
    get_rook_attack_mask_inc_end_blockers
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import count_set_bits, bitmask

from MoveGenerationUtilities.PreCalculations.PreCalculationsData import bishop_attacks, rook_attacks, square_bitmask, \
    bishop_magic_number, bishop_attack_count, bishop_attacks_table, rook_magic_number, rook_attack_count, \
    rook_attacks_table


def init_slider_attacks(bishop: bool):
    piece_attacks = bishop_attacks if bishop else rook_attacks
    for position in list(Positions)[:-1]:
        attack_mask = piece_attacks[position.value]
        relevant_bits = count_set_bits(attack_mask)
        occupancy_indices = square_bitmask[relevant_bits]
        for index in range(occupancy_indices):
            if bishop:
                occupancy = setOccupancy(index, relevant_bits, attack_mask)
                magic_index = c_uint32(c_uint64(occupancy * bishop_magic_number[position.value]).value >> (
                        64 - bishop_attack_count[position.value])).value
                bishop_attacks_table[position.value][magic_index] = get_bishop_attack_mask_inc_end_blockers(
                    bitmask(position.value), occupancy)
            else:
                occupancy = setOccupancy(index, relevant_bits, attack_mask)
                magic_index = c_uint32(c_uint64(occupancy * rook_magic_number[position.value]).value >> (
                        64 - rook_attack_count[position.value])).value
                rook_attacks_table[position.value][magic_index] = get_rook_attack_mask_inc_end_blockers(
                    bitmask(position.value), occupancy)