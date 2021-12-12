from collections import deque
from copy import copy

from aocd import lines


def part1():
    queue = deque()
    queue.append(("start", set()))
    paths = 0
    while queue:
        curr, visited = queue.pop()
        if curr == "end":
            paths += 1
            continue
        if curr[0].islower():
            visited.add(curr)
        for next in adjacent[curr]:
            if next in visited:
                continue
            queue.append((next, copy(visited)))
    print(f"Part 1: {paths}")


def part2():
    queue = deque()
    queue.append(("start", set(), False))
    paths = 0
    while queue:
        curr, visited, doubled = queue.pop()
        if curr == "end":
            paths += 1
            continue
        if curr[0].islower():
            visited.add(curr)
        for next in adjacent[curr]:
            if next in visited:
                if not doubled:
                    queue.append((next, copy(visited), True))
            else:
                queue.append((next, copy(visited), doubled))
    print(f"Part 2: {paths}")


if __name__ == "__main__":
    adjacent = {}
    for line in lines:
        lr = line.split("-")
        left = lr[0]
        right = lr[1]
        if left != "end":
            if left in adjacent:
                adjacent[left].add(right)
            else:
                adjacent[left] = {right}
        if left != "start":
            if right in adjacent:
                adjacent[right].add(left)
            else:
                adjacent[right] = {left}
    part1()
    part2()
