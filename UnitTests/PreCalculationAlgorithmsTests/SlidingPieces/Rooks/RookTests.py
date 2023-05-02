from DebugUtilities.BeautifyDependency.GameBeautify import get_binary
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Rook import \
    get_rook_attack_mask_exc_ends
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import count_set_bits
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import rook_attacks, rook_attack_count
from UnitTests.UnitTestDependencies import assert_case, flatten_position
from UnitTests.UnitTestModels.UnitTestDataModel import UTestDataModel
from UnitTests.UnitTestModels.UnitTestModel import UnitTest
from UnitTests.UnitTestModels.UnitTestSectionModel import UTestSectionModel
from UnitTests.PreCalculationAlgorithmsTests.SlidingPieces.Rooks.TestedData import *


def run_rook_tests() -> UTestSectionModel:
    attacks_exc_end_generation_model = rook_attack_exc_ends_generation_tests()
    attacks_exc_end_generated_model = rook_attack_exc_ends_generated_tests()
    attacks_count_generation_model = rook_attack_count_generation_tests()
    attacks_count_generated_model = rook_attack_count_generated_tests()
    return UTestSectionModel('Rook Tests', [attacks_exc_end_generation_model, attacks_exc_end_generated_model,
                                            attacks_count_generation_model, attacks_count_generated_model])


def rook_attack_count_generation_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_rook_attack_count = count_set_bits(get_rook_attack_mask_exc_ends(position))
        tested_rook_attack_mask = tested_rook_attack_counts[position.value]
        unit_tests.append(
            assert_case(str(tested_rook_attack_mask), str(calculated_rook_attack_count), index + 1))
    return UTestDataModel(test_case_title='Rook Attacks Count Generation Tests', test_cases=unit_tests)


def rook_attack_count_generated_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_rook_attack_count = rook_attack_count[position.value]
        tested_rook_attack_mask = tested_rook_attack_counts[position.value]
        unit_tests.append(
            assert_case(str(tested_rook_attack_mask), str(calculated_rook_attack_count), index + 1))
    return UTestDataModel(test_case_title='Rook Attacks Count Generated Tests', test_cases=unit_tests)


def rook_attack_exc_ends_generation_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_rook_attack_count = get_binary(get_rook_attack_mask_exc_ends(position))
        tested_rook_attack_mask = flatten_position(tested_rook_attacks_exc_ends[position.name])
        unit_tests.append(
            assert_case(str(tested_rook_attack_mask), str(calculated_rook_attack_count), index + 1))
    return UTestDataModel(test_case_title='Rook Attacks exc. ends Generation Tests', test_cases=unit_tests)


def rook_attack_exc_ends_generated_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_rook_attack_count = get_binary(rook_attacks[position.value])
        tested_rook_attack_mask = flatten_position(tested_rook_attacks_exc_ends[position.name])
        unit_tests.append(
            assert_case(str(tested_rook_attack_mask), str(calculated_rook_attack_count), index + 1))
    return UTestDataModel(test_case_title='Rook Attacks exc. ends Generated Tests', test_cases=unit_tests)
