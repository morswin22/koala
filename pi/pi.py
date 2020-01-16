import math
n = int(input('n = '))
s = 0
for i in range(1,n):
    s += 1/(i*i)
print(math.sqrt(6*s))