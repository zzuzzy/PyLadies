#--*-- encoding:1250 --*--

from util import tah

def vyhodnot(pole, znakHrac, znakPC):
    
    if (znakHrac*3 in pole):
        return znakHrac
    elif (znakPC*3 in pole):
        return znakPC
    elif "-" not in pole:
        return "!"
    else:
        return "-"    

    
def tah_hrace(pole, znakHrac):
    if "" == pole:
        return pole
    while True:
        try:
            pozice = int(input('Zadejte ��slo pol��ka: '))
        except TypeError:
            print("Chyba vstupu. Opakujte.")
        except ValueError:
            print("Chyba vstupu. Opakujte.")
        else:
            if pozice > len(pole):
                print("��slo pol��ka nesm� p�ekro�it {0}".format(len(pole)))
            elif pozice < 0:
                print("��slo pol��ka mus� b�t kladn�")
            elif "o" == pole[pozice] or "x" == pole[pozice]: 
                #kontrola obsazenosti pole
                print("Toto pol��ko je ji� obsazeno")
                continue                
            else:
                return tah(pole, pozice, znakHrac)
                

    