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
    for cle, value in dico.items(): 
        # stringformázás alkalmazása :
        ofi.write("%s@%s#%s\n" % (cle, value[0], value[1]))
    ofi.close()

def readFile():
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
        enreg = line.split("@")    # [clé,value] lista visszaállítása  
        cle = enreg[0]
        value = enreg[1][:-1]      # sorvége karakter kiküszöbölése
        data = value.split("#")    # [âge, height] lista visszaállítása 
        age, height = int(data[0]), float(data[1])
        dico[cle] = (age, height)   # szótár rekonstruálása
    ofi.close()
    
dico ={}
readFile()        
while 1:
    choice = raw_input("Valasszon : (K)itolt - (M)egnez - (V)ege : ")
    if choice.upper() == 'V':
        break
    elif choice.upper() == 'K':
        fill()
    elif choice.upper() == 'M':
        consult()
writeFile()