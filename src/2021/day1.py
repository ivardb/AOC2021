from aocd import numbers

if __name__ == "__main__":
    part1 = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            part1 += 1
    print(f"Part 1: {part1}")
    part2 = 0
    prev = numbers[0] + numbers[1] + numbers[2]
    for i in range(1, len(numbers)-2):
        cur = prev + numbers[i+2] - numbers[i-1]
        if cur > prev:
            part2 += 1
        prev = cur
    print(f"Part 2: {part2}")
