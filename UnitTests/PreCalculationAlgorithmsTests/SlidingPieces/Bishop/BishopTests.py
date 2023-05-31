from DebugUtilities.BeautifyDependency.GameBeautify import get_binary
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Bishop import \
    get_bishop_attack_mask_exc_ends, get_bishop_attack_mask_inc_end_blockers, get_bishop_attacks
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.SliderAttacks import \
    init_slider_attacks
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import count_set_bits
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import bishop_attack_count, bishop_attacks, \
    bishop_attacks_table
from UnitTests.PreCalculationAlgorithmsTests.SlidingPieces.Bishop.TestedData import *
from UnitTests.UnitTestDependencies import assert_case, flatten_position
from UnitTests.UnitTestModels.UnitTestDataModel import UTestDataModel
from UnitTests.UnitTestModels.UnitTestModel import UnitTest
from UnitTests.UnitTestModels.UnitTestSectionModel import UTestSectionModel


def run_bishop_tests() -> UTestSectionModel:
    attacks_exc_end_generation_model = bishop_attack_exc_ends_generation_tests()
    attacks_exc_end_generated_model = bishop_attack_exc_ends_generated_tests()
    attacks_inc_end_generation_model = bishop_attack_inc_ends_generation_tests()
    attacks_count_generation_model = bishop_attack_count_generation_tests()
    attacks_count_generated_model = bishop_attack_count_generated_tests()
    attacks_generated_model = bishop_attacks_table_test()

    return UTestSectionModel('Bishop Tests', [attacks_exc_end_generation_model, attacks_exc_end_generated_model,
                                              attacks_inc_end_generation_model,
                                              attacks_count_generation_model, attacks_count_generated_model,
                                              attacks_generated_model])


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


def bishop_attack_inc_ends_generation_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_bishop_attack_count = get_binary(get_bishop_attack_mask_inc_end_blockers(position, 0))
        tested_bishop_attack_mask = flatten_position(tested_bishop_attacks_inc_ends[position.name])
        unit_tests.append(
            assert_case(str(tested_bishop_attack_mask), str(calculated_bishop_attack_count), index + 1))
    return UTestDataModel(test_case_title='Bishop Attacks inc. ends (no-blockers) Generation Tests',
                          test_cases=unit_tests)


def bishop_attacks_table_test() -> UTestDataModel:
    init_slider_attacks(bishop=True)
    unit_tests: list[UnitTest] = []
    index = 0
    for position in list(Positions)[:-1]:
        for blocker in range(4096):
            calculated_bishop_attack = count_set_bits(get_bishop_attacks(position.value, blocker) & blocker) in [0, 1,
                                                                                                                 2, 3,
                                                                                                                 4]
            unit_tests.append(
                assert_case(str(True), str(calculated_bishop_attack), index + 1))
            index += 1
    return UTestDataModel(test_case_title='Bishop Attacks Generated Tests',
                          test_cases=unit_tests)
