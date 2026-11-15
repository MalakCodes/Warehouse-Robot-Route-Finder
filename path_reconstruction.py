
def reconstruct_path(parent, start, goal):
    """
    Reconstructs the path from the goal back to the start.

    Args:
        parent (dict): Stores the parent of each visited position.
        start (tuple): Starting position (row, column).
        goal (tuple): Goal position (row, column).

    Returns:
        list: Ordered path from start to goal.
             Returns an empty list if no path exists.
    """

    # Handle the case where start and goal are the same
    if start == goal:
        return [start]

    # Check whether the goal was reached
    if goal not in parent:
        return []

    path = []
    current = goal

    # Trace the path backwards
    while current is not None:
        path.append(current)

        if current == start:
            break

        current = parent.get(current)

    # Verify that the path reaches the start
    if path[-1] != start:
        return []

    # Reverse the path to get Start -> Goal
    path.reverse()

    return path
