from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.DirectionalRaysUtilities import \
    init_directional_rays
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.MagicNumbersUtilities import init_magic_numbers
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.NormalPieces.King import init_king_attacks
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.NormalPieces.Knight import init_knight_attacks
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.NormalPieces.Pawn import init_pawn_attacks
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Bishop import \
    init_bishop_attack_mask
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Dependencies import \
    init_slider_attacks

from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Rook import init_rook_attack_mask
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SquareBitmaskDependencies import init_squares


def init_attacks(load_pre_cal_algo: bool = False):
    if load_pre_cal_algo:
        init_squares()
        init_directional_rays()
        init_pawn_attacks()
        init_knight_attacks()
        init_king_attacks()
        init_rook_attack_mask()
        init_bishop_attack_mask()
        init_magic_numbers()
    init_slider_attacks(True)
    init_slider_attacks(False)
