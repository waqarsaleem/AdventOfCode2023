import math

def day_3_a():
    total = 0
    lines = open('input.txt').readlines()
    lines = list(map(str.strip, lines))
    if lines[-1] == '':
        lines = lines[:-1]
    for i, line in enumerate(lines):
        number_found = False
        number = ''
        for j,c in enumerate(line):
            if c.isnumeric():
                if not number_found:
                    start = j
                    number_found = True
                number += c
            elif number_found:
                stop = j
                if check_num(i, start, stop, lines):
                    total += int(number)
                number_found = False
                number = ''
        if number_found:
            stop = len(line)
            if check_num(i, start, stop, lines):
                total += int(number)
    return total

def check_num(i, start, stop, lines):
    line = lines[i]
    if start > 0:
        start -= 1
        if line[start] != '.':
            return True
    if stop < len(line):
        if line[stop] != '.':
            return True
        stop += 1
    idx = []
    if i > 0:
        idx.append(i-1)
    if i < len(lines) - 1:
        idx.append(i+1)
    bad = '.' * (stop - start)
    return any(lines[j][start:stop] != bad for j in idx)

def day_3_gear_ratios_b(fname):
    lines = open(fname).readlines()
    lines = list(map(str.strip, lines))
    if lines[-1] == '':
        lines = lines[:-1]
    parts = {}
    for i, line in enumerate(lines):
        number_found = False
        number = ''
        for j,c in enumerate(line):
            if c.isnumeric():
                if not number_found:
                    start = j
                    number_found = True
                number += c
            elif number_found:
                stop = j
                if check_num(i, start, stop, lines):
                    parts[i] = parts.get(i, []) + [(start, stop-1)]
                number_found = False
                number = ''
        if number_found:
            stop = len(line)
            if check_num(i, start, stop, lines):
                parts[i] = parts.get(i, []) + [(start, stop-1)]
    gears = [(i,j) for i,line in enumerate(lines) for j,c in enumerate(line) if c == '*']
    sum_ratios = 0
    for r,c in gears:
        nbrs = []
        for start,stop in parts.get(r,[]):
            if c == start - 1 or c == stop + 1:
                nbrs.append(lines[r][start:stop+1])
        for i in [n for n in [r-1, r+1] if n in parts]:
            for start, stop in parts[i]:
                if start - 1 <= c <= stop + 1:
                    nbrs.append(lines[i][start:stop+1])
        if len(nbrs) == 2:
            sum_ratios += math.prod(map(int, nbrs))
    return sum_ratios
