'''
Created on 24. 5. 2016

@author: zuzana.kasakova
'''

a = ['-','-','-']
b = ['-','x','-']
c = ['-','-','-']

hraci_pole = [a,b,c]

#print(hraci_pole)

#for i in hraci_pole:
#    print(i)

for radek in hraci_pole:
    for znak in radek:
        print(znak, end='')
    print()
    
