import time
from copy import copy, deepcopy
from queue import PriorityQueue

from numpy import sign


def validMoves(hallway, rooms):
    res = []
    for x, c in enumerate(hallway):
        if c != ".":
            letter = ord(c) - ord("A")
            roomPos = 2 + 2 * letter
            pos = x
            option = True
            while pos != roomPos:
                pos += sign(roomPos - pos)
                if hallway[pos] != ".":
                    option = False
                    break
            if option and all((rc == "." or rc == c for rc in rooms[letter])):
                depth = 0
                while depth < len(rooms[letter]) and rooms[letter][depth] == ".":
                    cost = (abs(roomPos - x) + depth + 1) * pow(10, letter)
                    newHallway = copy(hallway)
                    newHallway[x] = "."
                    newRooms = deepcopy(rooms)
                    newRooms[letter][depth] = c
                    res.append((cost, newHallway, newRooms))
                    depth += 1
    for ri, room in enumerate(rooms):
        validPos = [0, 1, 3, 5, 7, 9, 10]
        depth = 0
        while depth < len(room) and room[depth] == ".":
            depth += 1
        if depth < len(room):
            if ord(room[depth]) - ord("A") == ri:
                newDepth = depth + 1
                while newDepth < len(room) and room[newDepth] == room[depth]:
                    newDepth += 1
                if newDepth == len(room):
                    continue
            letter = ord(room[depth]) - ord("A")
            hallwayDist = depth + 1
            hallwayPos = 2 + 2 * ri
            currPos = hallwayPos - 1
            while currPos >= 0:
                if hallway[currPos] != '.':
                    break
                if currPos in validPos:
                    cost = (hallwayDist + abs(currPos - hallwayPos)) * pow(10, letter)
                    newHallway = copy(hallway)
                    newHallway[currPos] = room[depth]
                    newRooms = deepcopy(rooms)
                    newRooms[ri][depth] = "."
                    res.append((cost, newHallway, newRooms))
                currPos -= 1
            currPos = hallwayPos + 1
            while currPos < len(hallway):
                if hallway[currPos] != '.':
                    break
                if currPos in validPos:
                    cost = (hallwayDist + abs(currPos - hallwayPos)) * pow(10, letter)
                    newHallway = copy(hallway)
                    newHallway[currPos] = room[depth]
                    newRooms = deepcopy(rooms)
                    newRooms[ri][depth] = "."
                    res.append((cost, newHallway, newRooms))
                currPos += 1
    return res


def run(hallway, rooms):
    queue = PriorityQueue()
    queue.put((0, hallway, rooms))
    visited = set()
    rounds = 0
    while queue:
        rounds += 1
        cost, hallway, rooms = queue.get()
        tH = tuple(hallway)
        tR = tuple(tuple(room) for room in rooms)
        if (tH, tR) in visited:
            continue
        visited.add((tH, tR))
        if all(all(ord(c) - ord("A") == ri for c in room) for ri, room in enumerate(rooms)):
            return cost
        for extraCost, newHallway, newRooms in validMoves(hallway, rooms):
            queue.put((cost + extraCost, newHallway, newRooms))


if __name__ == "__main__":
    start = time.time()
    hallway = ["."] * 11
    roomA = ["C", "B"]
    roomB = ["D", "A"]
    roomC = ["D", "B"]
    roomD = ["A", "C"]
    rooms = [roomA, roomB, roomC, roomD]
    print(f"Part 1: {run(hallway, rooms)}")
    print(f"Runtime : {time.time() - start}s")
    
    start = time.time()
    hallway = ["."] * 11
    roomA = ["C", "D", "D", "B"]
    roomB = ["D", "C", "B", "A"]
    roomC = ["D", "B", "A", "B"]
    roomD = ["A", "A", "C", "C"]
    rooms = [roomA, roomB, roomC, roomD]
    print(f"Part 2: {run(hallway, rooms)}")
    print(f"Runtime : {time.time() - start}s")
