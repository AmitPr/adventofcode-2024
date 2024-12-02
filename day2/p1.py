import itertools

with open("day2/in") as f:
    lines = f.readlines()
    reports = [[int(x) for x in line.split(" ")] for line in lines]

safe = []
for report in reports:
    s = sorted(report)
    if s == report or s[::-1] == report:
        # increasing or decreasing
        diffs = [
            abs(a - b)
            for (a, b) in itertools.zip_longest(report, report[1:], fillvalue=0)
        ][:-1]
        if max(diffs) < 4 and min(diffs) > 0:
            print(report)
            safe.append(report)

print(len(safe))
