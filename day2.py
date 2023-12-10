limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

with open("day2_input.txt") as f:
    id_sum = 0
    for line in f.readlines():
        label = line.split(": ")[0]
        id = int(label.split(" ")[1])
        rounds = line.split(": ")[1].strip().split("; ")
        possible = True
        for round in rounds:
            results = round.split(", ")
            for result in results:
                quantity = int(result.split(" ")[0])
                color = result.split(" ")[1]
                if quantity > limits[color]:
                    possible = False
        if possible:
            id_sum += id
print(f"Answer Day 2, Part 1: {id_sum}")



from functools import reduce
colors = ["red", "green", "blue"]
with open("day2_input.txt") as f:
    power_sum = 0
    for line in f.readlines():
        label = line.split(": ")[0]
        id = int(label.split(" ")[1])
        rounds = line.split(": ")[1].strip().split("; ")
        minima = {color: 0 for color in colors}
        for round in rounds:
            results = round.split(", ")
            for result in results:
                quantity = int(result.split(" ")[0])
                color = result.split(" ")[1]
                minima[color] = max(minima[color], quantity)
        power = reduce(lambda a, b: a * b, minima.values())
        power_sum += power
print(f"Answer Day 2, Part 2: {power_sum}")

