import re

file = open("inputP1.txt")

text = file.read()

lines = text.split("\n")


found = 0
for i,line in enumerate(lines):
    for a,ch in enumerate(line):
        if line[a:a + 4] == "XMAS" or line[a:a + 4] == "SAMX":
            found += 1

        if i <= len(lines) - 4:
            if lines[i][a]+lines[i+1][a]+lines[i+2][a]+lines[i+3][a] == "XMAS" or lines[i][a]+lines[i+1][a]+lines[i+2][a]+lines[i+3][a] == "SAMX":
                found += 1

        if i <= len(lines)-4 and a <= len(line) -4:
            if lines[i][a]+lines[i+1][a+1]+lines[i+2][a+2]+lines[i+3][a+3] == "XMAS" or lines[i][a]+lines[i+1][a+1]+lines[i+2][a+2]+lines[i+3][a+3] == "SAMX":
                found += 1
        if i <= len(lines) - 4 and a >= 3:
            if lines[i][a]+lines[i+1][a-1]+lines[i+2][a-2]+lines[i+3][a-3] == "XMAS" or lines[i][a]+lines[i+1][a-1]+lines[i+2][a-2]+lines[i+3][a-3] == "SAMX":
                found += 1

print(found)

