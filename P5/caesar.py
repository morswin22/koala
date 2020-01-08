import re

# wartości stałe
alfabet = []
for litera in "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUWVXYZŹŻ":
    alfabet.append(litera)

# wczytanie danych
zaszyfrowane = input("Zaszyfrowany tekst: ").strip().upper()
wyraz = input("Wyraz, który w nim występuje: ").strip().upper()

# obliczenie
odszyfrowane = []
for n in range(1,len(alfabet)+1):
    tekst = ""
    for litera in zaszyfrowane:
        indeks = alfabet.index(litera) + n
        if indeks >= len(alfabet):
            indeks -= len(alfabet)
        tekst += alfabet[indeks]
    if re.search(rf"{wyraz}", tekst, re.UNICODE):
        odszyfrowane.append((str(n), tekst))

# wypisanie wyniku
for dane in odszyfrowane:
    print(' '.join(dane))