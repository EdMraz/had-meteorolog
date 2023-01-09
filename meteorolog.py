fr = open('meteo_stanice.txt','r',encoding="utf-8")
riadky = fr.readlines()

a = 0
for riadok in riadky:
    a+=1
print("Počet meraní:",a)

b = []
for riadok in riadky:
    zoz_riadok = riadok.split()
    x = zoz_riadok[-2]
    b.append(x)
print("Teploty:",*b)

c = []
for riadok in riadky:
    zoz_riadok = riadok.split()
    x = zoz_riadok[-2]
    c.append(float(x))
z = max(c)

print("Najväčšia nameraná teplota:",z)

c = []
counter=0
for riadok in riadky:
    zoz_riadok = riadok.split()
    x = zoz_riadok[-2]
    c.append(float(x))
    counter+=1

print("Priemerná teplota:", round((sum(c)/counter),2))
