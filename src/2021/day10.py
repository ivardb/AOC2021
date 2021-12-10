from aocd import lines


def complete(stack):
    scores = {")": 1, "]": 2, "}": 3, ">": 4}
    matching = {"(": ")", "<": ">", "{": "}", "[": "]"}
    res = 0
    while stack:
        c = stack.pop()
        res *= 5
        res += scores[matching[c]]
    return res


if __name__ == "__main__":
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    matching = {")": "(", ">": "<", "}": "{", "]": "["}
    part1 = 0
    part2 = []
    for line in lines:
        stack = []
        finished = True
        for c in line:
            if c not in matching:
                stack.append(c)
            else:
                match = stack.pop()
                if matching[c] != match:
                    part1 += scores[c]
                    finished = False
                    break
        if stack and finished:
            part2.append(complete(stack))
    print(f"Part 1: {part1}")
    sortedscores = sorted(part2)
    print(f"Part 2: {sortedscores[len(sortedscores)//2]}")
