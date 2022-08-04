#import pygame
import sys, pygame
from pygame.locals import *

#initiate pygame
pygame.init()

#set window size
screen_info = pygame.display.info()
size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
