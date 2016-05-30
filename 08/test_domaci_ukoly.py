# --*-- encoding:1250 --*--
'''
Created on 27. 5. 2016

@author: zzuzzy
'''
zvirata = ["pes", "kočka", "králík", "had"]

from domaci_ukoly import ukol4

def test_ukol4():
    assert  ukol4([], []) == ([], [], [])
    assert ukol4([], ['pes', 'kočka']) == ([], [], ['pes', 'kočka'])
    assert ukol4(['pes', 'kocka'], ['holub', 'slepice']) == ([], ['pes', 'kocka'], ['holub', 'slepice'])
    assert ukol4(['pes', 'kocka'], ['holub', 'kocka']) == (['kocka'], ['pes'], ['holub'])
    assert ukol4(zvirata, zvirata) == (zvirata, [], [])
    
def test_ukol7():
    assert ukol7("I") == 1
    assert ukol7("II") == 2
    assert ukol7("III") == 3
    assert ukol7("IV") == 4
    assert ukol7("V") == 5
    assert ukol7("VI") == 6
    assert ukol7("IX") == 9
    assert ukol7("X") == 10
    assert ukol7("XX") == 20
    assert ukol7("L") == 50
    assert ukol7("C") == 100
    assert ukol7("D") == 500
    assert ukol7("M") == 1000
    assert ukol7("i") == 1
    assert ukol7("v") == 5
    assert ukol7("LIIIVII") == 87
    assert ukol7("CDXCIV") == 494
    