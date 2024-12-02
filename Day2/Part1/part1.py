

file = open("inputP1.txt")

text = file.read()

text = text.split("\n")

st = 0
prst = 0
for line in text:
    arr = [int(x) for x in line.split()]
    #smer
    if arr[0] < arr[1]:
        st += len(arr)-1 == sum([1 <= y - x <= 3 for x, y in zip(arr,arr[1:])])
    elif arr[0] > arr[1]:
        st += len(arr) - 1 == sum([1 <= x - y <= 3 for x, y in zip(arr, arr[1:])])


    prst = st
print(st)
