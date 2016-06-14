#--*--encoding:1250--*--
'''
Created on 14. 6. 2016

@author: zuzana.kasakova
'''

#class Kotatko:
#    
#    def zamnoukej(self):
#        print("{}:Mňau".format(self.jmeno))
#        
#        
#micka = Kotatko()
#micka.jmeno = "Micka"
#
#mourek = Kotatko()
#mourek.jmeno = "Mourek"
#
#micka.zamnoukej()
#mourek.zamnoukej()


class Kotatko:
    def __init__(self, jmeno):
        self.jmeno = jmeno
    
    # predefinuji funkci str, ktera je definovana na jakykoliv objekt    
    def __str__(self):
        #srovnej s print(type("abc")
        return("<Kotatko se jmenem: {}>".format(self.jmeno))
    
    #nadefinuji funkci __len__, ta ale neni automaticky definovana na kazdem objektu
    def __len__(self):
        return 1  
        
    def zamnoukej(self):
        print("{}:Mňau".format(self.jmeno)) 
        
    def snez(self, jidlo):
        print("{}: {} mi chutná!".format(self.jmeno, jidlo))
        
        
micka = Kotatko("Micka")

mourek = Kotatko(jmeno = "Mourek")

micka.zamnoukej()
mourek.zamnoukej()

micka.jmeno = "Micinka"
micka.zamnoukej()

#Vzdy, kdyz neco tisknu, musi se nejprve prevest parametr printu na string, na coz se vzdy pouzije metoda str()
print(micka)
print(micka.__str__())
print(str(micka))

print("{} {}".format(micka, mourek))

print(len(micka))

micka.snez("ryba")


