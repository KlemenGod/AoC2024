import copy
from collections import defaultdict

file = open("inputP2.txt")

lines = file.read().splitlines()
map = [list(line) for line in lines]

x = y = -1

for yi, line in enumerate(map):
    for xi, ch in enumerate(line):
        if map[yi][xi] in "<>v^":
            x = xi
            y = yi
            break
    if x != -1 and y != -1:
        break


def isLoopedOn(x, y, map):
    player = "^"
    map[y][x] = "."
    while 0 <= x <= len(map[0]) - 1 and 0 <= y <= len(map) - 1:
        if map[y][x] == "#":
            if player == "v":
                y -= 1
                player = "<"
            elif player == "^":
                y += 1
                player = ">"
            elif player == "<":
                x += 1
                player = "^"
            elif player == ">":
                x -= 1
                player = "v"

        if map[y][x] not in "<>^v":
            map[y][x] = player
        elif map[y][x] == player:
            return True

        if player == "v":
            y += 1
        elif player == "^":
            y -= 1
        elif player == "<":
            x -= 1
        elif player == ">":
            x += 1
    return False


sum = 0

for yi in range(len(map)):
    for xi in range(len(map[0])):
        mapc = copy.deepcopy(map)
        mapc[yi][xi] = "#"
        if isLoopedOn(x,y,mapc):
            sum += 1

print(sum)


