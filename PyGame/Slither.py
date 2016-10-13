__author__ = 'Oskar'

import pygame

pygame.init()

# region Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
# endregion
# region Global Variables
display_width = 800
display_height = 600

lead_x = display_width / 2
lead_y = display_height / 2

lead_x_change = 0
lead_y_change = 0

block_size = 10

frame_rate = 15
# endregion
# region Game Variables
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Slither")

clock = pygame.time.Clock()
# endregion

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -block_size
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = block_size
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -block_size
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = block_size
                lead_x_change = 0

    if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
        gameExit = True

    lead_x += lead_x_change
    lead_y += lead_y_change

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, block_size, block_size])
    pygame.display.update()

    clock.tick(frame_rate)

pygame.quit()
quit()
