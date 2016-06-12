#--*--encoding:1250 --*--
'''
Created on 12. 6. 2016

@author: zzuzzy

Graficka hra pro dva hrace. Kazdy hrac ovlada "palku" na sve strane hriste,
a snazi se odpalit micek na protivnikovu stranu.

Ovladani:
Hrac 1: klavesy W a S
Hrac 2: sipky Nahoru a Dolu
Konec: Esc


Hra pouziva gravickou knihovnu Pyglet, coz je Pythonova nadstavba nad OpenGL.

Souradny system okynka je nasledujici::

        y ^
          |
    VYSKA +---------------------------------------+
          |                   :                   |
          |                   :                   |
          |                   :                   |
          |                   ;     []            |
          |]                  ;                  [|
          |]                  ;                  [|
          |]                  ;                  [|
          |]                  ;                  [|
          |                   ;                   |
          |                   :                   |
          |                   ;                   |
          |                   ;                   |
        0 +---------------------------------------+------> x
          :                   :                   :
          0               SIRKA/2               SIRKA

   1. Hrací pole ve tvaru obdélníku s půlící čárou.
   2. Míček létající určitou rychlostí po hracím poli.
   3. Dvě pálky pohybující se vertikálně na krajích pole.
   4. Dvě počítadla skóre.

'''
import pyglet
from pyglet import gl
from random import randrange

#DEFINICE KONSTANT
NADPIS_y = 15
SIRKA = 800
VYSKA = 600

micek = [SIRKA//2 - 10, VYSKA//2 - 10, SIRKA//2 + 10,VYSKA//2 + 10]
rychlost = [0, 0]

#DEFINICE FUNKCI
PULICI_CARA_x = 100
PULICI_CARA_y = 50



def nakresli_obdelnik(x1, y1, x2, y2, mode):
    '''
    x--------x
    |        |
    |        |
    x--------x
    
    (x1, y1) - levy dolni roh
    (x2, y2) - pravy hordni roh
    '''    
    
    
   # gl.glBegin(gl.GL_LINE_STRIP)
    gl.glBegin(mode)
    gl.glVertex2f(x1, y1)
    gl.glVertex2f(x2, y1)
    gl.glVertex2f(x2, y2)
    gl.glVertex2f(x1, y2)
    gl.glVertex2f(x1, y1)       
    gl.glEnd() 
    
def nakresli_caru(x1, y1, x2, y2):
   
    gl.glBegin(gl.GL_LINES)
    #  gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glVertex2f(x1, y1)
    gl.glVertex2f(x2, y2)   
    gl.glEnd()
    

def vykresli():
     #Vykresleni hraciho pole
    
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    nakresli_obdelnik(0, 0, SIRKA, VYSKA, mode = gl.GL_LINE_STRIP)
    
    #vykresleni pulici cary   
    
    nakresli_caru(SIRKA//2, 0, SIRKA//2, VYSKA)
    
    #micek
       
    nakresli_obdelnik(*micek, mode = gl.GL_QUADS)
    #nazev hry
    label = pyglet.text.Label("Hra PONG",
                              font_size = NADPIS_y,
                              x = window.width, y = window.height - NADPIS_y,
                              anchor_x = 'right')
    label.draw()   
    
    #vykresleni micku
    #vykresleni palek
    #nastaveni pocatecniho skore, zobrazeni skore
    
def posun(t):
    
    #posun micku
    rychlost_x = rychlost[0]
    rychlost_y = rychlost[1]
    
    #kontrola odrazu od horniho a dolniho okraje    
    
    #kontrola narazu na palku
    
    #kontrola narazu mimo palku - bod pro druheho hrace 
    
    micek[0] += rychlost_x
    micek[1] += rychlost_y
    micek[2] += rychlost_x
    micek[3] += rychlost_y


def set_rychlost():
    rychlost[0] = randrange(1,5)
    rychlost[1] = randrange(0,5)
    
  
#INICIALIZACE HRY


#inicializace okna
window = pyglet.window.Window(width = SIRKA, height = VYSKA)

#registrace handleru
window.push_handlers(on_draw = vykresli)


#SPUSTENI HRY

#dokud se nezmeni skore opakuje se nasledujici

    
#nastaveni nove rychlosti micku
set_rychlost()
#pohyb micku
    
pyglet.clock.schedule_interval(posun, 1/30)
    
#reakce na narazy micku na okraj pole

#reakce na naraz micku na palku - navyseni pocitadla, micek se spousti znovu ze stredu

#pohyb palek - reakce na stisky klaves


pyglet.app.run()
