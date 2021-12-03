from copy import copy

from aocd import lines


def count_pos(data, index):
    ones = sum(row[index] for row in data)
    zeros = len(data) - ones
    return ones, zeros


def part1(data):
    gamma = ""
    epsilon = ""
    for i in range(len(data[0])):
        ones, zeros = count_pos(data, i)
        if ones > zeros:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    print(f"Part 1: {int(gamma, 2) * int(epsilon, 2)}")


def part2(data):
    ox = copy(data)
    i = 0
    while len(ox) > 1:
        ones, zeros = count_pos(ox, i)
        if ones >= zeros:
            ox = list(filter(lambda x: x[i] == 1, ox))
        else:
            ox = list(filter(lambda x: x[i] == 0, ox))
        i+=1
    co2 = copy(data)
    i = 0
    while len(co2) > 1:
        ones, zeros = count_pos(co2, i)
        if zeros <= ones:
            co2 = list(filter(lambda x: x[i] == 0, co2))
        else:
            co2 = list(filter(lambda x: x[i] == 1, co2))
        i+=1
    print(f"Part 2: {int(''.join(str(o) for o in ox[0]), 2) * int(''.join(str(o) for o in co2[0]), 2)}")


if __name__ == "__main__":
    data = [[int(c) for c in line] for line in lines]
    part1(data)
    part2(data)
