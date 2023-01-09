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

max_temp = b[0]
nazov_stanice = ""
for riadok in riadky:
    zoz_riadok = riadok.split()
    temp = zoz_riadok[-2]
    if float(max_temp) < float(temp):
        max_temp = temp
        nazov_stanice = zoz_riadok[-5]
print("Nazov stanice s najvyssou teplotou:", nazov_stanice)
