import math

def day_2_a():
    ids = 0
    target_d = {'red': 12, 'green': 13, 'blue': 14}
    with open('input.txt') as f:
        for line in f:
            colon = line.find(':')
            game_num = int(line[5:colon])
            possible = True
            for sets in line[colon+1:].split(';'):
                for cubes in sets.split(','):
                    num, color = cubes.split()
                    if int(num) > target_d[color]:
                        possible = False
                        break
                if not possible:
                    break
            if possible:
                ids += game_num
        return ids

def day_2_b():
    power = 0
    with open('input.txt') as f:
        for line in f:
            d = {'red': 0, 'green': 0, 'blue': 0}
            colon = line.find(':')
            game_num = int(line[5:colon])
            possible = True
            for sets in line[colon+1:].split(';'):
                for cubes in sets.split(','):
                    num, color = cubes.split()
                    d[color] = max(int(num), d[color])
            power += math.prod(d.values())
        return power
