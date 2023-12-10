cards = []
value_sum = 0
with open("day4_input.txt") as f:
    for line in f.readlines():
        numbers = line.split(": ")[1]
        card_numbers = [int(number) for number in numbers.split(" | ")[0].split(" ") if number != ""]
        winning_numbers = [int(number) for number in numbers.split(" | ")[1].split(" ") if number != ""]
        cards.append({
            "card_id": int([part for part in line.split(": ")[0].split(" ") if part][1]),
            "copies": 1,
            "card_numbers": card_numbers,
            "winning_numbers": winning_numbers
        })
        wins = 0
        for number in card_numbers:
            if number in winning_numbers:
                wins += 1
        if wins:
            value = 2 ** (wins - 1)
            cards[-1]["value"] = wins
            value_sum += value
        else:
            cards[-1]["value"] = 0

print(f"Answer Day 4, Part 1: {value_sum}")



for i, card in enumerate(cards):
    for j in range(i + 1, min(len(cards), i + 1 + card["value"])):
        cards[j]["copies"] += card["copies"]
print(f"Answer Day 4, Part 2: {sum([card['copies'] for card in cards])}")