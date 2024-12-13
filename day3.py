import re

line = ""
with open("day3.txt", "r") as file3:
    line = file3.read()
matches = re.findall("mul[(][0-9,]*[)]", line)
matches2 = re.findall("(mul[(][0-9,]*[)])|(do[(][)])|(don't[(][)])", line)


def mul(x: str) -> int:
    comma = x.index(",")
    a, b = int(x[4:comma]), int(x[comma + 1 : -1])
    return a * b


print(sum(mul(x) for x in matches))

do = True
mult_sum = 0
for i in matches2:
    if "do()" in i:
        do = True
        continue
    elif "don't()" in i:
        do = False
        continue
    if do:
        mult_sum += mul(i[0])
print(mult_sum)
