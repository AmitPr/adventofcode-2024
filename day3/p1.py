import sys
from pathlib import Path

file = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent / "in"
with open(file, "r") as f:
    inst = f.read()

import re

expr = re.compile(r"mul\((\d+),(\d+)\)")

ans = 0
for m in expr.finditer(inst):
    a, b = map(int, m.groups())
    ans += a * b

print(ans)
