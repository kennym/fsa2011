#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escrito por Daniel Fuentes B.
# Modificado por Kenny Meyer
# Licencia: X11/MIT license http://www.opensource.org/licenses/mit-license.php

# ---------------------------
# Importacion de los módulos
# ---------------------------

import pygame
from pygame.locals import *

# -----------
# Constantes
# -----------

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------


# ------------------------------
# Funcion principal del juego
# ------------------------------


def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("tutorial pygame parte 1")


if __name__ == "__main__":
    main()
