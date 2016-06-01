'''
Created on 31. 5. 2016

@author: zuzana.kasakova
'''

import requests, json

#stazeni stranky
stranka = requests.get('https://github.com/')

#overeni
stranka.raise_for_status()

#vypsani obsahu
#print(stranka.text)

with open('token.txt') as soubor:
    token = soubor.read().strip()

hlavicky = {'Authorization': 'token ' + token}

stranka = requests.get('https://api.github.com/user', headers = hlavicky)  
stranka.raise_for_status()
print(stranka.text)

#vytvoreni ze ziskaneho textu Python objektu

data = json.loads(stranka.text)

print(json.dumps(data, indent = 2))
print(data["login"])


    
    