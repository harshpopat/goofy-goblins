import pygame
pygame.init()

win = pygame.display.set_mode( (500, 480) )

pygame.display.set_caption("you bet!")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

class player(object):
      def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = 5
            self.isjump = False
            self.jumpcount = 10
            self.left = False
            self.right = False
            self.walkcount = 0

      def draw(self,win):
            if self.walkcount + 1 >= 27:
                  self.walkcount = 0

            if self.left:
                  win.blit(walkLeft[self.walkcount//3], (self.x, self.y))
                  self.walkcount +=1
            elif self.right:
                  win.blit(walkRight[self.walkcount//3], (self.x, self.y))
                  self.walkcount +=1
            else:
                  win.blit(char, (self.x, self.y))




def redrawGameWindow():
      win.blit(bg, (0,0,))
      man.draw(win)
      pygame.display.update()

         

#mainloop
man = player(300, 410, 64, 64)
run = True
while run:
      clock.tick(27)

      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run = False

      keys = pygame.key.get_pressed()

      if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
      elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
            man.x += man.vel
            man.right = True
            man.left = False
      else:
            man.right = False
            man.left = False
            man.walkcount = 0
            
      if not(man.isjump):
          if keys[pygame.K_SPACE]:
              man.isjump = True
              man.right = False
              man.left = False
              man.walkcount = 0
        
      else:
          if man.jumpcount >= -10:
              neg = 1
              if man.jumpcount < 0:
                  neg = -1
              man.y -= (man.jumpcount ** 2) * 0.5 * neg
              man.jumpcount -= 1
          else:
                  man.isjump = False
                  man.jumpcount = 10
                  
      redrawGameWindow()

          
      

pygame.quit()
            
