
from warehouse_grid import create_warehouse_grid, START, GOAL
from ucs import ucs
from a_star import a_star

# Test 1: Reachable Goal
grid = [
    [0, 0, 0, 0, 0],
    [0, -1, -1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, -1, -1, -1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

result = a_star(grid, start, goal)

print("=== Reachable Goal Test ===")
for key, value in result.items():
    print(f"{key}: {value}")

assert result["found"] is True
assert result["steps"] == 8
print("PASS: A* found a valid path.")


# Test 2: Weighted Aisle
weighted_grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 3, 3, 3, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (2, 0)
goal = (2, 4)

result = a_star(weighted_grid, start, goal)

print("\n=== Weighted Aisle Test ===")
for key, value in result.items():
    print(f"{key}: {value}")

assert result["found"] is True
assert result["cost"] == 6
print("PASS: A* found the minimum-cost path.")


# Test 3: No Valid Route
blocked_grid = [
    [0, 0, 0],
    [-1, -1, -1],
    [0, 0, 0]
]

start = (0, 0)
goal = (2, 2)

result = a_star(blocked_grid, start, goal)

print("\n=== No Valid Route Test ===")
for key, value in result.items():
    print(f"{key}: {value}")

assert result["found"] is False
assert result["path"] == []
print("PASS: A* correctly detected no valid route.")


# Test 4: A* vs UCS
grid = create_warehouse_grid()

astar_result = a_star(grid, START, GOAL)
ucs_result = ucs(grid, START, GOAL)

print("\n=== A* vs UCS Comparison ===")
print("A* Cost:", astar_result["cost"])
print("UCS Cost:", ucs_result["cost"])
print("Same Minimum Cost:", astar_result["cost"] == ucs_result["cost"])
print("A* Expanded Nodes:", astar_result["expanded_nodes"])
print("UCS Expanded Nodes:", ucs_result["expanded_nodes"])

assert astar_result["found"] is True
assert ucs_result["found"] is True
assert astar_result["cost"] == ucs_result["cost"]

print("\nALL A* TESTS PASSED!")
