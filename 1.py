import math

def day_1_a():
    with open('input.txt') as f:
        total = 0
        for line in f:
            # save all the digits in this line, work on the first and last.
            nums = [c for c in line if c.isnumeric()]  
            total += 10 * int(nums[0]) + int(nums[-1])  # 
    return total

def day_1_b():
    # Generate digits and words to seek.
    digits = list(map(str, range(1, 10)))
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    total = 0
    with open('input.txt') as f:
        for line in f:
            # Initialize indexes of first and last occurrences in this
            # line. Will be updated as the line is traversed.
            first, last = len(line), -1
            # Initialize the digits that will make the number. Will be updated
            # as the line is traversed.
            tens = units = 0
            # Find first and last occurrence of each digit. Update values.
            for k in digits:
                idx = line.find(k)
                if idx != -1 and idx < first:
                    first = idx
                    tens = int(k)
                idx = line.rfind(k)
                if idx != -1 and idx > last:
                    last = idx
                    units = int(k)
            # Find first and last occurrence of each words. Update values.
            for i,k in enumerate(words, 1):
                idx = line.find(k)
                if idx != -1 and idx < first:
                    first = idx
                    tens = i
                idx = line.rfind(k)
                if idx != -1 and idx > last:
                    last = idx
                    units = i
            total += 10 * tens + units
    return total
