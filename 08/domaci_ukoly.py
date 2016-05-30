#--*-- encoding:1250 --*--

zvirata = ["pes", "kočka", "králík", "had"]
zvirata2 = ["pes", "kočka", "králík", "had", "andulka"]

def ukol1():
    """vypíše jména domácích zvířat, která jsou kratší než 5 písmen"""
   
    for zvire in zvirata:
        if len(zvire) < 5:
            print(zvire, end = ' ')


def ukol2():
    """která vypíše jména domácích zvířat, která začínají na k"""
    
    for zvire in zvirata:
        if zvire.startswith('k'):
            print(zvire, end = ' ')

def ukol3(slovo):
    """funkce dostane slovo a zjistí, jestli je v seznamu domácích zvířat"""
    return slovo in zvirata

def ukol4(seznam1, seznam2):
    """dostane dva seznamy jmen zvířat, a vrátí tři seznamy:
    (a)Zvířata, která jsou v obou seznamech
    (b)Zvířata, která jsou v jen prvním seznamu
    (c)Zvířata, která jsou v jen druhém seznam"""
    
    
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
     
    print("Římské číslo {0} představuje arabské číslo {1}".format(rnumber, arabicNumber))   
    return arabicNumber
       
def main():
    ukol7("CDXCIV")
    
main()