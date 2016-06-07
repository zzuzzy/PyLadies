#--*--encoding:1250--*--
'''
Created on 7. 6. 2016

@author: zuzana.kasakova
'''


import pyglet
from math import sin

def tik(t):
    had.x -= t*20
    had.y +=  5* sin(had.x/5)
    
   
    
def zpracuj_text(text):
    had.x = 500
    
    
window = pyglet.window.Window()
window.clear()

#naplanovani udalosti - kazdou 1/30 sekundy se zavola funkce tik. funkce schedule_interval je predavan automaticky parametr cas od posledniho volani funkce tik.

pyglet.clock.schedule_interval(tik, 1/30)

def zmen(t):
    had.image = obr2
    pyglet.clock.schedule_once(zmen_zpet, 0.5)
   
def zmen_zpet(t): 
    had.image = obr1
    pyglet.clock.schedule_once(zmen, 0.5)


pyglet.clock.schedule_once(zmen, 1)

#obrazek - nacteni a prevod obrazku na objekt, ktery predstavuje 2D obrazek

obrazek = pyglet.image.load('ninja01.png')
obr1 = pyglet.image.load('had.png')
obr2 = pyglet.image.load('had2.png')


ninja = pyglet.sprite.Sprite(obrazek)
had = pyglet.sprite.Sprite(obr1)
had.x = 500
had.y = 20


def vykresli():
    window.clear()
   # ninja.draw()
    had.draw()
 
def klik(x, y, tlacitko, mod):
    
    had.x = x
    had.y = y


    
      
  
  #zaregistrovani udalosti - udalosti priradim funkci - pouze jeji nazev, nevolam tu funkci
 
  #udalost psani na klavesnici se jmenuje "on_text" - pri stisku klavesy se vola funkce zpracuj_text s parametrem nazev dane klavesy
 #udalost on_draw
window.push_handlers(                         
                       on_text=zpracuj_text,
                       on_draw = vykresli,
                       on_mouse_press = klik
                       )
  
  
  
  
   #Knihovna pyglet - zabudovaný Event Loop - čekání na vstup uživatele - pyglet.app.run()

pyglet.app.run()
  
print("Konec")



 