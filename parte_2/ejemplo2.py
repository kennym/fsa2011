#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escrito por Daniel Fuentes B.
# Licencia: X11/MIT license http://www.opensource.org/licenses/mit-license.php

# ---------------------------
# Importacion de los módulos
# ---------------------------

import pygame
from pygame.locals import *
import os
import sys

# -----------
# Constantes
# -----------

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
IMG_DIR = "imagenes"

# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------


def load_image(nombre, dir_imagen, alpha=False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(dir_imagen, nombre)
    try:
        image = pygame.image.load(ruta)
    except:
        print "Error, no se puede cargar la imagen: ", ruta
        sys.exit(1)
    # Comprobar si la imagen tiene "canal alpha" (como los png)
    if alpha == True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image


# -----------------------------------------------
# Creamos los sprites (clases) de los objetos del juego:


class Pelota(pygame.sprite.Sprite):
    "La bola y su comportamiento en la pantalla"

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("bola.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.centery = SCREEN_HEIGHT / 2
        self.speed = [3, 3]


# ------------------------------
# Funcion principal del juego
# ------------------------------


def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ejemplo de un Pong Simple")

    # cargamos los objetos
    fondo = load_image("fondo.jpg", IMG_DIR, alpha=False)
    bola = Pelota()

    # el bucle principal del juego
    while True:
        # Actualizamos la pantalla
        screen.blit(fondo, (0, 0))
        # Y mostramos la pantalla
        screen.blit(bola.image, bola.rect)
        pygame.display.flip()

        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()
