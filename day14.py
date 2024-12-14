def create_empty_grid(width, height):
    return [[[] for _ in range(width)] for _ in range(height)]


def setup(input_val, width, height):
    velocities = {input_val.index(b) + 1: (b[1][1], b[1][0]) for b in input_val}
    pos_init = {input_val.index(b) + 1: (b[0][1], b[0][0]) for b in input_val}
    pos = create_empty_grid(width, height)
    for robot_id, (y, x) in pos_init.items():
        pos[y][x].append(robot_id)
    return pos, velocities


def move(pos, velocities, width, height):
    temp_pos = create_empty_grid(width, height)
    active_positions = {
        (y, x) for y in range(height) for x in range(width) if pos[y][x]
    }
    for y, x in active_positions:
        for machine_id in pos[y][x]:
            dy, dx = velocities[machine_id]
            temp_pos[(y + dy) % height][(x + dx) % width].append(machine_id)
    return [row[:] for row in temp_pos]


def p1_score(pos, width, height):
    sums = [0] * 4
    for y in range(height):
        for x in range(width):
            if pos[y][x]:
                if y < height // 2 and x < width // 2:
                    sums[0] += len(pos[y][x])
                elif y < height // 2 and x > width // 2:
                    sums[1] += len(pos[y][x])
                elif y > height // 2 and x < width // 2:
                    sums[2] += len(pos[y][x])
                elif y > height // 2 and x > width // 2:
                    sums[3] += len(pos[y][x])
    return sums[0] * sums[1] * sums[2] * sums[3]


with open("day14.txt", "r") as file14:
    input_val = list(
        map(
            lambda x: [
                list(map(int, coord.split("=")[1].split(","))) for coord in x.split(" ")
            ],
            file14.read().strip().split("\n"),
        )
    )
width = 101  # x
height = 103  # y
pos, vel = setup(input_val, width, height)
for _ in range(100):
    pos = move(pos, vel, width, height)
result1 = p1_score(pos, width, height)
print(result1)
k = 100
while True:
    pos = move(pos, vel, width, height)
    active_positions = {
        (y, x) for y in range(height) for x in range(width) if pos[y][x]
    }
    k += 1
    if len(active_positions) == len(input_val):
        break
print(k)
