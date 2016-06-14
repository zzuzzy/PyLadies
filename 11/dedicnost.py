#--*--encoding:1250--*--
'''
Created on 14. 6. 2016

@author: zuzana.kasakova
'''

class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno   
        
    def snez(self, jidlo):
        print("{}: {} mi chutná!".format(self.jmeno, jidlo))   


class Kotatko(Zviratko):    
    def zamnoukej(self):
        print("{}:Mňau!".format(self.jmeno)) 
        
    #predefinovani funkce z nadtridy
    def snez(self, jidlo):
        print("{} se na {} chvíli zmateně dívá".format(self.jmeno, jidlo))
        #nasledujici zapis se opakuje. Zjednodusime ho volanim funkce super, kterou se dostaneme do nadtridy
        #print("{}: {} mi chutná!".format(self.jmeno, jidlo))   
        super().snez(jidlo)

class Stenatko(Zviratko):
    def zastekej(self):
       print("{}:Haf!".format(self.jmeno))  
  
class Hadatko(Zviratko):
    def __init__(self, jmeno):
        jmeno = jmeno.replace('s', 'sss')
        super().__init__(jmeno)
    
class Blecha(Zviratko):
    def __init__(self):
        super().__init__('Blecha')
    
micka = Kotatko("Micka")
alik = Stenatko("Alík")
standa = Hadatko("stanislav")
standa.snez("myš")
blecha = Blecha()
print(blecha.jmeno)
micka.snez("ryba")
micka.zamnoukej()
alik.snez("kost")
alik.zastekej()
print("-------------")
print(micka.jmeno)
#print(micka.snez)
#metodu lze i prepsat - zde stringem
micka.snez = "aha"
print(micka.snez)