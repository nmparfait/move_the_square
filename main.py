import pygame

#to help to track the time
clock = pygame.time.Clock()

FPS = 30

#the color

blue = (80,184,231)
preto = (0, 0, 0)

#screen settings
screen_height = 700
screen_width = 900
screen = pygame.display.set_mode((screen_width, screen_height))

#getting the screen sizes
square_height = 140
square_width = 140

#draw the square
def draw_square(square_position):
  screen.fill(preto)
  pygame.draw.rect(screen, blue, (square_position[0], square_position[1], square_height, square_width))
  pygame.display.update()

#moving the square
def move_square():
  pygame.init()
  square_position = [250, 300]
  pygame.display.set_caption('move the square')

  ending = False
  while not ending:
    clock.tick(FPS)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        ending = True
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and square_position[1] > 0:
          square_position[1] -= 50

        elif event.key == pygame.K_DOWN and square_position[1] <= screen_height - screen_width:
          square_position[1] += 50
        
        elif event.key == pygame.K_LEFT and square_position[0] >= 0:
          square_position[0] -= 50
        
        elif event.key == pygame.K_RIGHT and square_position[0] <= screen_width - screen_height:
          square_position[0] += 50
      
      draw_square(square_position)

  pygame.quit()


move_square()


    
      



















