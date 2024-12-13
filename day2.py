def checkSafety(nums: list) -> bool:
    inc = True
    for i in range(len(nums) - 1):
        if not (nums[i] < nums[i + 1] and 1 <= nums[i + 1] - nums[i] <= 3):
            inc = False
            break

    dec = True
    for i in range(len(nums) - 1):
        if not (nums[i] > nums[i + 1] and 1 <= nums[i] - nums[i + 1] <= 3):
            dec = False
            break

    return inc or dec


inp = []
with open("day2.txt", "r") as file2:
    inp = [line.strip("\n") for line in file2]
print(sum(checkSafety(list(map(int, inp[x].split()))) for x in range(len(inp))))


def checkSafetyPowerDampener(nums: list) -> bool:
    if checkSafety(nums):
        return True
    else:
        for i in range(len(nums)):
            if checkSafety(nums[:i] + nums[i + 1 :]):
                return True
        return False


print(
    sum(
        checkSafetyPowerDampener(list(map(int, inp[x].split())))
        for x in range(len(inp))
    )
)
