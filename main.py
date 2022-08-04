#import pygame
import sys, pygame
from pygame.locals import *

#initiate pygame
pygame.init()

#set window size
screen_info = pygame.display.Info()
size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)

#setting up clock
clock = pygame.time.Clock()

#set up color
color = (0,127,255)

#load fish image
fish_image = pygame.image.load("fish.png")
fish_image = pygame.transform.smoothscale(fish_image,(80,80))
fish_rect = fish_image.get_rect()

#definining main
def main():
  clock.tick(60)
  screen.fill(color)
  pygame.display.flip()


#calling main
if __name__ == '__main__':
  main()