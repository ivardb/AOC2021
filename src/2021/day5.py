from aocd import lines


def run(part2=False):
    counts = {}
    for line in lines:
        coords = line.split("->")
        coord1 = list(coords[0].strip().split(","))
        x1 = int(coord1[0].strip())
        y1 = int(coord1[1].strip())
        coord2 = list(coords[1].strip().split(","))
        x2 = int(coord2[0].strip())
        y2 = int(coord2[1].strip())
        if x1 == x2:
            maxy = max(y1, y2)
            miny = min(y1, y2)
            for y in range(miny, maxy + 1):
                counts[(x1, y)] = counts.get((x1, y), 0) + 1
        elif y1 == y2:
            maxx = max(x1, x2)
            minx = min(x1, x2)
            for x in range(minx, maxx + 1):
                counts[(x, y1)] = counts.get((x, y1), 0) + 1
        else:
            if part2:
                dx = 1
                if x1 > x2:
                    dx = -1
                dy = 1
                if y1 > y2:
                    dy = -1
                x = x1
                y = y1
                counts[(x, y)] = counts.get((x, y), 0) + 1
                while x != x2:
                    x += dx
                    y += dy
                    counts[(x, y)] = counts.get((x, y), 0) + 1
    res = sum(1 for _ in filter(lambda v: v >= 2, counts.values()))
    if part2:
        print(f"Part 2: {res}")
    else:
        print(f"Part 1: {res}")


if __name__ == "__main__":
    run(True)
