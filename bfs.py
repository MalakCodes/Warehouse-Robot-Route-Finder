
from collections import deque
import time

def bfs(grid, start, goal):
    """
    Find a path from start to goal using Breadth-First Search.
    BFS finds the path with the minimum number of steps.
    """

    start_time = time.perf_counter()

    rows = len(grid)
    cols = len(grid[0])

    # Check whether positions are inside the grid
    def is_valid(position):
        r, c = position
        return 0 <= r < rows and 0 <= c < cols

    # Check whether a cell is not an obstacle
    def is_walkable(position):
        r, c = position
        return grid[r][c] != -1

    # Validate start and goal
    if not is_valid(start) or not is_valid(goal):
        return {
            "algorithm": "BFS",
            "path": [],
            "cost": 0,
            "steps": 0,
            "expanded_nodes": 0,
            "execution_time": time.perf_counter() - start_time,
            "found": False
        }

    if not is_walkable(start) or not is_walkable(goal):
        return {
            "algorithm": "BFS",
            "path": [],
            "cost": 0,
            "steps": 0,
            "expanded_nodes": 0,
            "execution_time": time.perf_counter() - start_time,
            "found": False
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

            total_cost = sum(
                3 if grid[r][c] == 3 else 1
                for r, c in path[1:]
            )

            execution_time = time.perf_counter() - start_time

            return {
                "algorithm": "BFS",
                "path": path,
                "cost": total_cost,
                "steps": len(path) - 1,
                "expanded_nodes": expanded_nodes,
                "execution_time": execution_time,
                "found": True
            }

        expanded_nodes += 1

        # Explore neighboring cells
        r, c = current

        for dr, dc in directions:
            neighbor = (r + dr, c + dc)

            if is_valid(neighbor) and is_walkable(neighbor):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)

    # No path found
    return {
        "algorithm": "BFS",
        "path": [],
        "cost": 0,
        "steps": 0,
        "expanded_nodes": expanded_nodes,
        "execution_time": time.perf_counter() - start_time,
        "found": False
    }


from path_reconstruction import reconstruct_path
