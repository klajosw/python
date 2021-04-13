#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Sorok mondatokká történõ egyesítése

fiSource = raw_input("A kezelendo file neve : ")
fiDest = raw_input("A celfile neve : ")
fs = open(fiSource, 'r')
fd = open(fiDest, 'w')


# Elõször az elsõ sort olvassuk el :
ch1 = fs.readline()
# utána a következõ sorokat olvassuk el és egyesítjük õket, ha szükséges :
while 1:
    ch2 = fs.readline()
    if ch2 == "":
        break
    # Ha a beolvasott karakterlánc nagybetûvel kezdõdik, akkor az elõzõt átírjuk a 
    # célfileba, és azzal a karakterlánccal helyettesítjük, amit beolvastunk :
    if ch2[0] >= "A" and ch2[0] <= "Z":
        fd.write(ch1)
        ch1 = ch2
    # ha nem, az elõzõvel egyesítjük :
    else:
        ch1 = ch1[:-1] + " " + ch2
        # (ügyeljünk rá, hogy távolítsuk el ch1 -rõl a sorvége karaktert)
        
fd.write(ch1)        # ne felejtsük el átírni az utolsót !
fd.close()    
fs.close()
