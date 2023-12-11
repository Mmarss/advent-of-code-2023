with open("day11_input.txt") as f:
    tiles = list(map(str.strip, f.readlines()))

double_y = list(range(len(tiles)))
double_x = list(range(len(tiles[0])))
galaxies = []
for y, row in enumerate(tiles):
    for x, tile in enumerate(row):
        if tile == "#":
            if y in double_y:
                double_y.remove(y)
            if x in double_x:
                double_x.remove(x)
            galaxies.append((x, y))

path_sum = 0
extras_sum = 0
for i, galaxy1 in enumerate(galaxies):
    for galaxy2 in galaxies[i + 1:]:
        path_sum += abs(galaxy2[0] - galaxy1[0]) + abs(galaxy2[1] - galaxy1[1])
        extras = 0
        for dx in double_x:
            if dx <= min(galaxy1[0], galaxy2[0]):
                continue
            elif dx >= max(galaxy1[0], galaxy2[0]):
                break
            else:
                extras_sum += 1
        for dy in double_y:
            if dy <= min(galaxy1[1], galaxy2[1]):
                continue
            elif dy >= max(galaxy1[1], galaxy2[1]):
                break
            else:
                extras_sum += 1


print(f"Answer Day 11, Part 1: {path_sum + extras_sum}")



print(f"Answer Day 11, Part 2: {path_sum + 999999 * extras_sum}")
