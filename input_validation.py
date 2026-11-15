def validate_position(grid, position, name="Position"):
    """
    Validate that a position is inside the grid
    and is not an obstacle.
    """

    # Check that position contains exactly two coordinates
    if not isinstance(position, tuple) or len(position) != 2:
        print(f"Invalid {name}: position must be in the form (row, column).")
        return False

    row, col = position

    # Check that coordinates are integers
    if not isinstance(row, int) or not isinstance(col, int):
        print(f"Invalid {name}: row and column must be integers.")
        return False

    # Check grid boundaries
    if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
        print(f"Invalid {name}: position is outside the grid.")
        return False

    # Check obstacle
    if grid[row][col] == -1:
        print(f"Invalid {name}: position is an obstacle.")
        return False

    return True


def validate_start_and_goal(grid, start, goal):
    """
    Validate both start and goal positions.
    """

    start_valid = validate_position(grid, start, "Start")
    goal_valid = validate_position(grid, goal, "Goal")

    return start_valid and goal_valid