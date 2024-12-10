

file = open("inputP2.txt")

text = file.read()

text = text.split("\n")

arr1 = []
arr2 = []
for line in text:
    arr1.append(line.split(" ")[0])
    arr2.append(line.split(" ")[3])

print(sum([abs(int(x)*arr2.count(x)) for x in arr1]))
