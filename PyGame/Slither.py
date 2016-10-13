__author__ = 'Oskar'
import pygame
import time

# Pygame init
pygame.init()

# region Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
# endregion
# region Game Variables
display_width = 800
display_height = 600
block_size = 10
frame_rate = 15

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Slither")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)
# endregion
# region Game defines


def message_to_screen(msg, colour):
    screen_text = font.render(msg, True, colour)
    gameDisplay.blit(screen_text, [display_width / 2, display_height / 2])


def gameLoop():
    # region Variables
    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0

    game_exit = False
    game_over = False
    # endregion

    while not game_exit:

        while game_over is True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # region Events Main Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
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
        # endregion

        # Screen boundaries
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            game_over = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, block_size, block_size])
        pygame.display.update()

        clock.tick(frame_rate)

    pygame.quit()
    quit()
# endregion

gameLoop()
