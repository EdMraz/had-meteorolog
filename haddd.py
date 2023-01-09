fr = open('hada.txt','r',encoding="utf-8")
fw = open('hada_new.txt','w',encoding="utf-8")
fww = open('hada_new2.txt','w',encoding="utf-8")

riadky = fr.readlines()
maximalka = max(riadky,key=len,default=0)
haha = maximalka.strip()
print("Počet krokov v najdlhšej hre:",len(haha))

a = 0
for riadok in riadky:
    a+=1
print("Počet zapísaných hier v súbore:",a)

for riadok in riadky:
    fw.write(riadok)

for riadok in riadky:
    counter = 0
    char = riadok[0]
    for x in range(len(riadok)):
        if char == riadok[x]:
            counter += 1
        else:
            if x == len(riadok)-1:
                fww.write(char + " " + str(counter) + "\n")
            else:
                fww.write(char + " " + str(counter) + " ")
            char = riadok[x]
            counter = 1
