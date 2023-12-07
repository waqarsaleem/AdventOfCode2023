import math

def day_6_a(fname):
    times, distances = open(fname).readlines()
    times = map(int, times.split(':')[1].split())
    distances = map(int, distances.split(':')[1].split())
    ways = 1
    for tmax, dmax in zip(times, distances):
        ways *= sum(1 for t in range(tmax+1) if t*(tmax-t) > dmax)
    return ways

def day_6_b(fname):
    time, distance = open(fname).readlines()
    # print(f'{times=} {distances=}')
    time = int(''.join(time.split(':')[1].split()))
    distance = int(''.join(distance.split(':')[1].split()))
    print(f'{time=} {distance=}')
    t = next(i for i in range(time) if i * (time - i) > distance)
    return time - 2*t + 1
        
test = False
print(day_6_b('input1.txt' if test else 'input.txt'))

