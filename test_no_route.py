
from warehouse_grid import create_warehouse_grid, START, STORAGE_ZONES
from bfs import bfs
from ucs import ucs
from a_star import a_star

# Create an independent test grid
grid = create_warehouse_grid()

# Block both entrances to S1
grid[0][8] = -1
grid[1][9] = -1

start = START
goal = STORAGE_ZONES["S1"]

algorithms = [bfs, ucs, a_star]

print("=== TEST 10: NO VALID ROUTE ===")
print("Start:", start)
print("Goal:", goal)
print("Blocked Cells: (0,8), (1,9)")

for algorithm in algorithms:
    result = algorithm(grid, start, goal)

    print(f"\n--- {result['algorithm']} ---")
    print("Route Found:", result["found"])
    print("Path:", result["path"])
    print("Total Cost:", result["cost"])
    print("Steps:", result["steps"])
    print("Expanded Nodes:", result["expanded_nodes"])
    print("Execution Time:", result["execution_time"])

    assert result["found"] is False
    assert result["path"] == []
    assert result["cost"] == 0
    assert result["steps"] == 0

    print(f"PASS: {result['algorithm']} correctly detected no valid route.")

print("\nALL NO VALID ROUTE TESTS PASSED!")


