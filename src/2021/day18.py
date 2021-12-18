import functools
import math
from copy import deepcopy

from aocd import lines


class Pair:
    def __init__(self, num=None, left=None, right=None):
        self.num = num
        self.left = left
        self.right = right
        self.parent = None
        self.leftNode = None
        self.rightNode = None

    def __str__(self):
        if self.num is not None:
            return str(self.num)
        return f"[{self.left}, {self.right}]"

    def __deepcopy__(self, memodict={}):
        if self.num is not None:
            return Pair(self.num)
        return Pair(left=deepcopy(self.left), right=deepcopy(self.right))


def make_linked(pair):
    if pair.num is not None:
        return pair, pair
    head1, tail1 = make_linked(pair.left)
    head2, tail2 = make_linked(pair.right)
    head2.leftNode = tail1
    tail1.rightNode = head2
    return head1, tail2


def add_num(num1, num2):
    res = Pair(None, left=num1, right=num2)
    num1.parent = res
    num2.parent = res
    return reduced(res)


def reduced(pair):
    linked_list = make_linked(pair)
    while True:
        if explode(pair):
            continue
        if not split(pair):
            break
    return pair


def split(pair):
    if pair.num is not None:
        if pair.num > 9:
            floored = math.floor(pair.num / 2)
            ceiled = math.ceil(pair.num / 2)
            pair.left = Pair(num=floored)
            pair.right = Pair(num=ceiled)

            pair.left.leftNode = pair.leftNode
            if pair.leftNode is not None:
                pair.leftNode.rightNode = pair.left

            pair.left.rightNode = pair.right
            pair.right.leftNode = pair.left
            pair.right.rightNode = pair.rightNode
            if pair.rightNode is not None:
                pair.rightNode.leftNode = pair.right
            pair.num = None
            return True
    else:
        return split(pair.left) or split(pair.right)


def explode(pair, counter=0):
    if pair.num is not None:
        return False
    if counter < 4:
        return explode(pair.left, counter + 1) or explode(pair.right, counter + 1)
    add_left(pair.left, pair.left.num)
    add_right(pair.right, pair.right.num)

    pair.leftNode = pair.left.leftNode
    if pair.leftNode is not None:
        pair.leftNode.rightNode = pair

    pair.rightNode = pair.right.rightNode
    if pair.rightNode is not None:
        pair.rightNode.leftNode = pair

    pair.left = None
    pair.right = None
    pair.num = 0
    return True


def add_left(pair, val):
    if pair.leftNode is not None:
        pair.leftNode.num += val


def add_right(pair, val):
    if pair.rightNode is not None:
        pair.rightNode.num += val


def parse_num(line: str, index=0):
    if line[index].isdigit():
        num = int(line[index])
        index += 1
        return index, Pair(num=num)
    index += 1
    index, left = parse_num(line, index)
    index += 1
    index, right = parse_num(line, index)
    index += 1
    pair = Pair(left=left, right=right)
    left.parent = pair
    right.parent = pair
    return index, pair


def magnitude(pair):
    if pair.num is not None:
        return pair.num
    return 3 * magnitude(pair.left) + 2 * magnitude(pair.right)


if __name__ == "__main__":
    numbers = [parse_num(line)[1] for line in lines]
    final = functools.reduce(add_num, numbers)
    print(f"Part 1: {magnitude(final)}")
    numbers = [parse_num(line)[1] for line in lines]
    maxMagnitude = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            maxMagnitude = max(magnitude(add_num(deepcopy(numbers[i]), deepcopy(numbers[j]))), maxMagnitude)
    print(f"Part 2: {maxMagnitude}")
