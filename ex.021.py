# PROGRAMA INSERINDO SOM #

import pygame
pygame.init()
pygame.mixer.music.load('vingtema.mp3')
pygame.mixer.music.play()
pygame.event.wait()
