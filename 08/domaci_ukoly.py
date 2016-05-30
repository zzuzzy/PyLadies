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
    
def ukol5b():
    zvirata.sort()
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
    
def ukol6b(zvirata):
    dict_zvirata = []
    
    for zvire in zvirata:
        dict_zvirata.append([zvire[1],zvire])
    dict_zvirata.sort()
    
    return [item[1] for item in dict_zvirata]
        
     



def ukol7(rnumber):
    
    romanNums = ["I", "V", "X", "L", "C", "D", "M"]
    arabicValues = [1, 5, 10, 50, 100, 500, 1000]
  #  bothValues = zip(romanNum, arabicValues)
    
    arabicNumber = 0
    rnumber = rnumber.upper()
    
    for i in range(len(romanNums)):
        romanNumsSorted = list(enumerate(romanNums))
        
    reverseNumber = list(rnumber)
    reverseNumber.reverse()
    
    previous = arabicValues[romanNums.index(reverseNumber[0])]
    
    #cte zadane cislo "zprava" a pricita si hodnoty rimskych cifer
    for i in range(len(reverseNumber)):      
        #jestlize je aktualni rimska cislice mensi mensi nez predchozi, musim ji odecist        
        actual = arabicValues[romanNums.index(reverseNumber[i])]     
        if actual < previous:          
            arabicNumber -= actual
        else:          
            arabicNumber += arabicValues[romanNums.index(reverseNumber[i])]            
        previous = actual
     
    print("��msk� ��slo {0} p�edstavuje arabsk� ��slo {1}".format(rnumber, arabicNumber))   
    return arabicNumber
       
def main():
    ukol7("CDXCIV")
    
main()