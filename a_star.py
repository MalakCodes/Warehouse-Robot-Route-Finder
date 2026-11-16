import heapq
import time
from itertools import count

from path_reconstruction import reconstruct_path


def heuristic(node, goal):
    """
    Calculate Manhattan Distance.
    """
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def get_movement_cost(cell):
    """
    Return the movement cost of a cell.
    """
    if cell == 3:
        return 3

    return 1


def a_star(grid, start, goal):
    start_time = time.perf_counter()

    # Validate grid and coordinates
    if not grid or not isinstance(start, tuple) or not isinstance(goal, tuple):
        return {
            "algorithm": "A*",
            "path": [],
            "cost": 0,
            "steps": 0,
            "expanded_nodes": 0,
            "execution_time": 0.0,
            "found": False
        }

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    if (
        len(start) != 2
        or len(goal) != 2
        or cols == 0
        or any(len(row) != cols for row in grid)
        or not (0 <= start[0] < rows and 0 <= start[1] < cols)
        or not (0 <= goal[0] < rows and 0 <= goal[1] < cols)
        or grid[start[0]][start[1]] not in (0, 3)
        or grid[goal[0]][goal[1]] not in (0, 3)
    ):
        return {
            "algorithm": "A*",
            "path": [],
            "cost": 0,
            "steps": 0,
            "expanded_nodes": 0,
            "execution_time": 0.0,
            "found": False
        }

   
    # Start and goal are the same
    if start == goal:
        return {
            "algorithm": "A*",
            "path": [start],
            "cost": 0,
            "steps": 0,
            "expanded_nodes": 0,
            "execution_time": time.perf_counter() - start_time,
            "found": True
        }

    # Priority Queue
    priority_queue = []

    tie_breaker = count()

    # Store the minimum cost to reach each cell
    g_score = {start: 0}

    # Store parent relationships
    parent = {}

    # Initial priority
    initial_f = heuristic(start, goal)

    heapq.heappush(
        priority_queue,
        (initial_f, next(tie_breaker), 0, start)
    )

    # Four possible movements
    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    expanded_nodes = 0
    found = False

    # A* Main Search Loop
    while priority_queue:

        current_f, _, current_g, current = heapq.heappop(
            priority_queue
        )

        # Ignore outdated entries
        if current_g != g_score.get(current):
            continue

        # Check if goal is reached
        if current == goal:
            found = True
            break

        expanded_nodes += 1

        current_row, current_col = current

        # Explore neighboring cells
        for dr, dc in directions:

            new_row = current_row + dr
            new_col = current_col + dc

            neighbor = (new_row, new_col)

            # Check grid boundaries
            if not (
                0 <= new_row < rows
                and 0 <= new_col < cols
            ):
                continue

            # Avoid obstacles
            if grid[new_row][new_col] == -1:
                continue

            # Calculate movement cost
            movement_cost = get_movement_cost(
                grid[new_row][new_col]
            )

            # Calculate new actual cost
            tentative_g = current_g + movement_cost

            # Update if a better path is found
            if tentative_g < g_score.get(
                neighbor, float("inf")
            ):

                g_score[neighbor] = tentative_g

                parent[neighbor] = current

                # Calculate heuristic
                h = heuristic(neighbor, goal)

                # Calculate total estimated cost
                f = tentative_g + h

                heapq.heappush(
                    priority_queue,
                    (
                        f,
                        next(tie_breaker),
                        tentative_g,
                        neighbor
                    )
                )

    # Reconstruct path
    if found:

        path = reconstruct_path(parent, start, goal)

        if not path:
            found = False

    if found:

        total_cost = g_score[goal]
        steps = len(path) - 1

    else:

        path = []
        total_cost = 0
        steps = 0

    # Calculate execution time
    execution_time = time.perf_counter() - start_time

    return {
        "algorithm": "A*",
        "path": path,
        "cost": total_cost,
        "steps": steps,
        "expanded_nodes": expanded_nodes,
        "execution_time": execution_time,
        "found": found
    }
