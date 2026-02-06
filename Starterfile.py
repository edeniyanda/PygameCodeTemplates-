import pygame


pygame.init()


# GAME CONFIGURATIONS 
GAME_NAME = "Moving Dodge Around"
WIDTH = 700
HEIGHT = 600
FPS = 60


screen = pygame.display.set_mode((WIDTH, HEIGHT))
caption = pygame.display.set_caption(GAME_NAME)
clock = pygame.time.Clock()

# Game Stylings and Designs 
BG_COLOUR = (15, 15, 25)


# Fate Variable
running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

    screen.fill(BG_COLOUR)

    pygame.display.flip()




pygame.quit()
