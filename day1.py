with open("day1_input.txt") as f: print("Calibration sum part 1: " + str(sum([int(str((digits:=[c for c in line if c.isnumeric()])[0]) + str(digits[-1])) for line in f.readlines()])))



import re
cardinals = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
pattern = "(?=([1-9]|" + "|".join(cardinals.keys()) + "))"

with open("day1_input.txt") as f: print("Calibration sum part 2: " + str(sum([int(str((digits:=[cardinals[match] if match in cardinals else int(match) for match in re.findall(pattern, line)])[0]) + str(digits[-1])) for line in f.readlines()])))
