from collections import defaultdict
file = open("inputP1.txt")

lines = file.read().splitlines()
map = [list(line) for line in lines]

x = y = -1

for yi,line in enumerate(map):
    for xi, ch in enumerate(line):
        if map[yi][xi] in "<>v^":
            x = xi
            y = yi
            break
    if x != -1 and y != -1:
        break

curr = "^"
sum = 0
while 0 <= x <= len(map[0])-1 and 0 <= y <= len(map)-1:

    if map[y][x] == "#":
        if curr == "v":
            y -= 1
            curr = "<"
        elif curr == "^":
            y += 1
            curr = ">"
        elif curr == "<":
            x += 1
            curr = "^"
        elif curr == ">":
            x -= 1
            curr = "v"

    if map[y][x] != "X":
        sum += 1
        map[y][x] = "X"



    if curr == "v":
        y += 1
    elif curr == "^":
        y -= 1
    elif curr == "<":
        x -= 1
    elif curr == ">":
        x += 1

print(sum)