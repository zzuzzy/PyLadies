#--*-- encoding:1250 --*--

zvirata = ["pes", "ko�ka", "kr�l�k", "had"]
zvirata2 = ["pes", "ko�ka", "kr�l�k", "had", "andulka"]

def ukol1():
    """vyp�e jm�na dom�c�ch zv��at, kter� jsou krat�� ne� 5 p�smen"""
   
    for zvire in zvirata:
        if len(zvire) < 5:
            print(zvire, end = ' ')


def ukol2():
    """kter� vyp�e jm�na dom�c�ch zv��at, kter� za��naj� na k"""
    
    for zvire in zvirata:
        if zvire.startswith('k'):
            print(zvire, end = ' ')

def ukol3(slovo):
    """funkce dostane slovo a zjist�, jestli je v seznamu dom�c�ch zv��at"""
    return slovo in zvirata

def ukol4(seznam1, seznam2):
    """dostane dva seznamy jmen zv��at, a vr�t� t�i seznamy:
    (a)Zv��ata, kter� jsou v obou seznamech
    (b)Zv��ata, kter� jsou v jen prvn�m seznamu
    (c)Zv��ata, kter� jsou v jen druh�m seznam"""
    
    
    seznam_spolecnych = []
    seznam_prvni = []
    seznam_druhe = []
    
    for zvire in seznam1:
        if zvire in seznam2:
            seznam_spolecnych.append(zvire)
        else:
            seznam_prvni.append(zvire)
            
    for zvire in seznam2:
        if zvire not in seznam1:
            seznam_druhe.append(zvire)
            
    return (seznam_spolecnych, seznam_prvni, seznam_druhe)
    
def ukol5():
    """seradi zvirata dle abecedy"""
    
    for i in range(len(zvirata) -1 ):
        for j in range(len(zvirata) - i - 1 ):
            if zvirata[j] > zvirata[j+1]:
                #bublej zvire dal v seznamu
                temp = zvirata[j + 1]
                zvirata[j+1] = zvirata[j]
                zvirata[j] = temp
    print(zvirata)
    
def ukol6(zvirata):
    """seradi zvirata dle abecedy, ale ignoruje prvni pismenko zvirete"""
    for i in range(len(zvirata) -1 ):
        for j in range(len(zvirata) - i - 1 ):
            #porovnavam podle 2.pismena zvirete
            if zvirata[j][1] > zvirata[j+1][1]:
                #bublej zvire dal v seznamu
                temp = zvirata[j + 1]
                zvirata[j+1] = zvirata[j]
                zvirata[j] = temp
    print(zvirata)
 
def ukol7(rim):
    
       
def main():
    ukol6(zvirata2)
    
main()