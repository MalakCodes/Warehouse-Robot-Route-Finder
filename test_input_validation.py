
from warehouse_grid import create_warehouse_grid
from input_validation import validate_position

grid = create_warehouse_grid()

test_cases = [
    ("Valid Position", (0, 1), True),
    ("Outside Grid", (10, 5), False),
    ("Negative Position", (-1, 2), False),
    ("Obstacle Position", (1, 2), False),
    ("Invalid Type", [0, 1], False),
    ("Missing Coordinate", (0,), False),
    ("Non-Integer Coordinate", (1.5, 2), False),
]

print("=== INPUT VALIDATION TESTING ===")

passed = 0

for name, position, expected in test_cases:
    actual = validate_position(grid, position)

    status = "PASS" if actual == expected else "FAIL"

    if status == "PASS":
        passed += 1

    print(f"{name}: {status}")

print(f"\nTotal Passed: {passed}/{len(test_cases)}")

assert passed == len(test_cases), "Some tests failed!"

print("ALL INPUT VALIDATION TESTS PASSED!")
