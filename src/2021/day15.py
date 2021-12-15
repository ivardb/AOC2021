from copy import deepcopy
from queue import PriorityQueue

import numpy as np
from aocd import lines


def heuristic(grid, x, y):
    return (len(grid) - 1 - x) + (len(grid[0]) - 1 - y)


def part1(grid):
    queue = PriorityQueue()
    queue.put((heuristic(grid, 0, 0), heuristic(grid, 0, 0), 0, 0, 0))
    visited = set()
    while queue:
        _, heur, cost, x, y = queue.get()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if heur == 0:
            return cost
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            newx = x + dx
            newy = y + dy
            if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]) and (newx, newy) not in visited:
                newHeur = heuristic(grid, newx, newy)
                newcost = cost + grid[newx][newy]
                queue.put((newcost + newHeur, newHeur, newcost, newx, newy))

def part2():
    tile = np.array([[int(c) for c in row] for row in lines])
    grid = deepcopy(tile)
    for i in range(4):
        tile = (tile + 1) % 10
        tile[tile == 0] = 1
        grid = np.concatenate((grid, tile), axis=1)
    tile = deepcopy(grid)
    for i in range(4):
        tile = (tile + 1) % 10
        tile[tile == 0] = 1
        grid = np.concatenate((grid, tile), axis=0)
    return part1(grid)

if __name__ == "__main__":
    print(f"Part 1: {part1([[int(c) for c in row] for row in lines])}")
    print(f"Part 2: {part2()}")
