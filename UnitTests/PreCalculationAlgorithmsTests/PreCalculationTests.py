from UnitTests.PreCalculationAlgorithmsTests.DirectionalRays.DirectionalRaysTests import run_directional_rays_tests
from UnitTests.PreCalculationAlgorithmsTests.SquareBitmask.SquareBitmaskTests import run_square_bitmask_tests
from UnitTests.UnitTestModels.UnitTestSectionModel import UTestSectionModel
from UnitTests.PreCalculationAlgorithmsTests.NormalPieces.King.KingTests import run_king_tests
from UnitTests.PreCalculationAlgorithmsTests.NormalPieces.Knight.KnightTests import run_knight_tests
from UnitTests.PreCalculationAlgorithmsTests.NormalPieces.Pawn.PawnTests import run_pawn_tests
from UnitTests.PreCalculationAlgorithmsTests.SlidingPieces.Bishop.BishopTests import run_bishop_tests
from UnitTests.PreCalculationAlgorithmsTests.SlidingPieces.Rooks.RookTests import run_rook_tests


def run_tests() -> list[UTestSectionModel]:
    return [run_square_bitmask_tests(),
            run_directional_rays_tests(),
            run_king_tests(),
            run_knight_tests(),
            run_pawn_tests(),
            run_bishop_tests(),
            run_rook_tests()]
