from functools import lru_cache


def part1():
    p1 = 4
    p2 = 9
    dice = 1
    s1 = 0
    s2 = 0
    turn1 = True
    r = 0
    while True:
        roll = dice
        dice = dice % 100 + 1
        roll += dice
        dice = dice % 100 + 1
        roll += dice
        dice = dice % 100 + 1
        r += 3
        if turn1:
            p1 = (p1 + roll - 1) % 10 + 1
            s1 += p1
            if s1 >= 1000:
                print(f"Part 1: {s2 * r}")
                break
        else:
            p2 = (p2 + roll - 1) % 10 + 1
            s2 += p2
            if s2 >= 1000:
                print(f"Part 1: {s1 * r}")
                break
        turn1 = not turn1


@lru_cache(maxsize=None)
def play(p1, p2, s1, s2, turn1):
    if s1 >= 21:
        return 1, 0
    if s2 >= 21:
        return 0, 1
    total1 = 0
    total2 = 0
    if turn1:
        for roll, multiplier in ((3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)):
            n1 = (p1 + roll - 1) % 10 + 1
            w1, w2 = play(n1, p2, s1 + n1, s2, not turn1)
            total1 += multiplier * w1
            total2 += multiplier * w2
    else:
        for roll, multiplier in ((3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)):
            n2 = (p2 + roll - 1) % 10 + 1
            w1, w2 = play(p1, n2, s1, s2 + n2, not turn1)
            total1 += multiplier * w1
            total2 += multiplier * w2
    return total1, total2


def part2():
    p1 = 4
    p2 = 9
    s1 = 0
    s2 = 0
    turn1 = True
    w1, w2 = play(p1, p2, s1, s2, turn1)
    print(f"Part 2: {max(w1, w2)}")


if __name__ == "__main__":
    part1()
    part2()
