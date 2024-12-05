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


unsatisfied = (
    lambda page, contained, processed: constraints[page]
    .intersection(contained)
    .difference(processed)
)

invalid = []
for update in updates:
    contained, processed = set(update), set()
    for page in update:
        if unsatisfied(page, contained, processed):
            invalid.append(update)
            break
        processed.add(page)


ans = 0
for update in invalid:
    contained = set(update)
    while True:
        processed = set()
        cont = False
        for i, page in enumerate(update):
            needed = unsatisfied(page, contained, processed)
            if needed:
                j = update.index(needed.pop())
                update[i], update[j] = update[j], update[i]
                cont = True
                break
            processed.add(page)
        if not cont:
            ans += int(update[len(update) // 2])
            break

print(ans)
