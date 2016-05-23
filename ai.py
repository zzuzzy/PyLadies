import random
def vyhraj(pole):
    """pocitac tahne na vyhru doplnenim jednoho "o" zprava ci zleva k "oo" nebo doprostred k "o-o" """
    if "-xx" in pole:
        pozice = pole.index("-xx")
        return pole[:pozice] + "x" + pole[pozice+1:]
    if "xx-" in pole:
        pozice =  pole.index("xx-")
        return pole[:pozice+2] + "x" + pole[pozice+3:]
    if "x-x" in pole:
        pozice = pole.index("x-x")
        return pole[:pozice+1] + "x" + pole[pozice+2:]
  
def bran_se(pole):
    """protihrac by mohl v pristim tahu vyhrat, pocitac tahne tak, aby zabranil okamzite vyhre protihrace """
    
    if "-oo" in pole:
        pozice = pole.index("-oo")
        return pole[:pozice] + "x" + pole[pozice+1:]
    if "oo-" in pole:
        pozice =  pole.index("oo-")
        return pole[:pozice+2] + "x" + pole[pozice+3:]
    if "o-o" in pole:
        pozice = pole.index("o-o")
        return pole[:pozice+1] + "x" + pole[pozice+2:]  
    
def zahrajx_x_x(pole):
    """tahni tak, aby se v poli objevili dve x v nasledujicim tvaru "x-x-x""" 
    pozice = pole.index("x---x")
    return pole[:pozice+2] + "x" + pole[:pozice+4]
 
    
def zahrajx_x(pole):
    """tahni tak, aby se v poli objevili dve x v nasledujicim tvaru "x---x""" 
    if "x----" in pole:
        pozice = pole.index("x----")
        return pole[:pozice+4] + "x" + pole[pozice+5:]
    if "----x" in pole:
        pozice = pole.index("----x")
        return pole[:pozice] + "x" + pole[pozice+1:]        
    
def tah_pocitace(pole):    
        
    #kontrola, zda pocitac nemuze okamzite vyhrat
    if ("-xx" in pole) or ("xx-" in pole) or ("x-x" in pole):
        return vyhraj(pole)
    
    #kontrola, zda nemuze protihrac tahnout na vitezstvi
    if ("-oo" in pole) or ("oo-" in pole) or ("o-o" in pole):
        return bran_se(pole)
    
    #muzes zahrat x mezi "x---x"? 
    if ("x---x" in pole):
        return zahrajx_x_x(pole)
       
    #zahraj tak, aby se v poli objevili dve x v nasledujicim tvaru "x---x". V dalsim kole se snad umistit x doprostred.
    
    if("x----" in pole) or ("----x" in pole):
        return zahrajx_x(pole)  
    
    #TODOzahraj o--o + zabran x--x
    
    #TODOzahraj tak, abys blokoval protihrace, tj. hned vedle nej
    
    #vsechny predchozi strategie se neuplatnili, umisti "o" nahodne do volneho mista
    while True:
        pozice = random.randrange(0,20)
        if (pole[pozice] == "-"):
            return pole[:pozice] + "x" + pole[pozice + 1:]