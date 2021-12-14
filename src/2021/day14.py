from copy import copy
from functools import lru_cache

from aocd import lines


@lru_cache(maxsize=None)
def get_counts(l, r, d):
    new = rules[l + r]
    if d == 1:
        res = {}
        for c in (l, r, new):
            res[c] = res.get(c, 0) + 1
        return res
    h1 = get_counts(l, new, d - 1)
    h2 = get_counts(new, r, d - 1)
    h3 = copy(h1)
    for k, v in h2.items():
        h3[k] = h3.get(k, 0) + v
    h3[new] = h3[new] - 1
    return h3


def count_sentence(start, depth):
    counts = {}
    for i in range(1, len(start)):
        newcounts = get_counts(start[i - 1], start[i], depth)
        for k, v in newcounts.items():
            counts[k] = counts.get(k, 0) + v
    for c in start[1:-1]:
        counts[c] = counts[c] - 1
    maxVal = 0
    minVal = float("inf")
    for v in counts.values():
        maxVal = max(maxVal, v)
        minVal = min(minVal, v)
    return maxVal - minVal


if __name__ == "__main__":
    start = lines[0]
    rules = {}
    for line in lines[2:]:
        splitted = line.split(" -> ")
        pattern = splitted[0].strip()
        output = splitted[1].strip()
        rules[pattern] = output
    print(f"Part 1: {count_sentence(start, 10)}")
    print(f"Part 2: {count_sentence(start, 40)}")
