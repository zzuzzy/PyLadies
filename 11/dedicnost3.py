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

    def udelej_zvuk(self):
        print("{}: {}!".format(self.jmeno, self.zvuk))  

class Kotatko(Zviratko):    
    zvuk = "Mňau"
        
    #predefinovani funkce z nadtridy
    def snez(self, jidlo):
        print("{} se na {} chvíli zmateně dívá".format(self.jmeno, jidlo))
        #nasledujici zapis se opakuje. Zjednodusime ho volanim funkce super, kterou se dostaneme do nadtridy
        #print("{}: {} mi chutná!".format(self.jmeno, jidlo))   
        super().snez(jidlo)

class Stenatko(Zviratko):
    zvuk = "Haf"
  
class Hadatko(Zviratko):
    def __init__(self, jmeno):
        jmeno = jmeno.replace('s', 'sss')
        super().__init__(jmeno)
        
        
micka = Kotatko("Micka")
rex = Stenatko("Rex")
micka.udelej_zvuk()
rex.udelej_zvuk()