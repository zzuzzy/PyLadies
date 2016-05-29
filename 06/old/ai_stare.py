#--*-- encoding:1250 --*--
import random

def vyhra_xx(pole):
    """Funkce zahraje zprava treti "x" vedle dvou jiz existujicich"""
    pozice = pole.index("xx-")
    #pocitac zahraje na policko pozice + 2
    return pole[:pozice + 2] + "x" + pole[pozice + 3:]
 
def vyhra_xx2(pole):
    """Funkce zahraje zleva treti "x" vedle dvou jiz existujicich"""
    pozice = pole.index("-xx")
    #pocitac zahraje na policko pozice 
    return pole[:pozice] + "x" + pole[pozice + 1:]
    
def vyhra_x_x(pole):
    """Funkce zahraje zleva treti "x" mezi dve jiz existujici"""
    pozice = pole.index("x-x")
    return pole[:pozice+1]+"x"+pole[pozice+2:]

def tah_pocitace_strategie(pole):
    # vitezna strategie-> mohu umistit treti x vedle dvou existujicich
    if "xx-" in pole:
        return vyhra_xx(pole)  
    elif "-xx" in pole:
        return vyhra_xx2(pole)
    elif "x-x" in pole:
        return vyhra_x_x(pole)
    
    #pc musi zahrat tah (zatim nahodny)
    return tah_pocitace()
    
def tah_pocitace(pole):    
    """Funkce dostane řetězec s herním polem, vybere pozici, na kterou hrát, a vrátí
    herní pole se zaznamenaným tahem počítače """
     
    while True:
        # tah, ktery zabrani okamzite vyhre soupere xoo- doplnit na xoox, resp. naopak ci na zacatku nebo na konci pole
        
        #tah pokud mozno blokujici rozehru protihrace a nejlepe hned vedle sveho symbolu "x"
        if "ox-" in pole:
            pozice = pole.index("ox-")
            return pole[:pozice+2] + "x" + pole[pozice+3:]
        if "-xo" in pole:
            pozice = pole.index("-xo")
            return pole[:pozice] + "x" + pole[pozice+1:]
        if "o-x" in pole:
            pozice = pole.index("o-x")
            return pole[:pozice+1] + "x" + pole[pozice+2:]
        if "x-o" in pole:
            pozice = pole.index("x-o")
            return pole[:pozice+1] + "x" + pole[pozice+2:]
        if "-o" in pole:
            pozice = pole.index("-o")
            return pole[:pozice]+"x"+pole[pozice+1:]
        if "o-" in pole:
            pozice = pole.index("o-")
            return pole[:pozice+1]+"x"+pole[pozice+2:]
        
        # tah pokud mozno vedle jiz existujiciho "x"
        if "-x" in pole:
            pozice = pole.index("-x")
            return pole[:pozice] + "x" + pole[pozice+1:]
        if "x-" in pole: 
            pozice = pole.index("x-")
            return pole[:pozice+1] + "x" + pole[pozice+2:]
        # nahodna volba
        pozice = random.randrange(0,20)
        #kontrola obsazenosti pozice
        if (pole[pozice] == "-"):
            return pole[:pozice] + "x" + pole[pozice + 1:]