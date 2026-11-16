def create_warehouse_grid():
    """
    Create the 10x10 warehouse grid.

    Cell values:
    0  = Ordinary cell
    3  = High-cost cell
    -1 = Obstacle
    """

    grid = [
        [0,  0,  0,  0,  3,  0,  0,  0,  0,  0],
        [0,  0, -1, -1,  0,  0,  0, -1,  0,  0],
        [0,  0,  3,  0,  0, -1,  0, -1,  0,  0],
        [0, -1,  0,  0,  0, -1,  0,  3,  0,  0],
        [0,  0,  0, -1,  0,  0,  0,  0, -1,  0],
        [0, -1,  0,  0,  3,  0, -1,  0,  0,  0],
        [0,  0,  0, -1,  0,  0,  3,  0, -1,  0],
        [0,  0, -1,  0,  0,  0,  0, -1,  0,  0],
        [0,  3,  0,  0, -1,  0,  0,  0, -1,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
    ]

    return grid


def is_valid_position(grid, position):
    """
    Check whether a position is inside the grid.
    """

    row, col = position

    return (
        0 <= row < len(grid)
        and 0 <= col < len(grid[0])
    )


def is_walkable(grid, position):
    """
    Check whether a position is inside the grid
    and is not an obstacle.
    """

    if not is_valid_position(grid, position):
        return False

    row, col = position

    return grid[row][col] != -1


def get_move_cost(grid, position):
    """
    Return the movement cost of a cell.

    Ordinary cell = 1
    High-cost cell = 3
    Obstacle = -1
    """

    if not is_valid_position(grid, position):
        return -1

    row, col = position

    if grid[row][col] == -1:
        return -1

    if grid[row][col] == 3:
        return 3

    return 1


# Warehouse locations
# Coordinates are represented as (row, column)
# Coordinates use zero-based indexing.

START = (0, 1)
GOAL = (9, 9)

# Three storage zones
STORAGE_ZONES = {
    "S1": (0, 9),
    "S2": (5, 9),
    "S3": (9, 9)
}

# Two charging stations
CHARGING_STATIONS = {
    "C1": (0, 0),
    "C2": (9, 0)
}


def get_warehouse_locations():
    """
    Return the main warehouse locations.
    """

    return {
        "start": START,
        "goal": GOAL,
        "storage_zones": STORAGE_ZONES,
        "charging_stations": CHARGING_STATIONS
    }