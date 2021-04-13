# -*- coding:Latin-1 -*-

def consult():
    while 1:
        name = raw_input("Irja be a nevet (vagy <enter> a kilepeshez) : ")
        if name == "":
            break
        if dico.has_key(name):           # a sz�t�rban szerepel a n�v ?
            item = dico[name]            # megn�zz�k
            age, height = item[0], item[1]
            print "N�v : %s - kor : %s ans - magass�g : %s m."\
                   % (name, age, height)          
        else:
            print "*** ismeretlen n�v ! ***"

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
    # az el�z�leg list�v� alak�tott sz�t�r bej�r�sa :
    for cle, value in dico.items(): 
        # stringform�z�s alkalmaz�sa :
        ofi.write("%s@%s#%s\n" % (cle, value[0], value[1]))
    ofi.close()

def readFile():
    file = raw_input("Irja be az elmentett file nevet : ")
    try:
        ofi = open(file, "r")
    except:
        print "*** nem l�tez� file ***"
        return

    while 1:
        line = ofi.readline()
        if line =='':              # filev�ge detekt�l�sa
            break
        enreg = line.split("@")    # [cl�,value] lista vissza�ll�t�sa  
        cle = enreg[0]
        value = enreg[1][:-1]      # sorv�ge karakter kik�sz�b�l�se
        data = value.split("#")    # [�ge, height] lista vissza�ll�t�sa 
        age, height = int(data[0]), float(data[1])
        dico[cle] = (age, height)   # sz�t�r rekonstru�l�sa
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