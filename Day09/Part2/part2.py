
file = open("inputP2.txt")
lines = file.read().splitlines()

def getInsertIndex(s,inlen):
    for i in range(len(s)-inlen):
        if not s[i]:
            continue
        if s[i][0] == "." and len(s[i]) >= inlen:
            return i
    return -1

suma = 0
for line in lines:
    midLine = []
    for i,ch in enumerate(line):
        chr = int(i/2) if i % 2 == 0 else "."
        if int(ch) > 0:
            midLine.append([chr for i in range(int(ch))])

    i = len(midLine)-1
    ch = ""
    while i > 0:
        obj = midLine[i]
        if not "." in obj:
            index = getInsertIndex(midLine[:i],len(obj))
            if index != -1:
                oglen = len(midLine[index])
                midLine[index] = midLine[i]
                midLine[i] = ["." for b in range(len(obj))]
                if len(obj) < oglen:
                    if midLine[index+1][0] == ".":
                        midLine[index+1][0] += ["."]*(oglen-len(obj))
                    else:
                        midLine.insert(index+1, ['.' for i in range(oglen-len(obj))])
                    i+=1
        if "." in midLine[i] and i < len(midLine)-1:
            if "." in midLine[i+1]:
                midLine[i] += midLine[i+1]
                midLine.pop(i+1)
        i-=1

print(midLine)
i = 0
for a,obj in enumerate(midLine):
    if not obj:
        continue

    for num in obj:
        if num != ".":
            suma += int(num) * i

        i+=1

print(suma)