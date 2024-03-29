from aocd import lines
import re


class Cube:
    def __init__(self, xs, xe, ys, ye, zs, ze):
        self.xs = xs
        self.xe = xe
        self.ys = ys
        self.ye = ye
        self.zs = zs
        self.ze = ze

    def is_valid(self):
        return self.xs <= self.xe and self.ys <= self.ye and self.zs <= self.ze

    def __int__(self):
        return (self.xe - self.xs + 1) * (self.ye - self.ys + 1) * (self.ze - self.zs + 1)

    def __sub__(self, other):
        # self subset of other
        if other.xs <= self.xs and other.xe >= self.xe and other.ys <= self.ys and other.ye >= self.ye and other.zs <= self.zs and other.ze >= self.ze:
            return []
        # total disjoint
        if self.xs > other.xe or self.xe < other.xs or self.ys > other.ye or self.ye < other.ys or self.zs > other.ze or self.ze < other.zs:
            return [self]
        top_cube = Cube(self.xs, self.xe, self.ys, self.ye, other.ze + 1, self.ze)
        bottom_cube = Cube(self.xs, self.xe, self.ys, self.ye, self.zs, other.zs - 1)
        front_cube = Cube(self.xs, self.xe, self.ys, other.ys - 1, max(other.zs, self.zs), min(self.ze, other.ze))
        back_cube = Cube(self.xs, self.xe, other.ye + 1, self.ye, max(other.zs, self.zs), min(self.ze, other.ze))
        left_cube = Cube(self.xs, other.xs - 1, max(other.ys, self.ys), min(self.ye, other.ye), max(other.zs, self.zs),
                         min(self.ze, other.ze))
        right_cube = Cube(other.xe + 1, self.xe, max(other.ys, self.ys), min(self.ye, other.ye), max(other.zs, self.zs),
                          min(self.ze, other.ze))
        return [cube for cube in (top_cube, bottom_cube, front_cube, back_cube, left_cube, right_cube) if
                cube.is_valid()]

    def __str__(self):
        if self.is_valid():
            return f"Cube of size {self.__int__()}"
        return "invalid"


if __name__ == "__main__":
    activeCubes = []
    lineRegex = r"(on|off) x=(-?\d*)..(-?\d*),y=(-?\d*)..(-?\d*),z=(-?\d*)..(-?\d*)"
    part1 = True
    for line in lines:
        groups = list(re.match(lineRegex, line).groups())
        on = groups[0]
        xs, xe, ys, ye, zs, ze = map(int, groups[1:])
        currentCube = Cube(xs, xe, ys, ye, zs, ze)
        if part1 and any(map(lambda x: abs(x) > 50, (xs, xe, ys, ye, zs, ze))):
            part1 = False
            print(f"Part 1: {sum(map(int, activeCubes))}")
        newActiveCubes = []
        if on == "on":
            currentCubeList = [currentCube]
            for oldCube in activeCubes:
                newCurrentCubeList = []
                for cube in currentCubeList:
                    newCurrentCubeList.extend(cube - oldCube)
                currentCubeList = newCurrentCubeList
                newActiveCubes.append(oldCube)
            newActiveCubes.extend(currentCubeList)
        else:
            for oldCube in activeCubes:
                newActiveCubes.extend(oldCube - currentCube)
        activeCubes = newActiveCubes
    print(f"Part 2: {sum(map(int, activeCubes))}")
