from collections import defaultdict

with open("day3_input.txt") as f:
    schematic = f.readlines()

tiles = [[{
        "character": c,
        "neighbour_symbol": False,
        "adjacent_gear_ids": []
    } for c in row.strip()] for row in schematic]

height = len(tiles)
width = len(tiles[0])

gear_id_counter = 0
for y in range(height):
    for x in range(width):
        tile = tiles[y][x]
        is_gear = False
        if not tile["character"].isalnum() and tile["character"] != ".":
            if tile["character"] == "*":
                is_gear = True
                gear_id_counter += 1
            for n_y in range(max(0, y-1), min(height, y+2)):
                for n_x in range(max(0, x-1), min(width, x+2)):
                    tiles[n_y][n_x]["neighbour_symbol"] = True
                    if is_gear:
                        tiles[n_y][n_x]["adjacent_gear_ids"].append(gear_id_counter)

gear_candidates = defaultdict(list)
part_num_sum = 0
for y in range(height):
    x = 0
    while x < width:
        number = ""
        is_part_num = False
        adjacent_gear_ids = []
        while x < width and tiles[y][x]["character"].isnumeric():
            number += tiles[y][x]["character"]
            if tiles[y][x]["neighbour_symbol"]:
                is_part_num = True
            for adjacent_gear_id in tiles[y][x]["adjacent_gear_ids"]:
                adjacent_gear_ids.append(adjacent_gear_id)
            x += 1
        if is_part_num:
            part_num_sum += int(number)
        for adjacent_gear_id in set(adjacent_gear_ids):
            gear_candidates[adjacent_gear_id].append(int(number))
        x += 1

print(f"Answer Day 3, Part 1: {part_num_sum}")

gear_ratio_sum = 0
for gear_id, part_nums in gear_candidates.items():
    if len(part_nums) == 2:
        gear_ratio = part_nums[0] * part_nums[1]
        gear_ratio_sum += gear_ratio

print(f"Answer Day 3, Part 2: {gear_ratio_sum}")
