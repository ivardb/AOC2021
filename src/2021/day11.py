import numpy as np
from aocd import lines


def check_cell(grid, i, j):
    if grid[i, j] > 9:
        next = []
        grid[i, j] = -1
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == dy == 0:
                    continue
                x = i + dx
                y = j + dy
                if 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1] and grid[x, y] != -1:
                    grid[x, y] += 1
                    if grid[x,y] > 9:
                        next.append((x,y))
        for x, y in next:
            check_cell(grid, x, y)


if __name__ == "__main__":
    grid = np.array([[int(c) for c in line] for line in lines])
    flashes = 0
    round = 0
    while True:
        round += 1
        grid += 1
        roundFlashes = 0
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                check_cell(grid, i, j)
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if grid[i, j] == -1:
                    roundFlashes += 1
                    grid[i, j] = 0
        if roundFlashes == 100:
            print(f"Part 2: {round}")
            break
        flashes += roundFlashes
        if round == 100:
            print(f"Part 1: {flashes}")
