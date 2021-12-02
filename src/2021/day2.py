from aocd import lines


def part1():
    horizontal = 0
    depth = 0
    for line in lines:
        splitted = line.split(" ")
        value = int(splitted[1])
        if splitted[0] == "down":
            depth += value
        elif splitted[0] == "up":
            depth -= value
        else:
            horizontal += value
    print(f"Part 1: {horizontal * depth}")


def part2():
    horizontal = 0
    depth = 0
    aim = 0
    for line in lines:
        splitted = line.split(" ")
        value = int(splitted[1])
        if splitted[0] == "down":
            aim += value
        elif splitted[0] == "up":
            aim -= value
        else:
            horizontal += value
            depth += aim * value
    print(f"Part 2: {horizontal * depth}")


if __name__ == "__main__":
    part2()
