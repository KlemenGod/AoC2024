import re

file = open("inputP2.txt")

text = file.read()

seperators = re.findall("do\(\)|don't\(\)",text)
strs = (re.split("do\(\)|don't\(\)",text))
dos = [stri for sep,stri in zip(seperators,strs[1:]+strs[0:1]) if(sep != "don't()")]
dos.append(strs[0])



sum = 0

for do in dos:
    muls = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)",do)

    for mul in muls:
        nums = mul[4:-1]
        nums = nums.split(",")
        sum += int(nums[0]) * int(nums[1])

print(sum)

