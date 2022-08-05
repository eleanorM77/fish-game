import sys, pygame, random

class Fish:
  def __init__(self, pos):
    self.image = pygame.image.load("fish.png")
    scale = random.randint(1,5)*10
    self.image = pygame.transform.smoothscale(fish_image,(scale,scale))
    self.rect = fish_image.get_rect()
    self.rect.center = pos
    
    self.speed = pygame.math.Vector2(0,random.randint(2,5))
    speed = pygame.math.Vector2(0,10)
    rotation = random.randint(0,360)
    speed.rotate_ip(rotation)
    fish_image = pygame.transform.rotate(fish_image, 180-rotation)
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
    











#defining move_fish
