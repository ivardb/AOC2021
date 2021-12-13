import matplotlib.pyplot as plt
from aocd import get_data

if __name__ == "__main__":
    splitted = get_data().split("\n\n")
    points = splitted[0].splitlines()
    folds = splitted[1].splitlines()

    grid = set()
    maxx = 0
    maxy = 0
    for point in points:
        pointsplit = point.split(",")
        x = int(pointsplit[0].strip())
        y = int(pointsplit[1].strip())
        maxx = max(x, maxx)
        maxy = max(x, maxy)
        grid.add((x, y))
    firstFold = True
    for fold in folds:
        foldsplit = fold.split(" ")[2].split("=")
        value = int(foldsplit[1].strip())
        newgrid = set()
        if foldsplit[0] == "x":
            maxx = value
        else:
            maxy = value
        for x, y in grid:
            if foldsplit[0] == "x":
                if x > value:
                    offset = x - value
                    newx = value - offset
                    newgrid.add((newx, y))
                else:
                    newgrid.add((x, y))
            else:
                if y > value:
                    offset = y - value
                    newy = value - offset
                    newgrid.add((x, newy))
                else:
                    newgrid.add((x, y))
        grid = newgrid
        if firstFold:
            print(f"Part 1: {len(grid)}")
            firstFold = False
    finalGrid = []
    for i in range(maxy):
        row = []
        for j in range(maxx):
            row.append((j, i) in grid)
        finalGrid.append(row)
    plt.figure()
    plt.imshow(finalGrid)
    plt.show()

