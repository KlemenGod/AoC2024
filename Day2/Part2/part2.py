

file = open("inputP2.txt")

text = file.read()

text = text.split("\n")

st = 0

def array_minus(arr):
    ret = []
    for i, el in enumerate(arr):
        ret.append([x for j,x in enumerate(arr) if j is not i])

    return ret

for line in text:
    arr = [int(x) for x in line.split()]
    #smer
#    if arr[0] < arr[1]:
    st += (len(arr) - 1 == sum([1 <= y - x <= 3 for x, y in zip(arr, arr[1:])])) or any([len(arr) - 2 == sum([1 <= y - x <= 3 for x, y in zip(arr_brez, arr_brez[1:])]) for arr_brez in array_minus(arr)])
#    elif arr[0] > arr[1]:
    st += (len(arr) - 1 <= sum([1 <= x - y <= 3 for x, y in zip(arr, arr[1:])])) or any([len(arr) - 2 == sum([1 <= x - y <= 3 for x, y in zip(arr_brez, arr_brez[1:])]) for arr_brez in array_minus(arr)])


print(st)
