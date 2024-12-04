import re

file = open("inputP2.txt")

text = file.read()

lines = text.split("\n")


found = 0
for i,line in enumerate(lines):
    for a,ch in enumerate(line):

        if i <= len(lines) - 3 and a <= len(line) - 3:
            diag1 = lines[i][a] + lines[i+1][a+1] + lines[i+2][a+2]
            diag2 = lines[i][a+2] + lines[i+1][a+1] + lines[i+2][a]
            if diag1 == "MAS" or diag1 == "SAM":
                if diag2 == "MAS" or diag2 == "SAM":
                    found += 1

print(found)

