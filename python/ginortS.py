a = list(input())
sayi_listesi = []
karakter_listesi = []
for x in a:
    try:
        integer = int(x)
        sayi_listesi.append(integer)
    except ValueError:
        karakter_listesi.append(x)
sayi_listesi = sorted(sayi_listesi, key = lambda a: int(a))
tek_sayi, cift_sayi= [], []

for x in sayi_listesi:
    if x % 2 != 0:
        tek_sayi.append(x)
    else:
        cift_sayi.append(x)

karakter_listesi1 = []
karakter_listesi2 = []
for a in karakter_listesi:
    if ord(a) >= 97 and ord(a) <= 122:
        karakter_listesi1.append(a)
    elif ord(a) >= 65 and ord(a) <= 90:
        karakter_listesi2.append(a)
karakter_listesi1 = sorted(karakter_listesi1, key = lambda a: ord(a))
karakter_listesi2 = sorted(karakter_listesi2, key = lambda a: ord(a))
print("".join(karakter_listesi1+ karakter_listesi2+ list(map(str, tek_sayi+cift_sayi))))
        
    
