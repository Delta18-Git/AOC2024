with open("day4.txt", "r") as file4:
    line = list(map(str.strip, file4.readlines()))

grid = {(y, x): line[y][x] for y in range(len(line)) for x in range(len(line[y]))}
# print(grid)

count = 0
diff = [-1, 0, 1]
for a, b in grid:
    for i in diff:
        for j in diff:
            test_string = ""
            for k in range(len("XMAS")):
                test_string += grid.get((a + i * k, b + j * k), "")
            if test_string == "XMAS":
                count += 1
print(count)

count = 0
diff = [-1, 1]
for a, b in grid:
    test1 = ""
    test2 = ""
    if grid[a,b] == "A":
        test1 = grid.get((a + diff[0], b + diff[0]), "") + "A" + grid.get((a + diff[1], b + diff[1]), "")
        test2 = grid.get((a + diff[0], b + diff[1]), "") + "A" + grid.get((a + diff[1], b + diff[0]), "")
    if (test1 == "MAS" or test1 == "SAM") and (test2 == "MAS" or test2 == "SAM"):
        count += 1
print(count)
