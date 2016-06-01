# --*--encoding:1250--*--
'''
Created on 31. 5. 2016

@author: zuzana.kasakova
'''

zvirata = [["pes", 2], ["kočka", 1], ["králík", 5], ["had", 3]]


def ohodnoceni():
    pass

zvirata.sort()
print(zvirata)

#pro serazeni dle druheho indexu je mozna nutna funkce lambda zvirata.sort(key = lambda:....)
zvirata = sorted(zvirata, key = lambda x:x[1])
print(zvirata)
