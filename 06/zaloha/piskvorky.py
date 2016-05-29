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
            pozice = int(input('Zadejte číslo políčka: '))
        except TypeError:
            print("Chyba vstupu. Opakujte.")
        except ValueError:
            print("Chyba vstupu. Opakujte.")
        else:
            if pozice > len(pole):
                print("Číslo políčka nesmí překročit {0}".format(len(pole)))
            elif pozice < 0:
                print("Číslo políčka musí být kladné")
            elif "o" == pole[pozice] or "x" == pole[pozice]: 
                #kontrola obsazenosti pole
                print("Toto políčko je již obsazeno")
                continue                
            else:
                return tah(pole, pozice, znakHrac)
                

    