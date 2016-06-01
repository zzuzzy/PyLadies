'''
Created on 31. 5. 2016

@author: zuzana.kasakova
'''
import requests


with open('token.txt') as soubor:
    token = soubor.read().strip()

hlavicky = {'Authorization': 'token ' + token}

stranka = requests.put('https://api.github.com/user/starred/pyladiescz/pyladies.cz', headers = hlavicky)  
stranka.raise_for_status()
#Chceš-li hvìzdièku zase odstranit, použij metodu DELETE na stejnou adresu.

#veskera dokumentace API - vyhledat github API documentation
# https://developer.github.com/v3/




