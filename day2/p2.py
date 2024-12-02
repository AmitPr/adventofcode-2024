import sys

file = sys.argv[1] if len(sys.argv) > 1 else "day2/in"
with open(file) as f:
    lines = f.readlines()
    reports = [[int(x) for x in line.split(" ")] for line in lines]

safe = []


def is_increasing(report):
    def inner(idx, remaining_skips, last_idx):
        if idx == len(report):
            return True

        last_num = report[last_idx] if last_idx >= 0 else float("-inf")
        current = report[idx]

        is_valid = last_idx < 0 or (current > last_num and (current - last_num <= 3))

        if is_valid and inner(idx + 1, remaining_skips, idx):
            # Keep going
            return True

        if remaining_skips > 0:
            # Skip cur
            return inner(idx + 1, remaining_skips - 1, last_idx)

        return False

    return inner(0, 1, -1)

for report in reports:
    if is_increasing(report) or is_increasing(report[::-1]):
        safe.append(report)

print(len(safe))
