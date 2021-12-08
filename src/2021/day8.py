from aocd import lines


def decipher_line(line):
    hints, res = parse_line(line)
    normal = {frozenset({"A", "B", "C", "E", "F", "G"}): 0,
              frozenset({"C", "F"}): 1,
              frozenset({"A", "C", "D", "E", "G"}): 2,
              frozenset({"A", "C", "D", "F", "G"}): 3,
              frozenset({"B", "C", "D", "F"}): 4,
              frozenset({"A", "B", "D", "F", "G"}): 5,
              frozenset({"A", "B", "D", "E", "F", "G"}): 6,
              frozenset({"A", "C", "F"}): 7,
              frozenset({"A", "B", "C", "D", "E", "F", "G"}): 8,
              frozenset({"A", "B", "C", "D", "F", "G"}): 9}
    mapping = {}
    frequencies = [0, 0, 0, 0, 0, 0, 0]
    four = None
    one = None
    for hint in hints:
        for c in hint:
            frequencies[ord(c) - ord('a')] += 1
        if len(hint) == 2:
            one = hint
        if len(hint) == 4:
            four = hint
    for i, freq in enumerate(frequencies):
        if freq == 6:
            mapping[chr(i + ord('a'))] = "B"
        elif freq == 4:
            mapping[chr(i + ord('a'))] = "E"
        elif freq == 9:
            mapping[chr(i + ord('a'))] = "F"
        elif freq == 7:
            letter = chr(i + ord('a'))
            if letter in four:
                mapping[letter] = "D"
            else:
                mapping[letter] = "G"
        elif freq == 8:
            letter = chr(i + ord('a'))
            if letter in one:
                mapping[letter] = "C"
            else:
                mapping[letter] = "A"
    return int("".join(str(normal[frozenset((mapping[c] for c in r))]) for r in res))


def parse_line(line):
    lr_split = line.split("|")
    hints = [set(c for c in hint) for hint in lr_split[0].strip().split(" ")]
    res = [set(c for c in ans) for ans in lr_split[1].strip().split(" ")]
    return hints, res


if __name__ == "__main__":
    output = list(map(decipher_line, lines))
    part1 = 0
    for out in output:
        for c in str(out):
            if c == "1" or c == "4" or c == "7" or c == "8":
                part1 += 1
    print(f"Part 1: {part1}")
    print(f"Part 2: {sum(output)}")
