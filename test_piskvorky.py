'''
Created on 17. 5. 2016

@author: zuzana.kasakova
'''
from piskvorky import tah_pocitace

def test_zakladni_tah():
    pole = "-" * 20
    pole = tah_pocitace(pole)
    # kontrola, zda i po tahu je v poli stale jen 20 znaku
    assert len(pole) == 20
    #kontrola, zda pole obsahuje jeden krizek
    assert pole.count('x') == 1
    assert pole.count('-') == 19
    
