import pygame
from ..views.vista import Vista


class Teclas():

    @classmethod
    def golpear(cls, personaje1,  personaje2):
        personaje1.sprite = "normal" #para que vuelva a la normalidad, despues de golpear
        personaje2.sprite = "normal"

        #Golpes
        teclas = pygame.key.get_pressed() #Tecla presionada
        if teclas[pygame.K_a]:  # Golpe del jugador 1
            dano = personaje1.golpear(personaje2)
            print(f"{personaje1.nombre} golpea a {personaje2.nombre} causando {dano} de daño.")
        if teclas[pygame.K_s]:  # Golpe del jugador 2
            dano = personaje2.golpear(personaje1)
            print(f"{personaje2.nombre} golpea a {personaje1.nombre} causando {dano} de daño.")
    
    @classmethod
    def patear(cls, personaje1,  personaje2):
        #personaje1.sprite = "normal" #para que vuelva a la normalidad, despues de golpear
        #personaje2.sprite = "normal"

        #Patadas
        teclas = pygame.key.get_pressed() #Tecla presionada
        if teclas[pygame.K_q]:  # Golpe del jugador 1
            dano = personaje1.patear(personaje2)
            print(f"{personaje1.nombre} patea a {personaje2.nombre} causando {dano} de daño.")
        if teclas[pygame.K_w]:  # Golpe del jugador 2
            dano = personaje2.patear(personaje1)
            print(f"{personaje2.nombre} patea a {personaje1.nombre} causando {dano} de daño.")

    @classmethod
    def mover(cls, personaje, ancho, player_1 = True):
        velocidad = 10
        mov_x = 0

        #movimientos
        teclas = pygame.key.get_pressed()
        if player_1:
            if teclas[pygame.K_m]:  # Mover hacia adelante
                mov_x = velocidad
                print(f"{personaje.nombre} se mueve hacia adelante")
            elif teclas[pygame.K_n]:  # Mover hacia atrás
                mov_x = -velocidad
                print(f"{personaje.nombre} se mueve hacia atrás")
        else:
            if teclas[pygame.K_RIGHT]:  # mover jugador jugador 1 hacia enfrente
                mov_x = velocidad
                print(f"{personaje.nombre} se mueve hacia entrente")
            if teclas[pygame.K_LEFT]:  # mover jugador jugador 1 hacia atras
                mov_x -= velocidad
                print(f"{personaje.nombre} se mueve hacia atras")

        # Actualizar el movimiento del personaje
        personaje.mover(mov_x)

        # Limitar el movimiento dentro de la pantalla
        if player_1:

            if personaje.hitbox.left < 0:
                personaje.pos_x = 0
            if personaje.hitbox.right > ancho:
                personaje.pos_x = ancho - personaje.hitbox.width

        else:

            if personaje.hitbox.left + mov_x < 0:
                personaje.pos_x = 0
            
            if personaje.hitbox.right + mov_x > ancho:
                personaje.pos_x = ancho - personaje.hitbox.width
