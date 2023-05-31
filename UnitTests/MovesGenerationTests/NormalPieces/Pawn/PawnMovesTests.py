from FenUtilities.FenDecrypt import decryptFen
from FenUtilities.FenModel import Fen
from MoveGenerationUtilities.GenerateMovesEngine.GenerateMoves import get_white_pawn_moves
from MoveGenerationUtilities.GenerateMovesEngine.MovesModel import MoveDependencyModel
from UnitTests.MovesGenerationTests.NormalPieces.Pawn.PawnTestsData import white_test_data
from UnitTests.UnitTestDependencies import assert_case
from UnitTests.UnitTestModels.UnitTestDataModel import UTestDataModel
from UnitTests.UnitTestModels.UnitTestModel import UnitTest
from UnitTests.UnitTestModels.UnitTestSectionModel import UTestSectionModel


def run_pawn_moves_tests() -> UTestSectionModel:
    return UTestSectionModel('Pawn Moves Tests', [])


def white_pawn_moves_length_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, fen, tested_values in enumerate(white_test_data.items()):
        fen_model: Fen = decryptFen(fen)
        move_model = MoveDependencyModel(fen_model, 0)
        moves_list_len = str(len(get_white_pawn_moves(move_model)))
        tested_values_len = str(len(tested_values))
        unit_tests.append(
            assert_case(moves_list_len, tested_values_len, index + 1))
    return UTestDataModel(test_case_title='White Pawn Move Count Tests', test_cases=unit_tests)

def white_pawn_moves_tests() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, fen, tested_values in enumerate(white_test_data.items()):
        fen_model: Fen = decryptFen(fen)
        move_model = MoveDependencyModel(fen_model, 0)
        moves_list_len = str(len(get_white_pawn_moves(move_model)))
        tested_values_len = str(len(tested_values))
        unit_tests.append(
            assert_case(moves_list_len, tested_values_len, index + 1))
    return UTestDataModel(test_case_title='White Pawn Move Generation Tests', test_cases=unit_tests)