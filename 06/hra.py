
from piskvorky import tah_hrace
from piskvorky import vyhodnot
from ai import tah_pocitace
from random import randrange

def piskvorky1D():
    
    pole = "-" * 20
    
    # kdo ma jaky znak 0:PC-x a hrac-o, 1:PC-o a hrac-x
    if randrange(0, 2):
        znakPC = "x"
        znakHrac = "o"        
    else:
        znakPC = "o"
        znakHrac = "x"
    
    print("Hrac ma", znakHrac)
    
    while True:            
       
        pole = tah_pocitace(pole, znakPC)
        print(pole)
        if "-" != vyhodnot(pole, znakHrac, znakPC):
            # jiz neni volne pole
            break
        pole = tah_hrace(pole, znakHrac)
        print(pole)
        if "-" != vyhodnot(pole, znakHrac, znakPC):
            # jiz neni volne pole
            break
    
    if "o" == vyhodnot(pole, znakHrac, znakPC):
        print("Vyhral hrac s kolecky")
    elif "x" == vyhodnot(pole, znakHrac, znakPC):
        print("Vyhral hrac s krizky")
    else:
        print("Remiza")

        
piskvorky1D()
