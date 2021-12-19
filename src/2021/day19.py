import itertools

import numpy as np
from aocd import get_data


def get_possible_vectors(vector):
    vector = np.atleast_2d(vector)
    vector = np.transpose(vector)
    rotations = [
        np.matrix([[1, 0, 0],
                   [0, 1, 0],
                   [0, 0, 1]]),
        np.matrix([[1, 0, 0],
                   [0, 0, -1],
                   [0, 1, 0]]),
        np.matrix([[1, 0, 0],
                   [0, -1, 0],
                   [0, 0, -1]]),
        np.matrix([[1, 0, 0],
                   [0, 0, 1],
                   [0, -1, 0]]),

        np.matrix([[0, -1, 0],
                   [1, 0, 0],
                   [0, 0, 1]]),
        np.matrix([[0, 0, 1],
                   [1, 0, 0],
                   [0, 1, 0]]),
        np.matrix([[0, 1, 0],
                   [1, 0, 0],
                   [0, 0, -1]]),
        np.matrix([[0, 0, -1],
                   [1, 0, 0],
                   [0, -1, 0]]),

        np.matrix([[-1, 0, 0],
                   [0, -1, 0],
                   [0, 0, 1]]),
        np.matrix([[-1, 0, 0],
                   [0, 0, -1],
                   [0, -1, 0]]),
        np.matrix([[-1, 0, 0],
                   [0, 1, 0],
                   [0, 0, -1]]),
        np.matrix([[-1, 0, 0],
                   [0, 0, 1],
                   [0, 1, 0]]),

        np.matrix([[0, 1, 0],
                   [-1, 0, 0],
                   [0, 0, 1]]),
        np.matrix([[0, 0, 1],
                   [-1, 0, 0],
                   [0, -1, 0]]),
        np.matrix([[0, -1, 0],
                   [-1, 0, 0],
                   [0, 0, -1]]),
        np.matrix([[0, 0, -1],
                   [-1, 0, 0],
                   [0, 1, 0]]),

        np.matrix([[0, 0, -1],
                   [0, 1, 0],
                   [1, 0, 0]]),
        np.matrix([[0, 1, 0],
                   [0, 0, 1],
                   [1, 0, 0]]),
        np.matrix([[0, 0, 1],
                   [0, -1, 0],
                   [1, 0, 0]]),
        np.matrix([[0, -1, 0],
                   [0, 0, -1],
                   [1, 0, 0]]),

        np.matrix([[0, 0, -1],
                   [0, -1, 0],
                   [-1, 0, 0]]),
        np.matrix([[0, -1, 0],
                   [0, 0, 1],
                   [-1, 0, 0]]),
        np.matrix([[0, 0, 1],
                   [0, 1, 0],
                   [-1, 0, 0]]),
        np.matrix([[0, 1, 0],
                   [0, 0, -1],
                   [-1, 0, 0]])
    ]
    for r in rotations:
                result = r * vector
                yield tuple((result[0, 0], result[1, 0], result[2, 0]))


def get_possible_vectors_list(vectors):
    iterators = list(map(get_possible_vectors, vectors))
    res = []
    for i in range(24):
        row = set()
        for iterator in iterators:
            row.add(next(iterator))
        res.append(row)
    return res

def test(points, offsets):
    starting_positions = set()
    for point in points:
        for offset in offsets:
            starting_positions.add((point[0] - offset[0], point[1] - offset[1], point[2] - offset[2]))
    for res in starting_positions:
        wrong = 0
        num_correct = 0
        for offset in offsets:
            pos = (res[0] + offset[0], res[1] + offset[1], res[2] + offset[2])
            if pos not in points:
                wrong += 1
                if len(offsets) - wrong < 12:
                    break
            else:
                num_correct += 1
                if num_correct == 12:
                    break
        if num_correct == 12:
            return res
    return None

if __name__ == "__main__":
    data = get_data()
    scanners = [[tuple(map(int, line.split(","))) for line in block.splitlines()[1:]] for block in data.split("\n\n")]
    possible_rotations = list(map(get_possible_vectors_list, scanners))
    positions = {0: (0, 0, 0)}
    orientations = {0: 0}
    probe_positions = {0: scanners[0]}
    dont_test = {0: set()}
    while len(positions) < len(scanners):
        found = False
        for i in range(len(scanners)):
            if i in positions:
                continue
            for j in positions.keys():
                if i in dont_test[j]:
                    continue
                for orientation in range(24):
                    probe_position = test(probe_positions[j], possible_rotations[i][orientation])
                    if probe_position is not None:
                        positions[i] = probe_position
                        orientations[i] = orientation
                        probe_positions[i] = list(map(lambda x: (probe_position[0] + x[0], probe_position[1] + x[1], probe_position[2] + x[2]), possible_rotations[i][orientation]))
                        found = True
                        print(f"Found {i}")
                        dont_test[i] = set()
                        break
                if found:
                    break
                else:
                    dont_test[j].add(i)
            if found:
                break
        if not found:
            break
    probe_set = set()
    for position_list in probe_positions.values():
        for position in position_list:
            probe_set.add(position)
    print(f"Part 1: {len(probe_set)}")
    maximum = 0
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            maximum = max(maximum, abs(positions[i][0] - positions[j][0]) + abs(positions[i][1] - positions[j][1]) + abs(positions[i][2] - positions[j][2]))
    print(f"Part 2: {maximum}")

