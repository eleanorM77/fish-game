#import pygame
import sys, pygame, random
from pygame.locals import *
from fish.py import *

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

#definining main
def main():
  while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
    move_fish()
    screen.fill(color)
    screen.blit(fish_image, fish_rect)
    pygame.display.flip()


#calling main
if __name__ == '__main__':
  main()