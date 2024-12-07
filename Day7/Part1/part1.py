from collections import defaultdict
file = open("inputP1.txt")

lines = file.read().splitlines()


def canDo(list, num):
    if len(list) == 2:
        if list[0] * list[1] == num:
            return True
        elif list[0] + list[1] == num:
            return True
        else:
            return False

    if canDo([list[0] * list[1]]+list[2:], num):
        return True
    elif canDo([list[0] + list[1]]+list[2:], num):
        return True
    else:
        return False

sum = 0
for line in lines:
    test_num = int(line.split(":")[0])
    nums = [int(num) for num in line.split(":")[1].split()]
    if canDo(nums,test_num):
        sum+=test_num


print(sum)
