from warehouse_grid import create_warehouse_grid, START, GOAL
from ucs import ucs
from a_star import a_star


# ==================================
# Test 1: Reachable Goal Test
# ==================================

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

print("Reachable Goal Test")
print("-------------------")

for key, value in result.items():
    print(f"{key}: {value}")

assert result["found"] is True
assert result["path"][0] == start
assert result["path"][-1] == goal

print("PASS: A* found a valid route.")


# ==================================
# Test 2: Weighted Aisle Test
# ==================================

print("\nWeighted Aisle Test")
print("-------------------")

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

for key, value in result.items():
    print(f"{key}: {value}")

assert result["found"] is True
assert result["cost"] == 6
assert result["steps"] == 6

print("PASS: A* avoided the high-cost cells.")


# ==================================
# Test 3: No Valid Route Test
# ==================================

print("\nNo Valid Route Test")
print("-------------------")

blocked_grid = [
    [0, 0, 0],
    [-1, -1, -1],
    [0, 0, 0]
]

start = (0, 0)
goal = (2, 2)

result = a_star(blocked_grid, start, goal)

for key, value in result.items():
    print(f"{key}: {value}")

assert result["found"] is False
assert result["path"] == []
assert result["cost"] == 0

print("PASS: A* correctly detected no valid route.")


# ==================================
# Test 4: A* vs UCS Comparison
# ==================================

print("\nA* vs UCS Comparison")
print("--------------------")

grid = create_warehouse_grid()

astar_result = a_star(grid, START, GOAL)
ucs_result = ucs(grid, START, GOAL)

print("A* Cost:", astar_result["cost"])
print("UCS Cost:", ucs_result["cost"])

print(
    "Same Minimum Cost:",
    astar_result["cost"] == ucs_result["cost"]
)

print("A* Expanded Nodes:", astar_result["expanded_nodes"])
print("UCS Expanded Nodes:", ucs_result["expanded_nodes"])

print("A* Execution Time:", astar_result["execution_time"])
print("UCS Execution Time:", ucs_result["execution_time"])

assert astar_result["found"] is True
assert ucs_result["found"] is True
assert astar_result["cost"] == ucs_result["cost"]

print("\nALL A* TESTS PASSED!")
