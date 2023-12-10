import re
import math

with open("day8_input.txt") as f:
    lines = f.readlines()
    instructions = lines[0].strip()
    network = {}
    for line in lines[2:]:
        label, left, right = re.match(r"(\w+) = \((\w+), (\w+)\)", line).groups()
        network[label] = {
            "label": label,
            "L": left,
            "R": right
        }

steps = 0
pos = 0
node = "AAA"
while node != "ZZZ":
    instruction = instructions[pos]
    pos = (pos + 1) % len(instructions)
    node = network[node][instruction]
    steps += 1

print(f"Answer Day 8, Part 1: {steps}")

steps = 0
pos = 0
nodes = [{"pos": node} for node in network.keys() if node.endswith("A")]
while not all("cycle" in node for node in nodes):
    instruction = instructions[pos]
    pos = (pos + 1) % len(instructions)
    for node in nodes:
        node["pos"] = network[node["pos"]][instruction]
    steps += 1
    for node in nodes:
        if "cycle" not in node and node["pos"].endswith("Z"):
            node["cycle"] = steps

total_steps = math.lcm(*[node["cycle"] for node in nodes])

print(f"Answer Day 8, Part 2: {total_steps}")