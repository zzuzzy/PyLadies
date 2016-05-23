#--*-- encoding:1250--*--
from ai import tah_pocitace

def vyhodnot(pole):
    if ("xxx" in pole):
        return "x"
    elif ("ooo" in pole):
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"
    
def tah(pole, cislo_policka, symbol):
    return  pole[:cislo_policka] + symbol + pole[cislo_policka+1:]

    
def tah_hrace(pole):
    while True:
        try:
            pozice = int(input('Zadejte pozici: '))
        except TypeError:
            print("Chyba vstupu. Opakujte.")
        except ValueError:
            print("Chyba vstupu. Opakujte.")
        else:
            if pozice > len(pole):
                print("Pozice nesmi překročit {0}".format(len(pole)))
            elif pozice < 0:
                print("Pozice musí být kladné číslo")
            elif "o" == pole[pozice] or "x" == pole[pozice]: 
                #kontrola obsazenosti pole
                continue                
            else:
                return tah(pole, pozice, "o")
                

        

def piskvorky1D():
    pole = "-" * 20
    while "-" == vyhodnot(pole):
        pole = tah_hrace(pole)
        print(pole)
        pole = tah_pocitace(pole)
        print(pole)
    
    if "o"== vyhodnot(pole):
        print("Vyhral hrac")
    elif "x" == vyhodnot(pole):
        print("Vyhral pocitac")
    else:
        print("Remiza")
    