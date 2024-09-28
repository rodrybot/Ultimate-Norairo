import pygame

#Importar los colores previamente definidos
from .color import Color
#Importar los Sprites
from .sprite import Sprite, Fondo

class Vista():

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

        pygame.init()
        self.pantalla = pygame.display.set_mode((ancho, alto)) #superficie
        pygame.display.set_caption("Ultimate Ñorairo")

        self.game_over = False

    @classmethod
    def cambiar_sprite(cls, personaje):
        nombre_sprite = personaje.nombre.lower()
        estado_sprite = personaje.sprite.lower()
        sprite = getattr(Sprite, f'{nombre_sprite}_{estado_sprite}')
        return sprite


    def gameover(self, personaje, pantalla):
        fuente = pygame.font.Font(None, 74)
        mensaje = f"Juego terminado! El ganador es: {personaje.nombre}"
        texto = fuente.render(mensaje, True, Color.blanco)
        texto_rect = texto.get_rect(center=(self.ancho // 2, self.alto // 2))
        pygame.draw.rect(pantalla, Color.negro, (111 , 200, 1050, 300))  # Fondo del mensaje
        pygame.draw.rect(pantalla, Color.rojo, (111, 200, 1050, 300), 2)
        pantalla.blit(texto, texto_rect)



    def dibujar(self, personajes): #personajes tiene que ser un a lista
        self.pantalla.fill(Color.negro)
        self.pantalla.blit(Fondo.linea, (0, 0))

        for personaje in personajes:

            if personaje.nombre == "Mincho":
                sprite = Vista.cambiar_sprite(personaje)
                self.pantalla.blit(sprite, (personaje.pos_x, personaje.pos_y))#Se dibuja al sprite
            else:
                sprite = Vista.cambiar_sprite(personaje)
                self.pantalla.blit(pygame.transform.flip(sprite, True, False), (personaje.pos_x, personaje.pos_y))#Se dibuja el Sprite y ademas se invierte en modo espejo
                

            # Mostrar salud
            font = pygame.font.Font(None, 36)# Fuente, predeterminada, tamaño
            texto = font.render(f"Luchador: {personaje.nombre}       Vida: {personaje.vida}", True, Color.blanco)# True para suavizar, Color
            self.pantalla.blit(texto, (100 if personaje.nombre == "Mincho" else 800, 30))# lo que se deas mostrar (x, y)


        if self.game_over:
            print('holaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

            if personajes[0].vida < 0:
                self.gameover(personajes[1], self.pantalla)
            else:
                self.gameover(personajes[0], self.pantalla)


            #dibujar hitbox
            #pygame.draw.rect(self.pantalla, Color.blanco, personaje.hitbox),   #Descomentar par dibujar

        pygame.display.flip()



#Codigo recilado

'''
    if personaje.nombre == "Roberth":
    cambiar = personaje.hitbox.x = 880

        #sprite_rec = sprite.get_rect()

color = (Color.rojo) if personaje.nombre == "Mincho" else (Color.azul) #Definiendo el Color
pygame.draw.rect(self.pantalla, color, (100 if personaje.nombre == "Mincho" else 1100, 400, 50, 50))  # superficie, color, posicion -> (x, y, ancho, alto), borde opcional

pygame.transform.flip(imagen, True, False)  # (imagen, Verticalmente, horizontalmente) invertir'''