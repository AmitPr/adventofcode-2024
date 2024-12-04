import sys
from pathlib import Path

file = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent / "in"
with open(file, "r") as f:
    lines = f.readlines()

grid = [[c for c in line.strip()] for line in lines]
letters = ['X', 'M', 'A', 'S']
directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

def find(x, y, dx,dy, cur = 'X'):
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
        return 0
    
    if grid[y][x] != cur:
        return 0

    if cur == 'S':
        return 1
    
    nx,ny = x+dx, y+dy
    return find(nx, ny, dx, dy, letters[letters.index(cur)+1])

ans = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        for dx, dy in directions:
            ans += find(x, y, dx, dy)

print(ans)
    