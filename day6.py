import re
import math

# Solve x + y = t, xy > d => x(t-x) > d => x^2 - tx + d = 0

product = 1
with open("day6_input.txt") as f:
    lines = f.readlines()
    times = map(int, re.findall(r"\d+", lines[0]))
    distances = map(int, re.findall(r"\d+", lines[1]))
    for time, distance in zip(times, distances):
        x_min = math.ceil((time - math.sqrt(time * time - 4 * (distance + 1))) / 2)
        solutions = time - 2 * x_min + 1
        product *= solutions

print(f"Answer Day 6, Part 1: {product}")



with open("day6_input.txt") as f:
    lines = [line.replace(" ", "") for line in f.readlines()]
    time = int(re.search(r"\d+", lines[0]).group(0))
    distance = int(re.search(r"\d+", lines[1]).group(0))
    x_min = math.ceil((time - math.sqrt(time * time - 4 * (distance + 1))) / 2)
    solutions = time - 2 * x_min + 1

print(f"Answer Day 6, Part 2: {solutions}")
