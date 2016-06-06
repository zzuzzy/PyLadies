#--*--encoding:1250--*--
'''
Created on 6. 6. 2016

@author: zuzana.kasakova
'''
from domaci_ukoly3_hra import pohyb
from pytest import  raises

def test_nakresli_mapu():
    pass

def test_pohyb():
    assert(pohyb([(0,0)], "v")) == [(0,1)]
    assert(pohyb([(0,1)], "v")) == [(0,2)]
    assert(pohyb([(0,2)], "j")) == [(1,2)]
    assert(pohyb([(1,2)], "s")) == [(0,2)]
    assert(pohyb([(0,0), (0,1), (1,1)], "z")) == [(0,1), (1,1), (1,0)]
    
    with raises(ValueError):
        pohyb([(0, 0), (1, 0), (2, 0)], "z")
    