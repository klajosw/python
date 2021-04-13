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
    for key, value in dico.items(): 
        # stringform�z�s alkalmaz�sa pour cr�er l'enregistrement :
        ofi.write("%s@%s#%s\n" % (key, value[0], value[1]))
    ofi.close()

def readFile():
    print "picsa"
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
        enreg = line.split("@")    # cl�,value] lista vissza�ll�t�sa
        key = enreg[0]
        value = enreg[1][:-1]      # sorv�ge karakter kik�sz�b�l�se
        data = value.split("#")    # [�ge, height] lista vissza�ll�t�sa
        age, height = int(data[0]), float(data[1])
        dico[key] = (age, height)   # sz�t�r rekonstru�l�sa
    ofi.close()

def finish():
    print "*** Munka v�ge ***"
    return 1                        # a ciklus befejez�s�nek el�id�z�se
    
def other():
    print "K�rem v�lasszon : V, H, B, M vagy K"
    
dico ={}
func ={"V":readFile, "H":fill, "B":consult,
       "M":writeFile, "K":finish}
while 1:
    choice = raw_input("Valasszon :\n" +\
    "(V)isszaolvasunk egy m�r l�tez� mentett sz�t�rat egy fileb�l\n" +\
    "(H)ozz�adunk az aktu�lis sz�t�rhoz �jabb adatokat\n" +\
    "(B)elen�z�nk az aktu�lis sz�t�rba\n" +\
    "(M)enti az aktu�lis sz�t�rat egy file-ba\n" +\
    "(K)il�p : ")
    # az al�bbi utas�t�s minden v�laszt�sra m�s f�ggv�nyt h�v
    # a <func> sz�t�r seg�ts�g�vel :
    if func.get(choice, other)():
        break
    # Megjegyz�s : valamennyi itt h�vott f�ggv�ny alap�rtelmezett visszat�r�si �rt�ke <None>
    #              kiv�ve a finish() f�ggv�nyt, ami eset�n 1 => kil�p�s a ciklusb�l