forward_extrapolation_sum = 0
backward_extrapolation_sum = 0
with open("day9_input.txt") as f:
    for line in f.readlines():
        differences = []
        differences.append(list(map(int, line.strip().split())))
        index = 0
        while any(difference != 0 for difference in differences[index]):
            differences.append([b - a for a, b in zip(differences[index][:-1], differences[index][1:])])
            index += 1
        for i in range(len(differences) - 1, 0, -1):
            differences[i - 1].append(differences[i - 1][-1] + differences[i][-1])
        forward_extrapolation_sum += differences[0][-1]
        for i in range(len(differences) - 1, 0, -1):
            differences[i - 1].insert(0, differences[i - 1][0] - differences[i][0])
        backward_extrapolation_sum += differences[0][0]

print(f"Answer Day 9, Part 1: {forward_extrapolation_sum}")
print(f"Answer Day 9, Part 2: {backward_extrapolation_sum}")
