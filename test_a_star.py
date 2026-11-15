from warehouse_grid import create_warehouse_grid, START, GOAL
from ucs import ucs
from a_star import a_star

grid = [
["R", ".", ".", ".", "."],
[".", "X", "X", ".", "."],
[".", ".", ".", ".", "."],
[".", "X", "X", "X", "."],
[".", ".", ".", ".", "G"]
]

start = (0, 0)
goal = (4, 4)

result = a_star(grid, start, goal)

print("Reachable Goal Test")
print("-------------------")

for key, value in result.items():
    print(f"{key}: {value}")

print("\nWeighted Aisle Test")
print("-------------------")

weighted_grid = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    ["R", "H", "H", "H", "G"],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."]
]

start = (2, 0)
goal = (2, 4)

result = a_star(weighted_grid, start, goal)

for key, value in result.items():
    print(f"{key}: {value}")


print("\nNo Valid Route Test")
print("-------------------")

blocked_grid = [
    ["R", ".", "."],
    ["X", "X", "X"],
    [".", ".", "G"]
]

start = (0, 0)
goal = (2, 2)

result = a_star(blocked_grid, start, goal)

for key, value in result.items():
    print(f"{key}: {value}")

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
