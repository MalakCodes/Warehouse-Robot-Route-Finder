
from warehouse_grid import (
    create_warehouse_grid,
    START,
    STORAGE_ZONES,
    CHARGING_STATIONS
)
from bfs import bfs
from ucs import ucs
from a_star import a_star

# Use the same start and destination in every test
start = START
goal = STORAGE_ZONES["S3"]

# Protect important locations
protected = {
    START,
    *STORAGE_ZONES.values(),
    *CHARGING_STATIONS.values()
}

def create_test_grid(target_obstacles):
    grid = create_warehouse_grid()

    current = sum(
        cell == -1 for row in grid for cell in row
    )

    # Remove obstacles if the target is smaller
    if target_obstacles < current:
        for r in range(9, -1, -1):
            for c in range(9, -1, -1):
                if current == target_obstacles:
                    break
                if grid[r][c] == -1:
                    grid[r][c] = 0
                    current -= 1
            if current == target_obstacles:
                break

    # Add obstacles if the target is larger
    elif target_obstacles > current:
        for r in range(9, -1, -1):
            for c in range(9, -1, -1):
                if current == target_obstacles:
                    break
                if grid[r][c] == 0 and (r, c) not in protected:
                    grid[r][c] = -1
                    current += 1
            if current == target_obstacles:
                break

    assert current == target_obstacles
    return grid


print("=== OBSTACLE DENSITY TESTING ===")
print("Start:", start)
print("Goal:", goal)

for obstacle_count in [15, 20, 25, 30]:

    grid = create_test_grid(obstacle_count)

    print(f"\n=== {obstacle_count} OBSTACLES ===")

    for algorithm in [bfs, ucs, a_star]:
        result = algorithm(grid, start, goal)

        print(
            f"{result['algorithm']:4} | "
            f"Found: {str(result['found']):5} | "
            f"Cost: {result['cost']:2} | "
            f"Steps: {result['steps']:2} | "
            f"Expanded: {result['expanded_nodes']:3} | "
            f"Time: {result['execution_time']:.6f}s"
        )

print("\nOBSTACLE DENSITY TESTING COMPLETED!")
