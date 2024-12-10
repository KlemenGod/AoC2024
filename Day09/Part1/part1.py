
file = open("inputP1.txt")
lines = file.read().splitlines()

def popLastNum(s):
    i = len(s)-1
    while i>0:
        if s[i] != ".":
            ret = s[i]
            s[i] = "."
            return i,ret
        i-=1
    return False

suma = 0
for line in lines:
    midLine = []
    for i,ch in enumerate(line):
        chr = int(i/2) if i % 2 == 0 else "."
        midLine+=[chr for i in range(int(ch))]

    i = 0
    ch = ""
    while i < len(midLine):
        ch = midLine[i]

        if ch == ".":
            a,num = popLastNum(midLine)
            if a < i:
                midLine[i-1] = num
                break
            midLine[i] = num
        i+=1
    #midLine = [x for x in midLine if x != "."]

    suma += sum([i*int(ch) for i,ch in enumerate(midLine) if ch != "."])

print(suma)