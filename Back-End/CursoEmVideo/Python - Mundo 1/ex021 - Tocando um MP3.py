# Faça u programa em Pyhton que abra e reproduza o áudio de
# um arquivo mp3

import pygame as pgm

pgm.init()

pgm.mixer.music.load('ex021.p3')
pgm.mixer.music.play()

pgm.event.wait()