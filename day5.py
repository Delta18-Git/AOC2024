ordering = []
pages = []
with open("day5.txt", "r") as file5:
    temp = file5.readlines()
    br = temp.index("\n")
    ordering = list(map(lambda x: x.split("|"), temp[:br]))
    ordering = [[y.strip("\n") for y in x] for x in ordering]
    pages = list(map(lambda x: x.split(","), temp[br + 1:]))
    pages = [[y.strip("\n") for y in x] for x in pages]
    del temp

rules = {}
for x in ordering:
    if x[0] not in rules:
        rules[x[0]] = []
    rules[x[0]].append(x[1])

sum_middle = 0
fake_middle = 0
for p in pages:
    valid = True
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[j] in rules and p[i] in rules[p[j]]:
                valid = False
                break
        if not valid:
            break
    if valid:
        sum_middle += int(p[len(p) // 2])
    else:
        temp_rules = {}
        for page in p:
            temp_rules[page] = []
            if page in rules:
                for later in rules[page]:
                    if later in p:
                        temp_rules[page].append(later)
        dep_count = {page: 0 for page in p}
        for page in temp_rules:
            for later_page in temp_rules[page]:
                dep_count[later_page] += 1
        no_dep = [page for page in p if dep_count[page] == 0]
        result = []
        while no_dep:
            result.append(no_dep.pop(0))
            for later_page in temp_rules[result[-1]]:
                dep_count[later_page] -= 1
                if dep_count[later_page] == 0:
                    no_dep.append(later_page)
        fake_middle += int(result[len(result) // 2])

print(sum_middle)
print(fake_middle)
