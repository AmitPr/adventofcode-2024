import sys
from pathlib import Path

file = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent / "in"
with open(file, "r") as f:
    inst = f.read()

import re

mul = r"mul\((\d+),(\d+)\)"
do = r"do\(\)"
dont = r"don't\(\)"
expr = re.compile(f"({mul}|{do}|{dont})")

ans = 0
enable = True
for i in expr.finditer(inst):
    if "mul" in i.group(1):
        a, b = map(int, i.groups()[1:])
        if enable:
            ans += a * b
    elif "don't" in i.group(1):
        enable = False
    elif "do" in i.group(1):
        enable = True

print(ans)
