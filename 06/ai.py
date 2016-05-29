from random import randrange
from util import tah
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
            pozice = pole.index("-" + symbolPC + "-") + 2
        elif re.search(symbolPC + "-+" + symbolPC + "-", pole):
            pozice = pole.index("-" + symbolPC + "-")
        else:
            pozice = pole.index("-" + symbolPC + "-") + randrange(0,4,2)
       
    #utocny tah        
    elif(symbolPC + "---" + symbolPC in pole):
        pozice = pole.index(symbolPC + "---" + symbolPC) + 2
        
    #blokace protihrace
    elif("-" + symbolHrace + "-" in pole):
        
        if re.search("-"+ symbolHrace + "-+" + symbolHrace, pole):
            pozice = pole.index("-" + symbolHrace + "-") + 2
        elif re.search(symbolHrace + "-+" + symbolHrace + "-", pole):
            pozice = pole.index("-" + symbolHrace + "-")
        else:      
            pozice = pole.index("-" + symbolHrace + "-") +  randrange(0,4,2)    
           
    #zaloz utok    
    elif(symbolPC + "----" in pole):        
        pozice = pole.index(symbolPC + "----") + 4
    elif("----" + symbolPC in pole):      
        pozice = pole.index("----" + symbolPC)
                
    #nahodna strategie, selhaly ostatni
    else:
    
        while True:
            if "-" not in pole:
                print("Pocitac nemuze na pole hrat")            
                return pole
            pozice = randrange(0, len(pole))
            if ("-"*len(pole) == pole) and ((pozice == 0) or (pozice == len(pole)-1)):
                #je-li pole jeste prazdne, nehraj na krajni policka
                continue
            if "-" == pole[pozice]:
                break                
    
    return tah(pole, pozice, symbolPC)