file = open("inputP2.txt")
lines = file.read().splitlines()

def getScore(x,y,map):
    if map[y][x] == "9":
        return 1

    score = 0

    #up
    if y > 0 and map[y-1][x] == str(int(map[y][x])+1):
        score += getScore(x,y-1,map)

    #down
    if y < len(map)-1  and map[y+1][x] == str(int(map[y][x])+1):
        score += getScore(x,y+1,map)

    # left
    if x > 0 and map[y][x-1] == str(int(map[y][x]) + 1):
        score += getScore(x-1, y, map)

    # right
    if x < len(map[0])-1 and map[y][x + 1] == str(int(map[y][x]) + 1):
        score += getScore(x + 1, y, map)

    return score

map = []

for line in lines:
    map.append(list(line))

sc = 0
for y,line in enumerate(map):
    for x,num in enumerate(line):
        if num == "0":
            a = getScore(x,y,map)
            sc += a

print(sc)