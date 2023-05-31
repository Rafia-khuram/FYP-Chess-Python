import json

from FenUtilities.FenDecrypt import *

from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.SliderAttacks import \
    init_slider_attacks
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SquareBitmaskDependencies import init_squares
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import count_set_bits
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import square_bitmask
from UnitTests.UnitTestDependencies import TestsOf
from UnitTests.UnitTestEngine import UnitTestEngine
from DebugUtilities.BeautifyDependency.GameBeautify import print_bitboard, get_binary
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Rook import \
    get_rook_attack_mask_inc_end_blockers
from DebugUtilities.BeautifyDependency.GameBeautify import print_attack_map
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Bishop import \
    get_bishop_attack_mask_inc_end_blockers, get_bishop_attacks


def run_main():
    u_engine = UnitTestEngine(show_only_tests=TestsOf.FAILED, print_test_cases=TestsOf.FAILED,
                              print_test_case_details=TestsOf.FAILED)
    u_engine.run_tests()
    u_engine.print_tests()


def run_testing():
    import itertools

    chess_positions = range(64)  # Assuming you have a list or range of 64 chess positions

    combinations = list(itertools.combinations(chess_positions, 16))

    # Print the generated combinations
    for combo in combinations:
        print(combo)


# run_main()
run_testing()
