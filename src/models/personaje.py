import pygame
import random

class Personaje():

    def __init__(self, nombre, vida = 500, pos_x = 0, pos_y = 241, sprite = "normal"):
        self.nombre = nombre
        self.vida = vida
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hitbox = pygame.Rect((self.pos_x, self.pos_y, 280, 180)) #Generando el cuadrado de colisiones
        self.sprite = sprite


    def mover(self, mov_x, ancho = True, player_1 = True):
        self.pos_x += mov_x
        self.hitbox.x = self.pos_x

        
    def golpear(self, otro):
        self.sprite = "golpe"
        dano = random.randint(5, 20)
        otro.vida -= dano
        return dano

    def patear(self, otro):
        self.sprite = "patada"
        dano = random.randint(5, 20)
        otro.vida -= dano
        return dano

    def ataque_especial(self, otro):
        dano = random.randit(20, 40)
        otro.vida -= dano
        return dano


    def esta_vivo(self):
        return self.vida >= 0 




#Codigo reciclado

'''velocidad = 10
        mov_x = 0
        mov_y = 0

        #Moviminetos
        teclas = pygame.key.get_pressed()
        if player_1:
            if teclas[pygame.K_m]:  # mover jugador jugador 1 hacia enfrente
                mov_x = velocidad
                print(f"{self.nombre} se mueve hacia entrente")

            if teclas[pygame.K_n]:  # mover jugador jugador 1 hacia atras
                mov_x -= velocidad
                print(f"{self.nombre} se mueve hacia atras")
        else:   
            if teclas[pygame.K_RIGHT]:  # mover jugador jugador 1 hacia enfrente
                mov_x = velocidad
                print(f"{self.nombre} se mueve hacia entrente")

            if teclas[pygame.K_LEFT]:  # mover jugador jugador 1 hacia atras
                mov_x -= velocidad
                print(f"{self.nombre} se mueve hacia atras")

        #Actualizar movimientos
        self.pos_x += mov_x #Actualizar posicion x
        self.hitbox.x = self.pos_x #Actualizar hitbox
        if player_1 == False:
            self.hitbox.x = self.pos_x + 80 #Actualizar hitbox

        self.pos_y -= mov_y #Actualizar posicion y
        self.hitbox.y = self.pos_y #Actualizar hitbox
        

        #Siempre en pantalla
        if player_1:
            if self.hitbox.left + mov_x < 0:
                self.pos_x = 0
            
            if self.hitbox.right + mov_x > ancho:
                self.pos_x = ancho - self.hitbox.width

        else:
            if self.hitbox.left + mov_x < 0:
                self.pos_x = 0 -80
            
            if self.hitbox.right + mov_x > ancho:
                self.pos_x = ancho - self.hitbox.width - 80'''