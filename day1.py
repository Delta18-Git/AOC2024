l1 = []
l2 = []
with open("day1.txt", "r") as f1:
    for i in range(1000):
        a, b = tuple(map(int, f1.readline().split()))
        l1.append(a)
        l2.append(b)
print(sum(list(map(lambda x: abs(x[0] - x[1]), list(zip(sorted(l1), sorted(l2)))))))
sim = 0
for i in range(1000):
    sim += l1[i] * l2.count(l1[i])
print(sim)
