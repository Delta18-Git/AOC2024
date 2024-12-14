import copy

with open("day6.txt", "r") as file6:
    matrix = list(map(list, file6.readlines()))


def initial_pos(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == "^":
                return y, x
    return -3, -3


def move(matrix, y, x):
    temp = copy.deepcopy(matrix)
    next = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir = 0

    while True:
        if temp[y][x] != "#":
            temp[y][x] = "X"

        dy, dx = next[dir]
        next_y, next_x = y + dy, x + dx

        if 0 <= next_y < len(temp) and 0 <= next_x < len(temp[0]):
            if temp[next_y][next_x] == "#":
                dir = (dir + 1) % 4
            else:
                y, x = next_y, next_x
        else:
            break
    return temp


def check_cycle(matrix: list[list[str]], y: int, x: int):
    moves = 0
    next = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir = 0
    while moves <= len(matrix) * len(matrix[0]) * 4:
        # if matrix[y][x] != "#":
        #     matrix[y][x] = "X"
        moves += 1
        dy, dx = next[dir]
        next_y, next_x = y + dy, x + dx

        if 0 <= next_y < len(matrix) and 0 <= next_x < len(matrix[0]):
            if matrix[next_y][next_x] == "#":
                dir = (dir + 1) % 4
            else:
                y, x = next_y, next_x
        else:
            return False
    return True


def obstacler(matrix, sy, sx):
    loop_counter = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] not in ["#", "^"]:
                temp = copy.deepcopy(matrix)
                temp[y][x] = "#"
                if check_cycle(temp, sy, sx):
                    loop_counter += 1
    return loop_counter


# Main code
with open("day6.txt", "r") as file6:
    matrix = list(map(list, file6.readlines()))

y, x = initial_pos(matrix)
p1 = sum(row.count("X") for row in move(matrix, y, x))
print(f"Part1: {p1}")
p2 = obstacler(matrix, y, x)
print(f"Part2: {p2}")
