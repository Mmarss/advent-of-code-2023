seeds = []
maps = {}

with open("day5_input.txt") as f:
    lines = f.readlines()
    seeds = list(map(int, lines[0].split(": ")[1].strip().split(" ")))
    for line in lines[1:]:
        if line.strip() == "":
            do_read_header = True
            continue
        if do_read_header:
            map_label = line.split(" ")[0]
            map_from, _, map_to = map_label.split("-")
            maps[map_from] = {
                "source": map_from,
                "dest": map_to,
                "ranges": []
            }
            do_read_header = False
            continue
        range_params = list(map(int, line.strip().split(" ")))
        maps[map_from]["ranges"].append({
            "dest_start": range_params[0],
            "source_start": range_params[1],
            "range_length": range_params[2],
            "source_end": range_params[1] + range_params[2],
            "offset": range_params[0] - range_params[1]
        })

properties = [{"seed": seed} for seed in seeds]
source_map = "seed"
while source_map != "location":
    almanac_map = maps[source_map]
    dest = almanac_map["dest"]
    for property in properties:
        value = property[source_map]
        for value_range in almanac_map["ranges"]:
            if value >= value_range["source_start"] and value < value_range["source_end"]:
                property[dest] = value + value_range["offset"]
                break
        if dest not in property:
            property[dest] = value
    source_map = dest

print(f"Answer Day 5, Part 1: {min([property['location'] for property in properties])}")



min_location = float('inf')
for seed, limit in zip(seeds[::2], seeds[1::2]):
    start = seed
    while start < seed + limit:
        value = start
        min_step = seed + limit - start
        source_map = "seed"
        while source_map != "location":
            almanac_map = maps[source_map]
            dest = almanac_map["dest"]
            initial_value = value
            for value_range in almanac_map["ranges"]:
                if value >= value_range["source_start"] and value < value_range["source_end"]:
                    value += value_range["offset"]
                    min_step = min(value_range["source_end"] - initial_value, min_step)
                    break
            else:
                min_step = min([value_range["source_end"] - initial_value for value_range in almanac_map["ranges"] if value_range["source_start"] > initial_value] + [min_step])
            # print(f"mapped {source_map} {initial_value} to {dest} {value}, min step {min_step}")
            source_map = dest
        min_location = min(value, min_location)
        start += min_step

print(f"Answer Day 5, Part 2: {min_location}")