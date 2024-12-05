import sys
from pathlib import Path

file = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent / "in"
with open(file, "r") as f:
    lines = f.readlines()

from collections import defaultdict

constraints = defaultdict(set)

cur = 0
while lines[cur].strip():
    # X->Y X happens before Y
    x, y = lines[cur].strip().split("|")
    constraints[y].add(x)
    cur += 1
cur += 1

updates = []
while cur < len(lines):
    updates.append(lines[cur].strip().split(","))
    cur += 1

valid = []
for update in updates:
    contained = set(update)
    processed = set()
    good = True
    for page in update:
        page_constraints = constraints[page].intersection(contained)
        if page_constraints.difference(processed):
            good = False
            break
        processed.add(page)

    if good:
        valid.append(update)

ans = 0
for update in valid:
    middle = update[len(update) // 2]
    ans += int(middle)

print(ans)
