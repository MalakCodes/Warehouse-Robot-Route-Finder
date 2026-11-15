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