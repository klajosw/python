# -*- coding:Latin-1 -*-

def consult():
    while 1:
        name = raw_input("Irja be a nevet (vagy <enter> a kilepeshez) : ")
        if name == "":
            break
        if dico.has_key(name):           # a szótárban szerepel a név ?
            item = dico[name]            # megnézzük
            age, height = item[0], item[1]
            print "Név : %s - kor : %s ans - magasság : %s m."\
                   % (name, age, height)          
        else:
            print "*** ismeretlen név ! ***"

def fill():
    while 1:
        name = raw_input("Irja be a nevet (vagy <enter> a kilepeshez) : ")
        if name == "":
            break
        age = int(raw_input("Irja be az eletkort (egesz szam !) : "))
        height = float(raw_input("Irja be a testmagassagot (meterben) : "))
        dico[name] = (age, height)

def writeFile():
    file = raw_input("Irja be az elmentendo file nevet : ")
    ofi = open(file, "w")
    # az elõzõleg listává alakított szótár bejárása :
    for key, value in dico.items(): 
        # stringformázás alkalmazása pour créer l'enregistrement :
        ofi.write("%s@%s#%s\n" % (key, value[0], value[1]))
    ofi.close()

def readFile():
    print "picsa"
    file = raw_input("Irja be az elmentett file nevet : ")
    try:
        ofi = open(file, "r")
    except:
        print "*** nem létezõ file ***"
        return

    while 1:
        line = ofi.readline()
        if line =='':              # filevége detektálása
            break
        enreg = line.split("@")    # clé,value] lista visszaállítása
        key = enreg[0]
        value = enreg[1][:-1]      # sorvége karakter kiküszöbölése
        data = value.split("#")    # [âge, height] lista visszaállítása
        age, height = int(data[0]), float(data[1])
        dico[key] = (age, height)   # szótár rekonstruálása
    ofi.close()

def finish():
    print "*** Munka vége ***"
    return 1                        # a ciklus befejezésének elõidézése
    
def other():
    print "Kérem válasszon : V, H, B, M vagy K"
    
dico ={}
func ={"V":readFile, "H":fill, "B":consult,
       "M":writeFile, "K":finish}
while 1:
    choice = raw_input("Valasszon :\n" +\
    "(V)isszaolvasunk egy már létezõ mentett szótárat egy fileból\n" +\
    "(H)ozzáadunk az aktuális szótárhoz újabb adatokat\n" +\
    "(B)elenézünk az aktuális szótárba\n" +\
    "(M)enti az aktuális szótárat egy file-ba\n" +\
    "(K)ilép : ")
    # az alábbi utasítás minden választásra más függvényt hív
    # a <func> szótár segítségével :
    if func.get(choice, other)():
        break
    # Megjegyzés : valamennyi itt hívott függvény alapértelmezett visszatérési értéke <None>
    #              kivéve a finish() függvényt, ami esetén 1 => kilépés a ciklusból