import pygame

#Importando las teclas pulsadas
from .teclas import Teclas

#Importando los modelos y la parte visual
from ..models.personaje import Personaje
from ..views.vista import Vista


class Controlador():

    def __init__(self):
        self.ancho = 1266
        self.alto = 688
        self.fps = 20

        self.personaje1 = Personaje("Mincho")
        self.personaje2 = Personaje("Roberth", pos_x = 800)

        self.vista = Vista(self.ancho, self.alto)
        self.lista_de_jugadores = [self.personaje1, self.personaje2]
    
    

    def iniciar_juego(self):
        juego_activo = True
        reloj = pygame.time.Clock()

        while juego_activo:

            #Se indica para salir del juego
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    juego_activo = False


            #Golpear, caso se haya pulsado la tecla
            Teclas.golpear(self.personaje1, self.personaje2)

            #Paperar, caso se haya puslsado la tecla
            Teclas.patear(self.personaje1, self.personaje2)

            #Mover, caso se haya pulsado la tecla
            Teclas.mover(self.personaje1, self.ancho)
            Teclas.mover(self.personaje2, self.ancho, False) #Se envia un false para desactivar player1
            
            

            # Verificar si algún jugador ha sido derrotado
            if not self.personaje1.esta_vivo() or not self.personaje2.esta_vivo():
                self.vista.game_over = True
                print("¡El juego ha terminado!")
                #juego_activo = False


            #Dibujar personajes
            self.vista.dibujar(self.lista_de_jugadores)

            #Reloj del juego
            reloj.tick(self.fps)


        pygame.quit()




#Codigo reciclado

'''#Golpes
teclas = pygame.key.get_pressed() #Tecla presionada
if teclas[pygame.K_a]:  # Golpe del jugador 1
    dano = self.personaje1.golpear(self.personaje2)
    print(f"{self.personaje1.nombre} golpea a {self.personaje2.nombre} causando {dano} de daño.")
                
if teclas[pygame.K_s]:  # Golpe del jugador 2
    dano = self.personaje2.golpear(self.personaje1)
    print(f"{self.personaje2.nombre} golpea a {self.personaje1.nombre} causando {dano} de daño.")'''