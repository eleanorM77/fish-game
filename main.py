#import pygame
import sys, pygame, random
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

#setting up fish movement
speed = pygame.math.Vector2(0,10)
rotation = random.randint(0,360)
speed.rotate_ip(rotation)
fish_image = pygame.transform.rotate(fish_image, 180-rotation)

#defining move_fish
def move_fish():
  fish_rect.move_ip(speed)

#definining main
def main():
  while True:
    clock.tick(60)
    move_fish()
    screen.fill(color)
    screen.blit(fish_image, fish_rect)
    pygame.display.flip()


#calling main
if __name__ == '__main__':
  main()