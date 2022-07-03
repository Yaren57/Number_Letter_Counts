onlar = [0, 3, 3, 2, 4, 3, 4, 4, 5, 5, 2]
yüz = 3
bin = 3
toplam = 0
for i in range(1, 1000):
    x = i % 10
    y = int(((i % 100) - x) / 10)
    z = int(((i % 1000) - (y * 10) - x) / 100)

    if z != 0 and (y != 0 or x != 0):
        if y == 0 or y == 1:
            toplam += yüz + x
        else:
            toplam += yüz + onlar[y]
    elif y == 0 and x == 0:
        toplam += yüz
    else:
        toplam += onlar[y]

print(toplam + bin)
