def possible_antinodes(antenna,antennas):
    xlen = len(lines[0])
    ylen = len(lines)

    ax,ay = antenna
    ret = set()
    for (x,y) in antennas:
        if lines[y][x] != lines[ay][ax] or (x,y) == antenna:
            continue

        xdiff = ax-x
        ydiff = ay-y
        ret.add((ax + xdiff,ay+ydiff))
        ret.add((ax - 2*xdiff, ay - 2*ydiff))

    return {(x,y) for x,y in ret if 0 <= x < xlen and 0 <= y <ylen}

file = open("inputP1.txt")
lines = file.read().splitlines()
antennas = {(x,y) for x,ch in enumerate(lines[0]) for y,l in enumerate(lines) if lines[y][x] != "."}

antinodes = set()
for antenna in antennas:
    antinodes |= possible_antinodes(antenna,antennas)

print(len(antinodes))