import pygame
import random

#inizialiazziamo pygame
pygame.init()

#setto le immagini di gioco
sfondo = pygame.image.load("sfondo.png")
uccello = pygame.image.load("uccello.png")
base = pygame.image.load("base.png")
gameover = pygame.image.load("gameover.png")
tubogiu = pygame.image.load("tubo.png")
#la fuznione flip prende l'immagine da specchiare, il flip orizzontale e il terzo verticale
tubosu = pygame.transform.flip(tubogiu,False,True)

#faccio vedere lo schermo e ci setto la grandezza
schermo =  pygame.display.set_mode((288,512))
FPS = 60

#poszione dello schermo
basex = 0
#velocita di avanzamento
velocitaAvanzata = 3

def inizializza():
    # rispetivamente posizione verticale, orrizontale e velocita
    global uccellox,uccelloy,uccello_vel
    global tubi
    uccellox = 30
    uccelloy = 150
    uccello_vel = 0
    tubi = []#quando creo la cose iniziali genero una lista di tubi
    tubi.append(tubiClass())#e ne aggiungo uno

def disegnaOggetti():
    schermo.blit(sfondo, (0,0))#disegna l'immagine safondo alla poszione 0 0
    for t in tubi:#e quando ridisegno gli oggetti avanzo con il tubo
        t.avanzaDisegna()
    schermo.blit(uccello, (uccellox,uccelloy))#disegna immagine pennuto alla poszione x e y
    schermo.blit(base, (basex,400))

#aggiorniamo lo schermo passo passo
def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)##aggiorniamo gli fps

#funzione se si tocca il terreno
#se schiaccio barra spazziatrice ricomincia il gioco
def haiPerso():
    schermo.blit(gameover, (50,180))#metto a schermo il game over
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():  # con questa funzione posso leggere gli eventi che si verificano
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # se premo un tasto e uil tasto barra spazziatrice
                inizializza()
                ricominciamo = True
            if event.type == pygame.QUIT:  # se clicco sulla XC per chiudere il gioco
                pygame.quit()

#classe tubi, ovvero una classe che chiamero per ogni tubo
class tubiClass:#self e il tubo stesso su qui viene chiamamto il o i metodi
    def __init__(self):#funzione che viene lanciata ogni volta che creo un tubo
        self.x = 300#setto posizione in altezza
        self.y = random.randint(-70,150)#setto posizione cqasuale in largezza

    def avanzaDisegna(self):#funzione che posso che crea i tubi su e giu
        self.x -= velocitaAvanzata #avvicina i tubi
        schermo.blit(tubogiu,(self.x,self.y+210))#posizione il tubo gi in larghezza x e altezza +210
        schermo.blit(tubogiu,(self.x,self.y-210))#posizione il tubo su in larghezza x e altezza -210

    def collissione(self,uccello,uccellox,uccelloy):#funzion che serve per gestire lo sschianto del pennutto contro i tubi
        tolleranza  = 5 #tolleranza per le collissioni
        # per il lato destro del piccione prendo la posizione orrizzontale sommata alla larghezza dell'immagine e sotriamo la tolleranza
        uccelloLatoDx = uccellox + uccello.get_width()-tolleranza #get_width server per prendere la grandezza dell'immagine
        #lato sinistro del piccione = posizione x piu tolleranza
        uccelloLatoSx = uccellox + tolleranza
        tubiLatoDx = self.x + tubogiu.get_width()
        tubiLatoSx = self.x
        uccelloLatoGiu = uccelloy+tolleranza
        uccelloLatoSu = uccelloy + uccello.get_width() - tolleranza
        tubiLatoSu = self.y + 110
        tubiLatoGiu = self.y - 210
        #if uccelloLatoDx > tubiLatoSx and uccelloLatoSx < tubiLatoDx:
        #   if()

inizializza()

while(True):
    #la base scorre
    basex -= velocitaAvanzata
    if basex < -45:  # se l'immagine della base e alla fine la ricreo
        basex = 0
    #gravita
    uccello_vel += 1 #fara cadere il pennuto piu velocemente
    uccelloy += uccello_vel  #prendiamo la posizione verticale e gli sommiamo la velocita (cade piu in fretta)
    #eventi
    for event in pygame.event.get():#con questa funzione posso leggere gli eventi che si verificano
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:#se premo un tasto e uil tasto e freccettia su
            uccello_vel = -10
        if event.type == pygame.QUIT:#se clicco sulla XC per chiudere il gioco
            pygame.quit()
    if tubi[-1].x < 150:
        tubi.append(tubiClass())
    if uccelloy > 385:#se tocca il terreno
        haiPerso()
    #aggiorna schermo
    disegnaOggetti()
    aggiorna()