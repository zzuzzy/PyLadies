'''
Created on 14. 6. 2016

@author: zuzana.kasakova
'''

type("abc") == str  # vrati True

str.lower("XYZ")  #vrati xyz

class Kotatko:
    #vzdy musi byt prvni argument metody samotny objekt odkazovany klicovym slovem self
    def zamnoukej(self):
        print("Mnau!")

       
kote= Kotatko()
#Python umoznuje pridavat nove atributy, aniz by predem byly definovane predem v tride
kote.jmeno = "Micka"
kote1 = Kotatko()

#ekvivalentni zapisy
kote.zamnoukej()
Kotatko.zamnoukej(kote)
