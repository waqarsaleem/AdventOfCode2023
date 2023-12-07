import math
from collections import Counter

def _strength(counts):
    '''
    7. Five of a kind, where all five cards have the same label: AAAAA
    6. Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    5. Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    4. Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    3. Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    2. One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    1. High card, where all cards' labels are distinct: 23456
    '''
    if counts == [5]:
        return 7
    if counts == [1,4]:
        return 6
    if counts == [2,3]:
        return 5
    if counts == [1,1,3]:
        return 4
    if counts == [1,2,2]:
        return 3
    if counts == [1,1,1,2]:
        return 2
    return 1

def strength(hand):
    return _strength(sorted(Counter(hand).values()))

def strength1(hand):
    if 'J' not in hand:
        return strength(hand)
    counts = Counter(hand)
    js = counts['J']
    counts = sorted(counts.values())
    if js != 5:
        counts.remove(js)
        counts[-1] += js
    return _strength(counts)

def day_7_a(fname):
    hands = [tuple(h.strip().split()) for h in open(fname).readlines()]
    hands = [(h, int(b)) for h,b in hands]
    hands.sort(key=lambda h: (strength(h[0]), h[0].translate(str.maketrans('TJQKA', ':;<=>'))))
    return sum(i*h[1] for i,h in enumerate(hands, 1))

def day_7_b(fname):
    hands = [tuple(h.strip().split()) for h in open(fname).readlines()]
    hands = [(h, int(b)) for h,b in hands]
    hands.sort(key=lambda h: (strength1(h[0]), h[0].translate(str.maketrans('TJQKA', ':1<=>'))))
    return sum(i*h[1] for i,h in enumerate(hands, 1))
        
test = False
print(day_7_b('input1.txt' if test else 'input.txt'))

