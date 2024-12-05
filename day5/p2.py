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

invalid = []
for update in updates:
    contained, processed = set(update), set()
    for page in update:
        page_constraints = constraints[page].intersection(contained)
        if page_constraints.difference(processed):
            invalid.append(update)
            break
        processed.add(page)

unsatisfied = (
    lambda page, contained, processed: constraints[page]
    .intersection(contained)
    .difference(processed)
)


def settle(needed, fixed, processed, moving):
    stop = True
    while True:
        needed_l = list(needed)
        for npage in needed_l:
            if not unsatisfied(npage, contained, processed):
                stop = False
                fixed.append(npage)
                processed.add(npage)
                needed.remove(npage)
                moving.remove(npage)
        if stop or not needed:
            break
    return not needed

res = []
for update in invalid:
    contained, processed = set(update), set()
    moving = set()
    fixed = []
    for page in update:
        needed = unsatisfied(page, contained, processed)
        if needed:
            # page has unsatisfied constraints
            if needed.issubset(moving):
                # all prerequisites are moving, can try placing them first.
                if settle(needed, fixed, processed, moving):
                    fixed.append(page)
                    processed.add(page)
            else:
                moving.add(page)
        else:
            processed.add(page)
            fixed.append(page)
    settle(moving.copy(), fixed, processed, moving)
    res.append(fixed)

ans = 0
for r in res:
    ans += int(r[len(r)//2])

print(ans)