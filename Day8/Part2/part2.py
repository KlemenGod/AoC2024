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
        i = 0
        while True:
            point = (ax + i*xdiff,ay+i*ydiff)
            if not(0 <= point[0] < xlen and 0 <= point[1] <ylen):
                break
            ret.add(point)
            i += 1
        i = -1
        while True:
            point = (ax - i*xdiff, ay - i*ydiff)
            if not(0 <= point[0] < xlen and 0 <= point[1] <ylen):
                break
            ret.add(point)
            i -= 1

    return ret

file = open("inputP2.txt")
lines = file.read().splitlines()
antennas = {(x,y) for x,ch in enumerate(lines[0]) for y,l in enumerate(lines) if lines[y][x] != "."}

antinodes = set()
for antenna in antennas:
    antinodes |= possible_antinodes(antenna,antennas)

print(len(antinodes))