from collections import defaultdict
file = open("inputP1.txt")

def isCorrect(line):
    correct = True
    for i in range(len(line)):
        num = liner[i]
        for a, num2 in enumerate(liner[i + 1:]):
            if num2 in ordering[num]:
                correct = False
    return correct

ordering = defaultdict(lambda: set())
printed = []
temp = file.read().splitlines()
a = True


for line in temp:
    if line == "":
        a = False
        continue

    if a:
        val = line.split("|")[1]
        ordering[line.split("|")[0]].add(val)
    else:
        printed.append(line.split(","))

sum = 0
for line in printed:

    correct = False
    liner = line.copy()
    liner.reverse()
    if isCorrect(liner):
        continue
    while not correct:

        correct = True
        for i in range(len(liner)):
            num = liner[i]
            for a,num2 in enumerate(liner[i+1:]):
                if num2 in ordering[num]:
                    correct = False
                    temp = liner[i]
                    liner[i] = num2
                    liner[a+i+1] = temp

    sum += int(liner[(int(len(line)/2))])



print(sum)
