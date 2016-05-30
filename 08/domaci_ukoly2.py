#--*-- encoding:1250 --*--
'''
Created on 30. 5. 2016

@author: zzuzzy
'''

def ukol9():
    """vypíše básničku ze souboru basnicka.txt , ale obrátí pořadí veršů (t.j. jako první vypíše poslední řádek, atd."""
    with open('basnicka.txt', 'r') as soubor:      
        content = soubor.readlines() 
        content.reverse() 
        for item in content:
        
            print(item.rstrip())

def ukol10():
    """obrátí pořadí slov v jednotlivých verších"""
    
    with open('basnicka.txt', 'r') as soubor:  
        for line in soubor:
            line = line.rstrip().split()  
            line.reverse()
            line = " ".join(line)
            print(line)
 
def ukol11():
    """Obrať pořadí slok (ty by měly být oddělené jedním prázdným řádkem)."""
    with open('basnicka.txt', 'r') as soubor:  
        content = soubor.read().rstrip()
        seznam = content.split("\n\n")
        seznam.reverse()
        content = "\n\n".join(seznam)
        print(content)
    
       
def main():
    ukol11()

main()