from functools import reduce
from operator import mul, add

from aocd import get_data


class Packet:

    def __init__(self, version, type_id, data=None, children=None):
        self.typeId = type_id
        self.version = version
        self.data = data
        self.children = [] if children is None else children


def parse_packet(i):
    version = int(inputNum[i:i + 3], 2)
    i += 3
    type_id = int(inputNum[i:i + 3], 2)
    i += 3
    if type_id == 4:
        num = ""
        while inputNum[i] != "0":
            i += 1
            num += inputNum[i:i + 4]
            i += 4
        i += 1
        num += inputNum[i:i + 4]
        i += 4
        return i, Packet(version, type_id, data=int(num, 2))
    else:
        children = []
        if inputNum[i] == "0":
            i += 1
            total_sub_packet_length = int(inputNum[i:i + 15], 2)
            i += 15
            new_id = i
            while (new_id - i) < total_sub_packet_length:
                new_id, new_child = parse_packet(new_id)
                children.append(new_child)
            i = new_id
        else:
            i += 1
            num_of_sub_packets = int(inputNum[i:i + 11], 2)
            i += 11
            for _ in range(num_of_sub_packets):
                i, new_child = parse_packet(i)
                children.append(new_child)
        return i, Packet(version, type_id, children=children)


def part1(root):
    return sum((part1(c) for c in root.children)) + root.version


def part2(root: Packet):
    if root.typeId == 4:
        return root.data
    child_values = map(part2, root.children)
    if root.typeId == 0:
        return sum(child_values)
    if root.typeId == 1:
        return reduce(mul, child_values, 1)
    if root.typeId == 2:
        return min(child_values)
    if root.typeId == 3:
        return max(child_values)
    if root.typeId == 5:
        return next(child_values) > next(child_values)
    if root.typeId == 6:
        return next(child_values) < next(child_values)
    if root.typeId == 7:
        return next(child_values) == next(child_values)


if __name__ == "__main__":
    data = get_data()
    inputNum = bin(int(data, 16))[2:].zfill(len(data) * 4)
    _, root = parse_packet(0)
    print(f"Part 1: {part1(root)}")
    print(f"Part 2: {part2(root)}")
