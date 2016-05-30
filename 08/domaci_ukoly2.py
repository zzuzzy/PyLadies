#--*-- encoding:1250 --*--
'''
Created on 30. 5. 2016

@author: zzuzzy
'''

def ukol9():
    """vyp�e b�sni�ku ze souboru basnicka.txt , ale obr�t� po�ad� ver�� (t.j. jako prvn� vyp�e posledn� ��dek, atd."""
    with open('basnicka.txt', 'r') as soubor:      
        content = soubor.readlines() 
        content.reverse() 
        for item in content:
        
            print(item.rstrip())

def ukol10():
    """obr�t� po�ad� slov v jednotliv�ch ver��ch"""
    
    with open('basnicka.txt', 'r') as soubor:  
        for line in soubor:
            line = line.rstrip().split()  
            line.reverse()
            line = " ".join(line)
            print(line)
 
def ukol11():
    """Obra� po�ad� slok (ty by m�ly b�t odd�len� jedn�m pr�zdn�m ��dkem)."""
    with open('basnicka.txt', 'r') as soubor:  
        content = soubor.read().rstrip()
        seznam = content.split("\n\n")
        seznam.reverse()
        content = "\n\n".join(seznam)
        print(content)
    
       
def main():
    ukol11()

main()