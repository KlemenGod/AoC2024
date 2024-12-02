

file = open("inputP1.txt")

text = file.read()

text = text.split("\n")

arr1 = []
arr2 = []
for line in text:
    arr1.append(line.split(" ")[0])
    arr2.append(line.split(" ")[3])


print(sum([abs(int(x)-int(y)) for x, y in zip(sorted(arr1), sorted(arr2))]))
