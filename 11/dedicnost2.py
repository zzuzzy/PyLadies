#--*--encoding:1250--*--
'''
Created on 14. 6. 2016

@author: zuzana.kasakova
'''
class Volant:
    pass

class Auto:
    def __init__(self, volant=None):
        if volant == None:
            self.volant = Volant()
        else:
            self.volant = volant

#--------------------------------------------

class Salat:
    # do promenne prisady se vlozi vsechny argumenty zatim nepouzite 
    def __init__(self, *prisady):
        self.prisady = prisady


salat = Salat('mrkev', 'cibule', 'pomeranc')
print(salat.prisady)
salat2 = Salat('okurka', 'cibule', 'olivy', 'syr')
print(salat2.prisady)


#-----------------------------------------------
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
        
zviratka = [Kotatko('Micka'), Stenatko('Rex'), Hadatko('stanislav')]

for zviratko in zviratka:
    zviratko.snez('flákota')