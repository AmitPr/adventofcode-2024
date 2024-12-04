import sys
from pathlib import Path

file = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent / "in"
with open(file, "r") as f:
    lines = f.readlines()

grid = [[c for c in line.strip()] for line in lines]
try_get = lambda x, y: (
    grid[y][x] if 0 <= x < len(grid[0]) and 0 <= y < len(grid) else None
)

expected = set(["M", "S"])


def find(x, y):
    if try_get(x, y) != "A":
        return 0

    diag1 = set([try_get(x - 1, y - 1), try_get(x + 1, y + 1)])
    diag2 = set([try_get(x - 1, y + 1), try_get(x + 1, y - 1)])
    if diag1 == expected and diag2 == expected:
        return 1
    return 0


ans = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        ans += find(x, y)

print(ans)
