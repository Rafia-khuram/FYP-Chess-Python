from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import bitmask
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import square_bitmask


def init_squares():
    for position in list(Positions)[:-1]:
        square_bitmask[position.value] = (bitmask(position.value))
