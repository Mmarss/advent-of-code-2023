from collections import defaultdict
import json

hands = []
with open("day7_input.txt") as f:
    for line in f.readlines():
        hands.append({
            "hand": line[:line.find(" ")],
            "bid": int(line[line.find(" "):].strip()),
            "hand_class": defaultdict(list),
            "joker_hand_class": defaultdict(list)
        })

for hand in hands:
    cards = set(hand["hand"])
    for card in cards:
        count = hand["hand"].count(card)
        hand["hand_class"][count].append(card)

types = {
    7: lambda cls: 5 in cls,
    6: lambda cls: 4 in cls,
    5: lambda cls: 3 in cls and 2 in cls,
    4: lambda cls: 3 in cls,
    3: lambda cls: 2 in cls and len(cls[2]) == 2,
    2: lambda cls: 2 in cls,
    1: lambda cls: True
}

for hand in hands:
    for type, test in types.items():
        if test(hand["hand_class"]):
            hand["type"] = type
            break

card_strengths = "23456789TJQKA"

for hand in hands:
    hand["strength"] = hand["type"] * (13**5)
    for i, card in enumerate(hand["hand"]):
        hand["strength"] += card_strengths.find(card) * (13**(4-i))

hands = sorted(hands, key=lambda hand: hand["strength"])

for rank, hand in enumerate(hands):
    hand["rank"] = rank + 1
    hand["winnings"] = hand["rank"] * hand["bid"]

winnings = sum([hand["winnings"] for hand in hands])

print(f"Answer Day 7, Part 1: {winnings}")



for hand in hands:
    if hand["type"] == 7:
        hand["joker_hand"] = hand["hand"]
    elif hand["type"] == 6:
        repl = hand["hand_class"][4][0] if "J" in hand["hand_class"][1] else hand["hand_class"][1][0]
        hand["joker_hand"] = hand["hand"].replace("J", repl)
    elif hand["type"] == 5:
        repl = hand["hand_class"][3][0] if "J" in hand["hand_class"][2] else hand["hand_class"][2][0]
        hand["joker_hand"] = hand["hand"].replace("J", repl)
    elif hand["type"] == 4:
        repl = hand["hand_class"][1][0] if "J" in hand["hand_class"][3] else hand["hand_class"][3][0]
        hand["joker_hand"] = hand["hand"].replace("J", repl)
    elif hand["type"] == 3:
        repl = hand["hand_class"][2][1] if "J" == hand["hand_class"][2][0] else hand["hand_class"][2][0]
        hand["joker_hand"] = hand["hand"].replace("J", repl)
    elif hand["type"] == 2:
        repl = hand["hand_class"][1][0] if "J" in hand["hand_class"][2] else hand["hand_class"][2][0]
        hand["joker_hand"] = hand["hand"].replace("J", repl)
    else:
        repl = hand["hand_class"][1][1] if "J" == hand["hand_class"][1][0] else hand["hand_class"][1][0]
        hand["joker_hand"] = hand["hand"].replace("J", repl)

for hand in hands:
    cards = set(hand["joker_hand"])
    for card in cards:
        count = hand["joker_hand"].count(card)
        hand["joker_hand_class"][count].append(card)

for hand in hands:
    for type, test in types.items():
        if test(hand["joker_hand_class"]):
            hand["joker_type"] = type
            break

card_strengths = "J23456789TQKA"

for hand in hands:
    hand["strength"] = hand["joker_type"] * (13**5)
    for i, card in enumerate(hand["hand"]):
        hand["strength"] += card_strengths.find(card) * (13**(4-i))

hands = sorted(hands, key=lambda hand: hand["strength"])

for rank, hand in enumerate(hands):
    hand["rank"] = rank + 1
    hand["winnings"] = hand["rank"] * hand["bid"]

winnings = sum([hand["winnings"] for hand in hands])

print(f"Answer Day 7, Part 2: {winnings}")
