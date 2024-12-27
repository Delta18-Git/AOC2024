with open("day9.txt", "r") as file9:
    diskmap = list(int(x) for x in file9.read().strip("\n"))


def part1(diskmap: list[int]) -> list[int]:
    blocks: list[int] = []
    for i in range(len(diskmap)):
        if i % 2 == 0:
            blocks.extend([i // 2] * diskmap[i])
        else:
            blocks.extend([-1] * diskmap[i])
    last = len(blocks) - 1
    for i in range(len(blocks)):
        if blocks[i] == -1:
            while last > i and blocks[last] == -1:
                last -= 1
            if last > i:
                blocks[i] = blocks[last]
                blocks[last] = -1
                last -= 1
    return blocks


def part2(diskmap: list[int]):
    blocks: list[int] = []
    file_info = {file_id: dict() for file_id in set(diskmap)}

    for i in range(len(diskmap)):
        if i % 2 == 0:
            blocks.extend([i // 2] * diskmap[i])
        else:
            blocks.extend([-1] * diskmap[i])
    i = 0
    while i < len(blocks):
        if blocks[i] != -1:
            file_id = blocks[i]
            start = i
            while i < len(blocks) and blocks[i] == file_id:
                i += 1
            file_info[file_id] = {"size": i - start, "start": start, "end": i - 1}
        else:
            i += 1
    for file_id in sorted(file_info.keys(), reverse=True):
        file_data = file_info[file_id]
        size = file_data["size"]
        i = 0
        while i < file_data["start"]:
            if blocks[i] == -1:
                can_fit = True
                for j in range(size):
                    if i + j >= len(blocks) or blocks[i + j] != -1:
                        can_fit = False
                        break
                if can_fit:
                    for j in range(size):
                        blocks[i + j] = file_id
                    for j in range(file_data["start"], file_data["end"] + 1):
                        blocks[j] = -1
                    break
            i += 1
    return blocks


def checksum(blocks: list[int]) -> int:
    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] != -1:
            checksum += blocks[i] * i
    return checksum


print(checksum(part1(diskmap)))
print(checksum(part2(diskmap)))
