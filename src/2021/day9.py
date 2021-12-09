from collections import deque
from queue import PriorityQueue

from aocd import lines


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited = set()
    while queue:
        curx, cury = queue.pop()
        visited.add((curx, cury))
        for dx, dy in ([0, 1], [0, -1], [1, 0], [-1, 0]):
            newx = curx + dx
            newy = cury + dy
            if (newx, newy) in visited:
                continue
            if 0 <= newx < len(grid) and 0 <= newy < len(grid[newx]):
                if grid[newx][newy] == 9:
                    continue
                queue.append((newx, newy))
    return len(visited)


if __name__ == "__main__":
    grid = [[int(c) for c in line] for line in lines]
    part1 = 0
    basins = PriorityQueue()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            low = True
            current = grid[i][j]
            for dx, dy in ([0, 1], [0, -1], [1, 0], [-1, 0]):
                x = i + dx
                y = j + dy
                if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
                    if not (current < grid[x][y]):
                        low = False
                        break
            if low:
                part1 += current + 1
                basins.put(-bfs(i, j))
    print(f"Part 1: {part1}")
    part2 = 1
    for _ in range(3):
        part2 *= -basins.get()
    print(f"Part 2: {part2}")
