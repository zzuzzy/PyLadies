#--*--encoding:1250--*--
'''
Created on 31. 5. 2016

@author: zuzana.kasakova
'''

slovnik = {'cz':'�esk� republika', 'sk':'Slovensk� republika'}

slovnik['us'] = "Spojen� st�ty"
slovnik['de'] = "N�mecko"

#na poradi ve slovniku nezalezi - slovnik vytiskne zaznamy prehazene

print(slovnik)
print(slovnik['cz'])

#nasledujici volani vyhodi KeyError, nebot klic 3 neni ve slovniku
#print(slovnik[3])

print(slovnik.get('us'))

#metoda get nevyhodi KeyError, pokud klic ve slovniku neni
print(slovnik.get('ru'))

slovnik['ru'] = "Rusko"
print(slovnik)
#vyjimani ze slovniku
zaznam = slovnik.pop('ru')
print(zaznam)
print(slovnik)


#prochazeni slovnikem
for klic in slovnik:
    print(klic)
    
for (klic, hodnota) in slovnik.items():
    print(klic, 'je klic pro', hodnota)

#smazani zaznamu
del slovnik['us']

print(slovnik.items())
print(slovnik.keys())
print(slovnik.values())

print(len(slovnik))




