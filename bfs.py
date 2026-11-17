from collections import deque
import time
from path_reconstruction import reconstruct_path


def bfs(grid, start, goal):
    """
    Find a path from start to goal using Breadth-First Search.
    BFS finds a path with the minimum number of steps.
    """

    start_time = time.perf_counter()

    # Standard failure result
    def no_route_result(expanded_nodes=0):
        return {
            "algorithm": "BFS",
            "path": [],
            "cost": 0,
            "steps": 0,
            "expanded_nodes": expanded_nodes,
            "execution_time": time.perf_counter() - start_time,
            "found": False
        }

    # Validate grid structure
    if (
        not isinstance(grid, list)
        or not grid
        or not all(isinstance(row, list) for row in grid)
        or not grid[0]
        or any(len(row) != len(grid[0]) for row in grid)
    ):
        return no_route_result()

    rows = len(grid)
    cols = len(grid[0])

    # Validate positions
    def valid_position(position):
        return (
            isinstance(position, tuple)
            and len(position) == 2
            and all(type(value) is int for value in position)
            and 0 <= position[0] < rows
            and 0 <= position[1] < cols
        )

    if not valid_position(start) or not valid_position(goal):
        return no_route_result()

    # Check whether a cell is walkable
    def is_walkable(position):
        r, c = position
        return grid[r][c] in (0, 3)

    # Validate start and goal cells
    if not is_walkable(start) or not is_walkable(goal):
        return no_route_result()

    # Start and goal are the same
    if start == goal:
        return {
            "algorithm": "BFS",
            "path": [start],
            "cost": 0,
            "steps": 0,
            "expanded_nodes": 0,
            "execution_time": time.perf_counter() - start_time,
            "found": True
        }

    # Initialize BFS
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    # Four possible movements
    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    expanded_nodes = 0

    while queue:
        current = queue.popleft()

        # Goal reached
        if current == goal:
            path = reconstruct_path(parent, start, goal)

            if not path:
                return no_route_result(expanded_nodes)

            total_cost = sum(
                3 if grid[r][c] == 3 else 1
                for r, c in path[1:]
            )

            return {
                "algorithm": "BFS",
                "path": path,
                "cost": total_cost,
                "steps": len(path) - 1,
                "expanded_nodes": expanded_nodes,
                "execution_time": time.perf_counter() - start_time,
                "found": True
            }

        expanded_nodes += 1

        r, c = current

        # Explore neighboring cells
        for dr, dc in directions:
            neighbor = (r + dr, c + dc)

            if (
                0 <= neighbor[0] < rows
                and 0 <= neighbor[1] < cols
                and is_walkable(neighbor)
                and neighbor not in visited
            ):
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    # No path found
    return no_route_result(expanded_nodes)