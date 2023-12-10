with open("day10_input.txt") as f:
    tiles = list(map(str.strip, f.readlines()))

for j, row in enumerate(tiles):
    if row.find("S") >= 0:
        start = (row.find("S"), j)
        break

neighbours = {
    "S": [(-1,  0), (0, -1), (1, 0), (0, 1)],
    "-": [(-1,  0), (1,  0)],
    "|": [( 0, -1), (0,  1)],
    "7": [(-1,  0), (0,  1)],
    "J": [(-1,  0), (0, -1)],
    "L": [( 0, -1), (1,  0)],
    "F": [( 1,  0), (0,  1)],
    ".": []
}

nodes = [start]
visited = []
left = []
right = []
max_len = 0
while len(nodes) > 0:
    next_nodes = []
    for node in nodes:
        to_test = [{"coord": (node[0] + x_offset, node[1] + y_offset), "expect_offset": (-x_offset, -y_offset)}
            for x_offset, y_offset in neighbours[tiles[node[1]][node[0]]]
            if (node[0] + x_offset, node[1] + y_offset) not in visited]
        for test_node in to_test:
            if test_node["expect_offset"] in neighbours[tiles[test_node["coord"][1]][test_node["coord"][0]]]:
                next_nodes.append(test_node["coord"])
    visited += nodes
    nodes = next_nodes
    max_len += 1
max_len -= 1

print(f"Answer Day 10, Part 1: {max_len}")



rot_left = lambda coord: (coord[1], -coord[0])
rot_right = lambda coord: (-coord[1], coord[0])

node = start
path = []
left = []
right = []
while True:
    to_test = [{"coord": (node[0] + x_offset, node[1] + y_offset), "offset": (x_offset, y_offset), "expect_offset": (-x_offset, -y_offset)}
        for x_offset, y_offset in neighbours[tiles[node[1]][node[0]]]
        if (node[0] + x_offset, node[1] + y_offset) not in path]
    for test_node in to_test:
        if test_node["expect_offset"] in neighbours[tiles[test_node["coord"][1]][test_node["coord"][0]]]:
            next_node = test_node["coord"]
            left.append((node[0] + rot_left(test_node["offset"])[0],
                node[1] + rot_left(test_node["offset"])[1]))
            left.append((test_node["coord"][0] + rot_left(test_node["offset"])[0],
                test_node["coord"][1] + rot_left(test_node["offset"])[1]))
            right.append((node[0] + rot_right(test_node["offset"])[0],
                node[1] + rot_right(test_node["offset"])[1]))
            right.append((test_node["coord"][0] + rot_right(test_node["offset"])[0],
                test_node["coord"][1] + rot_right(test_node["offset"])[1]))
            break
    path.append(node)
    node = next_node
    if node in path:
        break

is_valid = lambda coord: coord[0] >= 0 and coord[1] >= 0 and coord[1] < len(tiles) and coord[0] < len(tiles[0])
is_edge = lambda coord: coord[0] == 0 or coord[1] == 0 or coord[1] == len(tiles) - 1 or coord[0] == len(tiles[0]) - 1

all_neighbours = [(-1,  0), (0, -1), (1, 0), (0, 1)]

def refine_and_grow(side):
    side = [coord for coord in set(side) if coord not in path and is_valid(coord)]
    to_visit = side
    visited = path
    while len(to_visit):
        next_visit = []
        for coord in to_visit:
            for neighbour in all_neighbours:
                test_coord = (coord[0] + neighbour[0], coord[1] + neighbour[1])
                if not is_valid(test_coord) or test_coord in visited:
                    continue
                next_visit.append(test_coord)
            if coord not in side:
                side.append(coord)
            if is_edge(coord):
                return side
            visited.append(coord)
        to_visit = next_visit
    return side

left = refine_and_grow(left)
right = refine_and_grow(right)

inner = left if any(is_edge(coord) for coord in right) else right

print(f"Answer Day 10, Part 2: {len(inner)}")
