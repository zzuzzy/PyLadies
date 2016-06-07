'''
Created on 7. 6. 2016

@author: zuzana.kasakova
'''
def a():
    return 3

def b(jina_funkce):
    jina_funkce()
    
    
print(a)
print(a())
print(b)
print(b(a)) # toto melo vytisknout 3

print("-----------------")

def fa(parametr):
    return parametr

def fb(jina_funkce, *args):
    return jina_funkce(*args)

def fc(jina_funkce):
    return jina_funkce(333)

print(fa)
print(fa(2))
print(fb)
print(fb(fa,22)) # toto melo vytisknout 3
print(fc(fa))
