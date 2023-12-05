import math
            
def day_4_a(fname):
    with open(fname) as f:
        total = 0
        for line in f:
            # Skip empty lines
            if line.strip() == '':
                continue
            # Get the winning numbers and those in hand.
            win, have = line[line.find(':')+1:].split('|')
            win, have = map(str.split, [win, have])
            # Set intersection, but there may be duplicates in hand.
            win = set(map(int, win))
            have = list(map(int, have))
            matches = sum(1 for n in have if n in win)
            if matches:
                total += 2 ** (matches - 1)
    return total

def day_4_b(fname):
    lines = open(fname).readlines()
    lines = list(map(str.strip, lines))
    # Omit blank line at the end.
    if lines[-1] == '':
        lines = lines[:-1]
    matches = {}  # store number of matches in each card.
    for i,line in enumerate(lines):
        # Get the winning numbers and those in hand.
        win, have = line[line.find(':')+1:].split('|')
        win, have = map(str.split, [win, have])
        win = set(map(int, win))
        have = list(map(int, have))
        # Compute and store the number of matches in this card.
        matches[i] = sum(1 for n in have if n in win)
    n = len(lines)
    lines = [1] * n  # quantity of each card. 1 card of each type initially.
    for i in range(n):
        k = lines[i]  # quantity of cards of current type.
        cards = matches[i]  # number of subsequent cards to update.
        # Update subsequent cards, once for each of the current k cards.
        for j in range(i+1, i+cards+1):
            lines[j] += k
    return sum(lines)

test = False
print(day_4_b('input1.txt' if test else 'input.txt'))

