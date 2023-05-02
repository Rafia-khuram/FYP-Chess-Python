from DebugUtilities.BeautifyDependency.GameBeautify import get_binary
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions

from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import bitmask
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import square_bitmask
from UnitTests.PreCalculationAlgorithmsTests.SquareBitmask.TestedData import tested_square_bitmask
from UnitTests.UnitTestDependencies import assert_case, flatten_position
from UnitTests.UnitTestModels.UnitTestDataModel import UTestDataModel
from UnitTests.UnitTestModels.UnitTestModel import UnitTest
from UnitTests.UnitTestModels.UnitTestSectionModel import UTestSectionModel


def run_square_bitmask_tests() -> UTestSectionModel:
    mask_generation_model = square_bitmask_generation_tests()
    mask_generated_model = square_bitmask_generated_tests()
    return UTestSectionModel('Bitmask Tests', [mask_generation_model, mask_generated_model])


def square_bitmask_generation_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_bitmask = get_binary(bitmask(position.value))
        tested_bitmask = flatten_position(tested_square_bitmask[position.name])
        unit_tests.append(
            assert_case(tested_bitmask, calculated_bitmask, index + 1))
    return UTestDataModel(test_case_title='Bitmask Generation Tests', test_cases=unit_tests)


def square_bitmask_generated_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_bitmask = get_binary(square_bitmask[position.value])
        tested_bitmask = flatten_position(tested_square_bitmask[position.name])
        unit_tests.append(
            assert_case(tested_bitmask, calculated_bitmask, index + 1))
    return UTestDataModel(test_case_title='Bitmask Generated Tests', test_cases=unit_tests)
