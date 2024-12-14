import itertools


def combination1(n: int) -> list[tuple[str, ...]]:
    return list(itertools.product(["*", "+"], repeat=n))


def combination2(n: int) -> list[tuple[str, ...]]:
    return list(itertools.product(("*", "+", "||"), repeat=n))


def eqn_solver(ans: str, values: list[str], part1: bool = True) -> bool:
    if part1:
        operators = combination1(len(values) - 1)
    else:
        operators = combination2(len(values) - 1)
    answers = []
    for ops in operators:
        result = int(values[0])
        for i in range(len(ops)):
            if ops[i] == "+":
                result += int(values[i + 1])
            elif ops[i] == "*":
                result *= int(values[i + 1])
            else:
                result = result * 10 ** len(values[i + 1]) + int(values[i + 1])
        answers.append(result)
    return int(ans) in answers


def calibration_result(dict_in: dict[str, list[str]], part1: bool = True) -> int:
    ans = 0
    for i, j in dict_in.items():
        if eqn_solver(i, j, part1):
            ans += int(i)
    return ans


with open("day7.txt", "r") as file7:
    dic = {x.split(":")[0]: x.split(":")[1].strip().split() for x in file7.readlines()}

print(calibration_result(dic))
print(calibration_result(dic, part1=False))
