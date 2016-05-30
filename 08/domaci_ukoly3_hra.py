#--*-- encoding:1250--*--
'''
Created on 30. 5. 2016

@author: zzuzzy
'''

def nakresli_mapu(souradnice):

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
    
    for (i, j) in souradnice:
        mapa[i][j] = "X"
        
    
    for i in range(len(mapa)):    
        print("".join(mapa[i]))    


def pohyb(souradnice, smer):
    """Napiš funkci pohyb, která dostane seznam souřadnic a světovou stranu ("s","j","v" nebo "z"), a přidá k seznamu poslední bod „posunutý“ v daném směru. Např.:
    souradnice = [(0, 0)]
    pohyb(souradnice, 'v')
    print(souradnice)  # → [(0, 0), (0, 1)]
    """
    smery = dict({"v":(0,1), "j":(1,0), "z":(0,-1), "s": (-1,0)})
    
    souradnice.append((souradnice[-1][0] + smery[smer][0], souradnice[-1][1] + smery[smer][1]))
    
    return souradnice
            

def main():
    nakresli_mapu([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9)])
    print(pohyb([(0, 0)], "v"))
    print(pohyb([(0, 0), (0, 1), (0, 2)], "j"))
    
main()
