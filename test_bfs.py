
from bfs import bfs

# Test 1: Reachable Goal
grid1 = [
    [0, 0, 0, 0, 0],
    [0, -1, -1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, -1, -1, -1, 0],
    [0, 0, 0, 0, 0]
]

result1 = bfs(grid1, (0, 0), (4, 4))

print("=== BFS Reachable Goal Test ===")
print("Found:", result1["found"])
print("Cost:", result1["cost"])
print("Steps:", result1["steps"])
print("Path:", result1["path"])

assert result1["found"] is True
assert result1["steps"] == 8

print("PASS: BFS found a shortest path.")


# Test 2: Weighted Cells
weighted_grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 3, 3, 3, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

result2 = bfs(weighted_grid, (2, 0), (2, 4))

print("\n=== BFS Weighted Cells Test ===")
print("Found:", result2["found"])
print("Cost:", result2["cost"])
print("Steps:", result2["steps"])
print("Path:", result2["path"])

assert result2["found"] is True
assert result2["steps"] == 4
assert result2["cost"] == 10

print("PASS: BFS selected the minimum-step path.")


# Test 3: Same Start and Goal
result3 = bfs([[0, 0], [0, 0]], (0, 0), (0, 0))

print("\n=== BFS Same Start and Goal Test ===")
print("Found:", result3["found"])
print("Path:", result3["path"])
print("Steps:", result3["steps"])
print("Cost:", result3["cost"])

assert result3["found"] is True
assert result3["steps"] == 0
assert result3["cost"] == 0

print("PASS: BFS handled the same start and goal.")

print("\nALL BFS TESTS PASSED!")
