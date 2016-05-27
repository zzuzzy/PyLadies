from random import randrange
from piskvorky import tah
import re

def tah_pocitace(pole, symbol):
    symbolPC = symbol
    
    if "x" == symbolPC:
        symbolHrace = "o"
    else:
        symbolHrace = "x"
    
    
    #Vyherni tah pocitace
    
    if(symbolPC*2+"-" in pole):
        pozice = pole.index(symbolPC*2+"-") + 2
    elif(symbolPC+"-"+symbolPC in pole):
       pozice = pole.index(symbolPC+"-"+symbolPC) + 1
    elif("-"+symbolPC*2 in pole):
        pozice = pole.index("-"+symbolPC*2)
    
    #obrana proti okamzitemu vitezstvi
    
    elif(symbolHrace*2 + "-" in pole):
        pozice = pole.index(symbolHrace*2 + "-") + 2
    elif(symbolHrace + "-" + symbolHrace in pole):
        pozice = pole.index(symbolHrace + "-" + symbolHrace) +1 
    elif("-" + symbolHrace*2 in pole):
        pozice = pole.index("-" + symbolHrace*2)
     
    #utocny tah
    elif("-" + symbolPC + "-" in pole):
        
        if re.search("-" + symbolPC + "-+"+symbolPC, pole):
            print("utok -PC----PC")
            pozice = pole.index("-" + symbolPC + "-") + 2
        elif re.search(symbolPC+"-+" + symbolPC + "-", pole):
            print("utok PC--PC-")
            pozice = pole.index("-" + symbolPC + "-")
        else:
            print("utok -PC-")
            pozice = pole.index("-" + symbolPC + "-") + randrange(0,4,2)
       
    #blokace protihrace
    elif("-" + symbolHrace + "-" in pole):
        print("Blokace -H-")
        #TODO regularni vyraz 
        pozice = pole.index("-" + symbolHrace + "-" )
        
    #utocny tah
        
    elif(symbolPC + "---" + symbolPC in pole):
        print("Utok PC---PC")
        pozice = pole.index(symbolPC + "---" + symbolPC) + 2
    elif(symbolPC + "----" in pole):
        print("Utok PC----")
        pozice = pole.index(symbolPC + "----") + 4
    elif("----" + symbolPC in pole):
        print("Utok ----PC")
        pozice = pole.index("----" + symbolPC)
    
        
    
    #nahodna strategie, selhaly ostatni
    else:
    
        while True:
            if "-" not in pole:
                print("Pocitac nemuze na pole hrat")            
                return pole
            pozice = randrange(0, len(pole))
            if "-" == pole[pozice]:
                break
        
    
    return tah(pole, pozice, symbolPC)