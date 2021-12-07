from aocd import get_data


def calc_fuel(target):
    return sum(map(lambda x: abs(target - x), positions))


def calc_fuel2(target):
    return sum(map(lambda x: sum(range(abs(target - x) + 1)), positions))


def find_optimum(low, high, calc_fuel):
    if low == high:
        return calc_fuel(low)
    if low == high - 1:
        low_fuel = calc_fuel(low)
        high_fuel = calc_fuel(high)
        if low_fuel < high_fuel:
            return low_fuel
        else:
            return high_fuel
    middle = (low + high) // 2
    mid_fuel = calc_fuel(middle)
    lower_fuel = calc_fuel(middle - 1)
    if lower_fuel < mid_fuel:
        return find_optimum(low, middle - 1, calc_fuel)
    else:
        return find_optimum(middle, high, calc_fuel)


if __name__ == "__main__":
    positions = [int(i.strip()) for i in get_data().split(",")]
    low = min(positions)
    high = max(positions)
    print(f"Part 1: {find_optimum(low, high, calc_fuel)}")
    print(f"Part 2: {find_optimum(low, high, calc_fuel2)}")
