"""
Faça um programa que abra e reproduza o áudio de um arquivo mp3
"""

import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
import time
time.sleep(360)

