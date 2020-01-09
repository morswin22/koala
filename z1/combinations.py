from itertools import product

valid = 0
for combination in product(range(1,10), repeat=4):
    if sum(combination) == 12:
        print(combination)
        valid += 1

print(valid)