import numpy as np
from aocd import lines

if __name__ == "__main__":
    grid = np.array([[c for c in line] for line in lines])
    step = 0
    while True:
        step += 1
        newGrid = np.full(grid.shape, ".")
        updated = False
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if grid[i, j] == ">":
                    if grid[i, (j + 1) % grid.shape[1]] == ".":
                        newGrid[i, (j + 1) % grid.shape[1]] = ">"
                        updated = True
                    else:
                        newGrid[i,j] = ">"
                if grid[i, j] == "v":
                    newGrid[i, j] = "v"
        grid = newGrid
        newGrid = np.full(grid.shape, ".")
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if grid[i, j] == "v":
                    if grid[(i + 1) % grid.shape[0], j] == ".":
                        newGrid[(i + 1) % grid.shape[0], j] = "v"
                        updated = True
                    else:
                        newGrid[i,j] = "v"
                if grid[i, j] == ">":
                    newGrid[i, j] = ">"
        grid = newGrid
        if not updated:
            break
    print(f"Part 1: {step}")