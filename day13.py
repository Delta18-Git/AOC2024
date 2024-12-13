import re


def solver(ax: int, bx: int, px: int, ay: int, by: int, py: int):
    a = (px * by - py * bx) // (by * ax - bx * ay)
    b = (px * ay - py * ax) // (ay * bx - ax * by)
    if a * ax + b * bx == px and a * ay + b * by == py:
        return 3 * a + b
    else:
        return 0


with open("day13.txt", "r") as file13:
    raw_input = file13.read().strip()

data = [line for line in raw_input.split("\n") if line]
machines = [data[i : i + 3] for i in range(0, len(data), 3)]
sum1 = 0
sum2 = 0
for machine in machines:
    vars = list(list() for i in range(3))
    for row in range(len(machine)):
        vars[row] = list(map(int, re.findall("[0-9]+", machine[row])))
    sum1 += solver(
        vars[0][0], vars[1][0], vars[2][0], vars[0][1], vars[1][1], vars[2][1]
    )
    sum2 += solver(
        vars[0][0],
        vars[1][0],
        vars[2][0] + 10**13,
        vars[0][1],
        vars[1][1],
        vars[2][1] + 10**13,
    )
print(sum1, sum2)
