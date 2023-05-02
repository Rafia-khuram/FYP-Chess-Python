from DebugUtilities.BeautifyDependency.GameBeautify import get_binary
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.NormalPieces.Knight import get_knight_attack
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import knight_attack_maps
from UnitTests.UnitTestDependencies import flatten_position, assert_case
from UnitTests.UnitTestModels.UnitTestDataModel import UTestDataModel
from UnitTests.UnitTestModels.UnitTestModel import UnitTest
from UnitTests.UnitTestModels.UnitTestSectionModel import UTestSectionModel
from UnitTests.PreCalculationAlgorithmsTests.NormalPieces.Knight.TestedData import knight_attacks_tested_data


def run_knight_tests() -> UTestSectionModel:
    attacks_generation_model = knight_attacks_generation_test()
    attacks_generated_model = knight_attacks_generated_test()
    return UTestSectionModel('Knight Tests', [attacks_generation_model, attacks_generated_model])


def knight_attacks_generation_test() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_knight_attack_mask = get_binary(get_knight_attack(position.value))
        tested_knight_attack_mask = flatten_position(knight_attacks_tested_data[position.name])
        unit_tests.append(
            assert_case(tested_knight_attack_mask, calculated_knight_attack_mask, index + 1))
    return UTestDataModel(test_case_title='Knight Attacks Generation Tests', test_cases=unit_tests)


def knight_attacks_generated_test() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_knight_attack_mask = get_binary(knight_attack_maps[position.value])
        tested_knight_attack_mask = flatten_position(knight_attacks_tested_data[position.name])
        unit_tests.append(
            assert_case(tested_knight_attack_mask, calculated_knight_attack_mask, index + 1))
    return UTestDataModel(test_case_title='Knight Attacks Generation Tests', test_cases=unit_tests)
