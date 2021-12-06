from aocd import get_data


def run(days):
    data = list(map(lambda x: int(x.strip()), get_data().split(",")))
    state = {}
    for n in data:
        state[n] = state.get(n, 0) + 1
    for _ in range(days):
        newstate = {}
        for n, c in state.items():
            n -= 1
            if n < 0:
                n = 6
                newstate[8] = c + newstate.get(8, 0)
            newstate[n] = c + newstate.get(n, 0)
        state = newstate
    return sum(state.values())


if __name__ == "__main__":
    print(f"Part 1: {run(80)}")
    print(f"Part 2: {run(256)}")
