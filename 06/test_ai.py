'''
Created on 29. 5. 2016

@author: zzuzzy
'''
from ai import  tah_pocitace

def test_ai():
    assert tah_pocitace("","x") == ""
    assert tah_pocitace("---", "x") ==  "---"