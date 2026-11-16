
from warehouse_grid import create_warehouse_grid
from input_validation import validate_start_and_goal
from bfs import bfs
from ucs import ucs
from a_star import a_star


def select_algorithm(priority, use_heuristic=False):
    """
    Select the search algorithm based on user preferences.
    """

    if priority == "steps":
        return "BFS"

    elif priority == "cost":
        if use_heuristic:
            return "A*"
        else:
            return "UCS"

    else:
        raise ValueError("Invalid priority selection.")


def run_algorithm(priority, grid, start, goal, use_heuristic=False):
    """
    Select and run the appropriate search algorithm.
    """

    algorithm = select_algorithm(priority, use_heuristic)

    if not validate_start_and_goal(grid, start, goal):
        return {
            "algorithm": algorithm,
            "path": [],
            "cost": 0,
            "steps": 0,
            "expanded_nodes": 0,
            "execution_time": 0,
            "found": False
        }

    if algorithm == "BFS":
        return bfs(grid, start, goal)

    elif algorithm == "UCS":
        return ucs(grid, start, goal)

    elif algorithm == "A*":
        return a_star(grid, start, goal)
