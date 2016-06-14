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
from pyglet.window import key

#DEFINICE KONSTANT
NADPIS_y = 15
SIRKA = 800
VYSKA = 600
DELKA_PALKY = 150
PULICI_CARA_x = 100
PULICI_CARA_y = 50

'''
micek
        |----+
        |    |
        +----|
        
    levy dolni roh - [x1,y1]
    pravy horni roh - [x2, y2]
'''   
micek = [SIRKA//2 - 10, VYSKA//2 - 10, SIRKA//2 + 10,VYSKA//2 + 10]
smer = [0, 0]
rychlost = 1/80


#palka = [x1, y1, x2, y2]
palka1 = [0, VYSKA // 2 - DELKA_PALKY/2, 5, VYSKA //2 + DELKA_PALKY/2]
palka2 = [SIRKA - 5, VYSKA // 2 - DELKA_PALKY/2, SIRKA, VYSKA //2 + DELKA_PALKY/2]
skore = [0,0]
stisknute_klavesy = list()

#DEFINICE FUNKCI




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
    
    #palky
    
    nakresli_obdelnik(*palka1, mode = gl.GL_QUADS)
    nakresli_obdelnik(*palka2, mode = gl.GL_QUADS)
    #nazev hry
    label = pyglet.text.Label("Hra PONG",
                              font_size = NADPIS_y,
                              x = window.width, y = window.height - NADPIS_y,
                              anchor_x = 'right')
    label.draw()   
    
    #vykresleni micku
    #vykresleni palek
    #nastaveni pocatecniho skore, zobrazeni skor   
    vypis_skore()
    
def vypis_skore():
    
    label1 = pyglet.text.Label(str(skore[0]),
                              font_size = NADPIS_y,
                              x = SIRKA//2 - 50 , y = VYSKA - NADPIS_y,
                              anchor_x = 'left')
    label2 = pyglet.text.Label(str(skore[1]),
                              font_size = NADPIS_y,
                              x = SIRKA//2 + 50 , y = VYSKA - NADPIS_y,
                              anchor_x = 'right')
    label1.draw() 
    label2.draw() 
    
def posun_micek():
    
    
    nova_pozice = list()
    nova_pozice.append(micek[0] + smer[0])
    nova_pozice.append(micek[1] + smer[1])
    nova_pozice.append(micek[2] + smer[0])
    nova_pozice.append(micek[3] + smer[1])
    
    
    #kontrola narazu mimo palku - bod pro druheho hrace 
    if (nova_pozice[0] <= 5) and ((nova_pozice[3] < palka1[1]) or (nova_pozice[1] > palka1[3])):
        #reset hry, uprava skore
        print("zasah -  hrac 2")
        skore[1] += 1
        reset()
        return        
        
    elif (nova_pozice[2] >= SIRKA -5) and ((nova_pozice[3] < palka2[1]) or (nova_pozice[1] > palka2[3])): 
        print("zasah -  hrac 2")       
        skore[0] += 1
        reset()
        return
    
    #kontrola odrazu od horniho a dolniho okraje    
    #horni okraj - pozice Y1 nebo Y2, tj. 4.index
    if (nova_pozice[1] < 0) or (nova_pozice[3] > VYSKA):
        #naraz nahore, y2 prekrocilo mez
        smer[1] = -smer[1]        
            
    #kontrola narazu na palku
    if (nova_pozice[0] < 0) or (nova_pozice[2] > SIRKA):
        smer[0] = -smer[0]
         
       
    
    micek[0] += smer[0]
    micek[1] += smer[1]
    micek[2] += smer[0]
    micek[3] += smer[1]


def posun_palku(palka, smer):
    
    nova_pozice = list()
    nova_pozice.append(palka[1]+ smer)
    nova_pozice.append(palka[3]+ smer)
    
    if (nova_pozice[0] <= 0) or (nova_pozice[1] >= VYSKA):
        return
    
    palka[1] = palka[1] + smer
    palka[3] = palka[3] + smer
 

       
def reset():
    micek[0] = SIRKA//2 - 10
    micek[1] = VYSKA//2 - 10
    micek[2] = SIRKA//2 + 10
    micek[3] = VYSKA//2 + 10    
    smer[0] = randrange(1,5)
    smer[1] = randrange(-5,5)
    
def stisk_klavesy(symbol, modifiers):
    if symbol == key.W:
        #posun palky1 nahoru
        stisknute_klavesy.append((palka1, 'nahoru'))
        
    elif symbol == key.S:
        #posun palky1 dolu
        stisknute_klavesy.append((palka1, 'dolu'))
            
    elif symbol == key.UP:
        stisknute_klavesy.append((palka2, 'nahoru'))     
            
    elif symbol == key.DOWN:
        stisknute_klavesy.append((palka2, 'dolu'))
        
        
def pusteni_klavesy(symbol, modifiers):
    if symbol == key.W:
        #posun palky1 nahoru
        stisknute_klavesy.remove((palka1, 'nahoru'))
        
    elif symbol == key.S:
        #posun palky1 dolu
        stisknute_klavesy.remove((palka1, 'dolu'))
            
    elif symbol == key.UP:
        stisknute_klavesy.remove((palka2, 'nahoru'))     
            
    elif symbol == key.DOWN:
        stisknute_klavesy.remove((palka2, 'dolu')) 
        
def prekresli_stav(t):
    posun_micek()
    vypis_skore()
    
    if (palka1, 'nahoru') in stisknute_klavesy:
        posun_palku(palka1, 5)
    if (palka1, 'dolu') in stisknute_klavesy:
        posun_palku(palka1, -5)
    if (palka2, 'nahoru') in stisknute_klavesy:
        posun_palku(palka2, 5)
    if (palka2, 'dolu') in stisknute_klavesy:
        posun_palku(palka2, -5)
    
#INICIALIZACE HRY

reset()

#inicializace okna
window = pyglet.window.Window(width = SIRKA, height = VYSKA)

#registrace handleru
window.push_handlers(on_draw = vykresli,
                     on_key_press = stisk_klavesy,
                     on_key_release = pusteni_klavesy)


#SPUSTENI HRY

#pohyb micku
    
pyglet.clock.schedule_interval(prekresli_stav, rychlost)

pyglet.app.run()
