import pygame
import os

# Width and Height of the game window
WIDTH, HEIGHT = 900, 500

# screen background color
WHITE = (255, 255, 255)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# set window title name
pygame.display.set_caption('Space Shooter')

# frame rate per second for the Game
FPS = 60

# yellow space ship image
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))

# red space ship image
RED_SPACE_SHIP = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))


def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
