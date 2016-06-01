#--*--encoding:1250--*--
'''
Created on 31. 5. 2016

@author: zuzana.kasakova
'''

# JSON je vlastn� velmi podobn� z�pis jako u slovn�ku, ale v�e mus� b�t uvedeno v uvozovk�ch

import json

#vytvorim rezetec. Nemusi byt nutne odsazovany, mezery jsou ignorovany. Na vice radcich je to psano pouze pro prehlednost.
json_retezec = """
    {
        "jm�no" : "Anna",
        "m�sto" : "Brno",
        "jazyky" : ["angli�tina", "n�m�ina", "Python"],
        "v�k" : 26
    }
    """
#odnekud ziskam retezec, ze ktereho chci ziskat konkretni data a hodnoty - json.loads   
data = json.loads(json_retezec)

print(data)

print(data["m�sto"])
        
for k, v in data.items():
    print(k, ' : ', v)


#ze ziskanych dat chci zpet vytvorit retezec
print(json.dumps(data))
#ovsem kvuli kodovani je vhodnejsi
print(json.dumps(data, indent = 2,  ensure_ascii=False))

