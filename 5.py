import math

def day_5_a(fname):
    # Apply mapping as it is encountered. Consolidate mappings at the end of
    # each block or file.
    with open(fname) as f:
        keys = list(map(int, f.readline().split(':')[1].strip().split()))  # the keys
        vals = [-1] * len(keys)  # the mapping of each key, -1 for no mapping.
        f.readline()  # skip empty line
        for line in f:
            line = line[:-1]  # strip trailing \n
            if line == '':  # consolidate at end of block
                # Mappings are the keys for the next block. Un-mapped keys carry through.
                keys = [v if v != -1 else keys[i]  for i,v in enumerate(vals)]
                vals = [-1] * len(keys)  # dummy mapping for next block
            elif line[-1] != ':':  # skip header line
                # Read and apply map to the keys.
                dst, src, step = map(int, line.split())
                for i, k in enumerate(keys):
                    dist = k - src
                    if 0 <= dist <= step:
                        vals[i] = dst + dist
        keys = [v if v != -1 else keys[i]  for i,v in enumerate(vals)]
        return min(keys)

def day_5_b(fname):
    # Apply mapping as it is encountered. Consolidate mappings at the end of
    # each block or file.
    with open(fname) as f:
        ranges = list(map(int, f.readline().split(':')[1].strip().split()))
        ranges = [(ranges[i],ranges[i+1]) for i in range(0, len(ranges), 2)]
        print(ranges)
        f.readline()
        bumped = []
        for i,line in enumerate(f):
            print('line',i,':', line[:-1])
            if line == '\n':
                ranges += bumped
                bumped = []
            elif line[-2] != ':':
                dst,src,step = map(int, line.split())
                dist = dst - src
                remaining = []
                for a, b in ranges:
                    b, r = intersect_range(a, b, src, step, dist)
                    bumped += b
                    remaining += r
                ranges = remaining
            # print(f'{ranges=}')
            print(f'{len(ranges)=}')
            for a,b in ranges:
                if a < 0 or b < 0:
                    return
        ranges += bumped
        print(f'{ranges=}')
        return min(ranges)[0]

def intersect_range(r1, step1, r2, step2, dist):
    a, b = r1, r1 + step1
    c, d = r2, r2 + step2
    # print(f'Intersecting [{a}, {b}) with [{c}, {d})', end=': ')
    if b <= c or a >= d:
        intersected = []
        remaining = [(a, step1)]
    elif a < c:
        if c < b <= d:
            intersected = [(c+dist,b-c)]
            remaining = [(a, c-a) ]
        else: # b > d
            intersected = [(c+dist,d-c)]
            remaining = [(a, c-a), (d, b-d)]
    elif c <= a < d:
        if c < b <= d:
            intersected = [(a+dist, step1)]
            remaining = []
        else: # b > d
            intersected = [(a+dist, d-a)]
            remaining = [(d,b-d)]
    # print(intersected, remaining)
    return intersected, remaining

# print(open('input1.txt').readlines())
test = False
print(day_5_b('input1.txt' if test else 'input.txt'))

