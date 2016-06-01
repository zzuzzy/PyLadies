#--*--encoding:1250--*--
'''
Created on 31. 5. 2016

@author: zuzana.kasakova
'''

# JSON je vlastně velmi podobný zápis jako u slovníku, ale vše musí být uvedeno v uvozovkách

import json

#vytvorim rezetec. Nemusi byt nutne odsazovany, mezery jsou ignorovany. Na vice radcich je to psano pouze pro prehlednost.
json_retezec = """
    {
        "jméno" : "Anna",
        "město" : "Brno",
        "jazyky" : ["angličtina", "němčina", "Python"],
        "věk" : 26
    }
    """
#odnekud ziskam retezec, ze ktereho chci ziskat konkretni data a hodnoty - json.loads   
data = json.loads(json_retezec)

print(data)

print(data["město"])
        
for k, v in data.items():
    print(k, ' : ', v)


#ze ziskanych dat chci zpet vytvorit retezec
print(json.dumps(data))
#ovsem kvuli kodovani je vhodnejsi
print(json.dumps(data, indent = 2,  ensure_ascii=False))

