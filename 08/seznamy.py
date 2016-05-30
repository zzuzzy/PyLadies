#--*--encoding:1250--*--
'''
Created on 24. 5. 2016

@author: zuzana.kasakova
'''


seznam = ['naucit se python', 'darovat krev', 'vycestovat na Island']

# se seznamy lze pracovat stejne jako s retezci - vyrezy 
#vytisteni dvou poslednich radku
#print(seznam[-2:])


tel_seznam = []

#pridavani 
tel_seznam.append('Zuzka 123 321 123')

#zahozeni existujiciho seznamu
tel_seznam = []
tel_seznam.append('Terka 666 777 888')
tel_seznam.append('Vasek 222 222 222')
tel_seznam.append('oskar 777 777 777')

#print(tel_seznam)
#1.oprava posledniho prvku
tel_seznam[-1] = 'Oskar 777 777 777'
#print(tel_seznam)

# POZOR nelze zmenit jedno konkretni pismeno - vyhodi se TypeError
#tel_seznam[-1][0] = 'O'
#print(tel_seznam)


tel_seznam.append('Bozena 121 121 121')

druhy_seznam =['Lenka 567 467 465', 'Petr 777 888 999']

#spojeni seznamu do noveho

spojeny_seznam = tel_seznam + druhy_seznam

#rozsireni stavajiciho  seznamu
tel_seznam.extend(druhy_seznam)

#serazeni seznamu
tel_seznam.sort()

#for item in tel_seznam:
   # print(item)

#metoda sorted(seznam) nezmeni seznam
#print(spojeny_seznam)
#print(sorted(spojeny_seznam))
#print(spojeny_seznam)

#serazeni v opacnem poradi
vysledky = ['5 Petr', '3 Honza', '7 Jan']
#print(vysledky)
vysledky.sort(reverse=True)
#print(vysledky)

vse = ['Honza', 3.234, 60, [1,2,3], 'Ahoj']
#nelze seradit, nebot neumi porovna napr. string a float

#vse.sort()

#mazani prvku
del vse[0]

batoh = []
batoh.append('boty')
batoh.append('spacak')
batoh.append('obleceni')
batoh.append('svacina')
batoh.append('celovka')

#print(batoh)

vyndana_vec = batoh.pop()

#print(batoh, 'vyndana vec', vyndana_vec)

####            Princip append a pop odpovida zasobniku - stack - LIFO , last in first out
####            Fronta - queue je LIFO

# funkce remove
#print(batoh)
batoh.remove('svacina')
#print(batoh)
#zjisteni pozice prvniho vyskytu prvku
batoh.index('boty')
batoh.count('boty')

#rozdeleni retezce - split - automaticky rozdeluje dle mezery
p = 'pýcha, pytel, pysk, netopýr, slepýš, pyl, kopyto, klopýtat, třpytit se, zpytovat, pykat, pýr, pýřit se, čepýřit se'
#print(p, type(p))
vp = p.split()

vp = p.split(', ')

#zjistit kolik je ve vstupu vyjmenovanych slov po p

vstup = 'netopýr nemá kopyto'
celkem = 0
for slovo in vstup.split():
    if slovo in vp:
        celkem += 1

vstup = 'netopýr nemá kopyto netopýr je savec'

#kolikrát je ve vstupu vyjmenovano slovo
celkem = 0


for slovo in vstup.split():
    if slovo in vp:        
        celkem += 1
        print(slovo, celkem)  



#  !!!!!!!!!!!!!1 pozor

a = ['-', '-', '-']
#b = a
#a[2] = 'x'
# a i b budou stejne
#print(a, b)
#kopirovani seznamu
b = list(a)
a[2] = 'x'
print(a, b)



