import sys, pygame, random

class Fish:
  def __init__(self):
    ##load fish image
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
  global fish_image
  screen_info = pygame.display.Info()
  fish_rect.move_ip(speed)
  if fish_rect.left < 0 or fish_rect.right >       screen_info.current_w:
    speed[0] *= -1
    fish_image = pygame.transform.flip(fish_image, True, False)
    fish_rect.move_ip(speed[0],0)
  if fish_rect.top < 0 or fish_rect.bottom > screen_info.current_h:
    speed[1] *= -1
    fish_image = pygame.transform.flip(fish_image, False, True)
    fish_rect.move_ip(0, speed[1])##