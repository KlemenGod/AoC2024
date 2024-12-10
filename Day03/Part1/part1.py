import re

file = open("inputP1.txt")

text = file.read()

muls = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)",text)

sum = 0
for mul in muls:
    nums = mul[4:-1]
    nums = nums.split(",")
    sum += int(nums[0]) * int(nums[1])


print(sum)

