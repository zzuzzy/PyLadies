from random import randrange
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
  
def bran_se_proti_vitezstvi(pole):
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

def bran_o3o(pole):
    """zabrani protihraci tah z o---o na oo--o nebo na o--oo"""
    
    pozice = pole.index("o---o")
    # zjisteni, zda uz nejake x vedle o lezi, pak bude pocitac hrat k samotnemu o
    #pripad xo---o? 
    if pole[pozice-1] == "x":
        #zahraj o--xo
        return pole[:pozice+3] + "x" + pole[pozice+4:]
    #pripad ?o---ox
    if pole[pozice+5] =="x":
        #zahraj ox--o
        return pole[:pozice+1] + "x" + pole[pozice+2:]
    #TODOostatni -random zda zahraju na pozici 1 nebo 3 - vygeneruju si bud 1 nebo 3
    nahoda = randrange(1,4,2)
    
    return pole[:pozice+nahoda] + "x" + pole[pozice+nahoda+1:]


def zahrajx_x_x(pole):
    """tahni tak, aby se v poli objevili dve x v nasledujicim tvaru "x-x-x""" 
    pozice = pole.index("x---x")
    return pole[:pozice+2] + "x" + pole[pozice+3:]
 
    
def zahrajx_x(pole):
    """tahni tak, aby se v poli objevili dve x v nasledujicim tvaru "x---x""" 
    if "x----" in pole:
        pozice = pole.index("x----")
        return pole[:pozice+4] + "x" + pole[pozice+5:]
    if "----x" in pole:
        pozice = pole.index("----x")
        return pole[:pozice] + "x" + pole[pozice+1:]        
  
def bran_o2o(pole):    
    nahoda = randrange(0,2)
    pozice = pole.index("o--o")
    return pole[:pozice+nahoda+1] + "x" + pole[pozice+nahoda+2:]  

def blokuj_protihrace(pole):
    pozice = pole.index("-o-")
    nahoda = randrange(0,3,2)
    return pole[:pozice+nahoda] + "x" + pole[pozice+nahoda+1:]

def zahraj_xx(pole):
    if "x-" in pole:
        pozice = pole.index("x-")
        return pole[:pozice+1] + "x" + pole[pozice+2:]   
    if "-x" in pole:
        pozice = pole.index("-x")
        return pole[:pozice] + "x" + pole[pozice+1:]
    
def tah_pocitace(pole):    
        
    #kontrola, zda pocitac nemuze okamzite vyhrat
    if ("-xx" in pole) or ("xx-" in pole) or ("x-x" in pole):
        return vyhraj(pole)
    
    ############## OBRANA #####################################
    
    #kontrola, zda nemuze protihrac tahnout na vitezstvi
    if ("-oo" in pole) or ("oo-" in pole) or ("o-o" in pole):
        return bran_se_proti_vitezstvi(pole)
    
     #zahraj tak, abys blokoval protihrace, tj. hned vedle nej
    if ("-o-" in pole):
        #neblokuje hned, zkus rozehrat utok 
        if("-x" in pole) or ("x-" in pole):
            zahraj_xx(pole)
        return blokuj_protihrace(pole)
    
    #obrana, aby protihrac s retezcem o---o nezahral na jiste vitezstvi 
    if("o---o" in pole):
        return bran_o3o(pole)
          
    #zahraj x--x + zabran o--o
    if ("o--o" in pole):
        return bran_o2o(pole)    
    
   
     
     ################## UTOK ############################
     #utocny tah - zahraj x doprostred k x---x 
    if ("x---x" in pole):
        return zahrajx_x_x(pole)
    #zahraj tak, aby se v poli objevili dve x v nasledujicim tvaru "x---x". V dalsim kole se snaz umistit x doprostred.
    
    if("x----" in pole) or ("----x" in pole):
        return zahrajx_x(pole) 
    
           
    #vsechny predchozi strategie se neuplatnily, umisti "x" nahodne do volneho mista
    while True:
        pozice = randrange(0,20)
        if (pole[pozice] == "-"):
            return pole[:pozice] + "x" + pole[pozice + 1:]
        
        
        