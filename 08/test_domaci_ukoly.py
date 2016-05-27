# --*-- encoding:1250 --*--
'''
Created on 27. 5. 2016

@author: zzuzzy
'''
zvirata = ["pes", "ko�ka", "kr�l�k", "had"]

from domaci_ukoly import ukol4

def test_ukol4():
    assert  ukol4([], []) == ([], [], [])
    assert ukol4([], ['pes', 'ko�ka']) == ([], [], ['pes', 'ko�ka'])
    assert ukol4(['pes', 'kocka'], ['holub', 'slepice']) == ([], ['pes', 'kocka'], ['holub', 'slepice'])
    assert ukol4(['pes', 'kocka'], ['holub', 'kocka']) == (['kocka'], ['pes'], ['holub'])
    assert ukol4(zvirata, zvirata) == (zvirata, [], [])
    