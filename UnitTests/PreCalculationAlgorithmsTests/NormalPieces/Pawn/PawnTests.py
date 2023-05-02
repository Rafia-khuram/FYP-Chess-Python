from DebugUtilities.BeautifyDependency.GameBeautify import get_binary
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PlayerDependency.PlayerSideDependency import PlayerSide

from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.NormalPieces.Pawn import get_pawn_attack
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import pawn_attack_maps
from UnitTests.UnitTestDependencies import flatten_position, assert_case
from UnitTests.UnitTestModels.UnitTestDataModel import UTestDataModel
from UnitTests.UnitTestModels.UnitTestModel import UnitTest
from UnitTests.UnitTestModels.UnitTestSectionModel import UTestSectionModel
from UnitTests.PreCalculationAlgorithmsTests.NormalPieces.Pawn.TestedData import pawn_attacks_tested_data


def run_pawn_tests() -> UTestSectionModel:
    attacks_generation_model = pawn_attacks_generation_test()
    attacks_generated_model = pawn_attacks_generated_test()
    return UTestSectionModel('Pawn Tests', [attacks_generation_model, attacks_generated_model])


def pawn_attacks_generation_test() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    case_id = 0
    for player_side in list(PlayerSide)[:-1]:
        for position in list(Positions)[:-1]:
            calculated_pawn_attack_mask = get_binary(get_pawn_attack(player_side, position.value))
            tested_pawn_attack_mask = flatten_position(pawn_attacks_tested_data[player_side.name][position.name])
            unit_tests.append(
                assert_case(tested_pawn_attack_mask, calculated_pawn_attack_mask, case_id + 1))
            case_id += 1
    return UTestDataModel(test_case_title='Pawn Attacks Generation Tests', test_cases=unit_tests)


def pawn_attacks_generated_test() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    case_id = 0
    for player_side in list(PlayerSide)[:-1]:
        for position in list(Positions)[:-1]:
            calculated_pawn_attack_mask = get_binary(pawn_attack_maps[player_side.value][position.value])
            tested_pawn_attack_mask = flatten_position(pawn_attacks_tested_data[player_side.name][position.name])
            unit_tests.append(
                assert_case(tested_pawn_attack_mask, calculated_pawn_attack_mask, case_id + 1))
            case_id += 1
    return UTestDataModel(test_case_title='Pawn Attacks Generation Tests', test_cases=unit_tests)
