#--*-- encoding:1250--*--
'''
Created on 30. 5. 2016

@author: zzuzzy
'''
from random import randrange

def nakresli_mapu(souradnice, potrava):

    """Napiš funkci, která dostane seznam souřadnic (párů čísel menších než 10), a vypíše je jako mapu. Například:
    nakresli_mapu([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9)])
    X X . . . . . . . .
    . . . . . . . . . .
    . . X . . . . . . .
    . . . . X . . . . .
    . . . . . . . . . .
    . . . . . . . . . .
    . . . . . . . . . .
    . . . . . . . . . .
    . . . . . . . . . .
    . . . . . . . . X .

    """
    
    mapa = []
    for i in range(10): 
        row = []      
        for j in range(10):
            row.append(".")
        mapa.append(row)
        
    mapa[potrava[0]][potrava[1]] = '?'
    
    for (i, j) in souradnice:
        mapa[i][j] = "X"
        
    
    for i in range(len(mapa)):    
        print("".join(mapa[i]))    


def posun(a,b):    
    return (a[0]+b[0], a[1]+b[1])

def vytvor_potravu(souradnice):
    while True:
        potrava = (randrange(0,9), randrange(0,9))
        if not potrava in souradnice:
            return potrava
    

def pohyb(souradnice, smer, potrava):
   
    smery = dict({"v":(0,1), "j":(1,0), "z":(0,-1), "s": (-1,0)})
    
    #kontrola pohybu mimo mapu
    nova_pozice =  posun(souradnice[-1], smery[smer])    
    if not((0 <= nova_pozice[0] <= 9) and (0 <= nova_pozice[1] <= 9)):
        raise ValueError("Hra skon�ila. Nedovolen� pohyb.")    
    
    #kontrola pohybu na pole, ktere uz v seznamu je
    
    if nova_pozice in souradnice:
        raise ValueError("Hra skon�ila. Pohyb mimo mapu")    
    

    
    #pohyb    
  
    souradnice.append(nova_pozice)  
        #narazil had na potravu?
    if nova_pozice == potrava:
        
        # vygeneruj novou potravu            
        potrava = vytvor_potravu(souradnice) 
        
        return(souradnice, potrava)
    #had nenarazil na potravu, musi se zkratit           
    if souradnice:
        del souradnice[0]
        
    return (souradnice, potrava)
            

def main():
    #inicializace
    souradnice = [(0, 0), (1, 0), (2, 0)]
    potrava = vytvor_potravu(souradnice)
    nakresli_mapu(souradnice, potrava)
    
    #hlavni cyklus
    while True:
        #Uzivatel je vyzvan z zadani svetove strany
        try:
            smer = input("Zadejte sm�r pohybu [v, j, z, s] (nebo q pro ukonceni)")
        except ValueError as err:
            print("Zadejte vstup znovu. �patn� vstup: ", err)
        else:
            if smer.lower() == 'q':
                break
            if smer.lower() not in ["v", "j", "z", "s"]:
                print("Zadejte vstup znovu[v, j, z, s]") 
        
        #Je proveden pohyb
        try:
            (souradnice, potrava) = pohyb(souradnice, smer, potrava)
        except ValueError as err:
            print(err)
            break
        
        
        #vykresleni mapy s novym pohybem
        nakresli_mapu(souradnice, potrava)
        
main()
