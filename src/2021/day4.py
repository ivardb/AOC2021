from aocd import get_data

def part1(cards, nums):
    done = False
    while not done:
        num = next(nums)
        for card in cards:
            for line in card:
                if num in line:
                    line.remove(num)
                if len(line) == 0:
                    done = True
            if done:
                rem = set.union(*card)
                print(f"Part 1: {sum(rem) * num}")
                break


def part2(cards, nums):
    while len(cards) > 1:
        num = next(nums)
        remove = []
        for card in cards:
            for line in card:
                if num in line:
                    line.remove(num)
                if len(line) == 0:
                    remove.append(card)
                    break
        for r in remove:
            cards.remove(r)
    done = False
    while not done:
        num = next(nums)
        for card in cards:
            for line in card:
                if num in line:
                    line.remove(num)
                if len(line) == 0:
                    done = True
            if done:
                rem = set.union(*card)
                print(f"Part 2: {sum(rem) * num}")
                break


if __name__ == "__main__":
    data = get_data()
    blocks = iter(data.split("\n\n"))
    nums = (int(n.strip()) for n in next(blocks).split(","))
    cards = []
    for block in blocks:
        grid = []
        for line in block.splitlines():
            row = []
            for n in line.strip().split():
                row.append(int(n.strip()))
            grid.append(row)
        bingo = []
        for row in grid:
            bingo.append(set(row))
        for i in range(len(grid[0])):
            col = set()
            for row in grid:
                col.add(row[i])
            bingo.append(col)
        cards.append(bingo)
    part2(cards, nums)

