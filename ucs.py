
import heapq
import time
from itertools import count

from path_reconstruction import reconstruct_path


def ucs(grid, start, goal):
    """
    Uniform-Cost Search (UCS).

    Finds the lowest-cost path from start to goal
    while avoiding obstacles.
    """

    # Check that start and goal are valid positions
    def is_walkable(position):
        row, col = position

        if row < 0 or row >= len(grid):
            return False

        if col < 0 or col >= len(grid[row]):
            return False

        return grid[row][col] != -1

    # Get the movement cost of a cell
    def get_move_cost(position):
        row, col = position
        cell = grid[row][col]

        if cell == 0:
            return 1
        elif cell == 3:
            return 3
        else:
            return None

      # Standard result when no route is found
    def no_route_result(execution_time=0, expanded_nodes=0):
        return {
            "algorithm": "UCS",
            "path": [],
            "cost": 0,
            "steps": 0,
            "expanded_nodes": expanded_nodes,
            "execution_time": execution_time,
            "found": False
        }

    # Validate the input
    if not grid or not isinstance(start, tuple) or not isinstance(goal, tuple):
        return no_route_result()

    if len(start) != 2 or len(goal) != 2:
        return no_route_result()

    if not is_walkable(start) or not is_walkable(goal):
        return no_route_result()

    # Initialize the priority queue
    counter = count()
    priority_queue = [(0, next(counter), start)]

    # Store the lowest cost to reach each position
    cost_so_far = {start: 0}

    # Store parent positions for path reconstruction
    parent = {}

    # Count expanded nodes
    expanded_nodes = 0

    # Start measuring search execution time
    start_time = time.perf_counter()

    found = False

    # UCS main search loop
    while priority_queue:

        current_cost, _, current = heapq.heappop(priority_queue)

        # Ignore outdated entries
        if current_cost != cost_so_far.get(current):
            continue

        # Stop when the goal is reached
        if current == goal:
            found = True
            break

        expanded_nodes += 1

        row, col = current

        # Four possible movement directions
        neighbors = [
            (row - 1, col),  # Up
            (row + 1, col),  # Down
            (row, col - 1),  # Left
            (row, col + 1)   # Right
        ]

        # Explore neighboring positions
        for neighbor in neighbors:

            if not is_walkable(neighbor):
                continue

            move_cost = get_move_cost(neighbor)

            new_cost = current_cost + move_cost

            # Update if a better path is found
            if new_cost < cost_so_far.get(neighbor, float("inf")):

                cost_so_far[neighbor] = new_cost
                parent[neighbor] = current

                heapq.heappush(
                    priority_queue,
                    (new_cost, next(counter), neighbor)
                )

    # Finish measuring search time
    execution_time = time.perf_counter() - start_time

    # Return failure if no route exists
    if not found:
        return no_route_result(execution_time, expanded_nodes)

    # Reconstruct the path using Malak's function
    path = reconstruct_path(parent, start, goal)

    if not path:
        return no_route_result(execution_time, expanded_nodes)

    # Calculate final performance metrics
    total_cost = cost_so_far[goal]
    number_of_steps = len(path) - 1

    return {
        "algorithm": "UCS",
        "path": path,
        "cost": total_cost,
        "steps": number_of_steps,
        "expanded_nodes": expanded_nodes,
        "execution_time": execution_time,
        "found": True
    }
