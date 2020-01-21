p = 0.014
t = 1

kw = int(input('Kwota: '))
n = int(input('Co ile mies: '))
m = int(input('Licz dla okresu mies: '))

s = 0

l = 1
for i in range(m):
  if l == n:
    s += kw - ((kw*p) + t)
    l = 0
  l+=1

print("\nDla {0} miesięcy zysk wyniesie {1:.2f} zł".format(m, s))
print("Dla 1 miesiąca zysk wyniesie {0:.2f} zł". format(s/m))

k = int(input('\nIle kont: '))

print("\nDla {0} kont zysk po {1} miesiącach wyniesie {2:.2f} zł".format(k, m, s*k))
print("Dla {0} kont zysk po 1 miesięcu wyniesie {1:.2f} zł".format(k, (s/m)*k))