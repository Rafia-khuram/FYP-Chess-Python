from DebugUtilities.BeautifyDependency.GameBeautify import get_binary
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Bishop import \
    get_bishop_attack_mask_exc_ends
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import count_set_bits
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import bishop_attack_count, bishop_attacks
from UnitTests.UnitTestDependencies import assert_case, flatten_position
from UnitTests.UnitTestModels.UnitTestDataModel import UTestDataModel
from UnitTests.UnitTestModels.UnitTestModel import UnitTest
from UnitTests.UnitTestModels.UnitTestSectionModel import UTestSectionModel
from UnitTests.PreCalculationAlgorithmsTests.SlidingPieces.Bishop.TestedData import *


def run_bishop_tests() -> UTestSectionModel:
    attacks_exc_end_generation_model = bishop_attack_exc_ends_generation_tests()
    attacks_exc_end_generated_model = bishop_attack_exc_ends_generated_tests()
    attacks_count_generation_model = bishop_attack_count_generation_tests()
    attacks_count_generated_model = bishop_attack_count_generated_tests()
    return UTestSectionModel('Bishop Tests', [attacks_exc_end_generation_model, attacks_exc_end_generated_model,
                                              attacks_count_generation_model, attacks_count_generated_model])


def bishop_attack_count_generation_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_bishop_attack_count = count_set_bits(
            get_bishop_attack_mask_exc_ends(position))
        tested_bishop_attack_mask = tested_bishop_attack_counts[position.value]
        unit_tests.append(
            assert_case(str(tested_bishop_attack_mask), str(calculated_bishop_attack_count), index + 1))
    return UTestDataModel(test_case_title='Bishop Attacks Count Generation Tests', test_cases=unit_tests)


def bishop_attack_count_generated_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_bishop_attack_count = bishop_attack_count[position.value]
        tested_bishop_attack_mask = tested_bishop_attack_counts[position.value]
        unit_tests.append(
            assert_case(str(tested_bishop_attack_mask), str(calculated_bishop_attack_count), index + 1))
    return UTestDataModel(test_case_title='Bishop Attacks Count Generated Tests', test_cases=unit_tests)


def bishop_attack_exc_ends_generation_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_bishop_attack_count = get_binary(get_bishop_attack_mask_exc_ends(position))
        tested_bishop_attack_mask = flatten_position(tested_bishop_attacks_exc_ends[position.name])
        unit_tests.append(
            assert_case(str(tested_bishop_attack_mask), str(calculated_bishop_attack_count), index + 1))
    return UTestDataModel(test_case_title='Bishop Attacks exc. ends Generation Tests', test_cases=unit_tests)


def bishop_attack_exc_ends_generated_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_bishop_attack_count = get_binary(bishop_attacks[position.value])
        tested_bishop_attack_mask = flatten_position(tested_bishop_attacks_exc_ends[position.name])
        unit_tests.append(
            assert_case(str(tested_bishop_attack_mask), str(calculated_bishop_attack_count), index + 1))
    return UTestDataModel(test_case_title='Bishop Attacks exc. ends Generated Tests', test_cases=unit_tests)
