from DebugUtilities.GameDependency.BoardDependency.DirectionalDependency.SpecificDirectionDependency import \
    SpecificDirections
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from MoveGenerationUtilities.PreCalculations.PreCalculationDependencies import move_bit
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import directional_rays, square_bitmask


def init_directional_rays():
    for direction in list(SpecificDirections)[:8]:
        directional_rays[direction.value] = get_all_uni_directional_rays(direction)


def get_all_uni_directional_rays(direction: SpecificDirections):
    uni_directional_ray_list = [0 for _ in range(64)]
    for position in list(Positions)[:-1]:
        uni_directional_ray_list[position.value] = get_ray_wrt_pos_dir(direction, position)
    return uni_directional_ray_list


def get_ray_wrt_pos_dir(direction: SpecificDirections, position: Positions):
    my_position = square_bitmask[position.value]
    ray = 0
    while my_position:
        my_position = move_bit(my_position, direction)
        ray |= my_position
    return ray
