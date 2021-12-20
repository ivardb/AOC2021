from aocd import lines


def run(rounds):
    minx = 0
    maxx = len(image)
    miny = 0
    maxy = len(image[0])
    grid = {}
    for i in range(len(image)):
        for j in range(len(image[0])):
            grid[(i, j)] = int(image[i][j] == "#")
    for r in range(rounds):
        minx -= 1
        maxx += 1
        miny -= 1
        maxy += 1
        if algorithm[0] == 1:
            default = 0 if r % 2 == 0 else 1
        else:
            default = 0
        newGrid = {}
        for x in range(minx, maxx):
            for y in range(miny, maxy):
                number = ""
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        number += str(grid.get((x + dx, y + dy), default))
                newGrid[(x, y)] = algorithm[int(number, 2)]
        grid = newGrid
    return sum(grid.values())


if __name__ == "__main__":
    algorithm = [1 if c == "#" else 0 for c in lines[0]]
    image = lines[2:]
    print(f"Part 1: {run(2)}")
    print(f"Part 2: {run(50)}")
