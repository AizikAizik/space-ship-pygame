import pygame
import os

# Width and Height of the game window
WIDTH, HEIGHT = 900, 500

# screen background color
WHITE = (255, 255, 255)

velocity = 5

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# set window title name
pygame.display.set_caption('Space Shooter')

# frame rate per second for the Game
FPS = 60

# spaceship width and height
SPACESHIP_WIDTH = 55
SPACESHIP_HEIGTH = 40

# yellow space ship image
YELLOW_SPACE_SHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png')
)

# scale the image down (yellow spaceship)
YELLOW_SPACE_SHIP = pygame.transform.rotate(
    pygame.transform.scale(
        YELLOW_SPACE_SHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGTH)
    ), 270
)

# red space ship image
RED_SPACE_SHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png')
)

# scale the image down (red spaceship)
RED_SPACE_SHIP = pygame.transform.rotate(
    pygame.transform.scale(
        RED_SPACE_SHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGTH)
    ), 90
)


def draw_window(red, yellow):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACE_SHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACE_SHIP, (red.x, red.y))
    pygame.display.update()


def handle_red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_a]:  # red player moves left
        red.x -= velocity
    if keys_pressed[pygame.K_d]:  # red player moves right
        red.x += velocity
    if keys_pressed[pygame.K_w]:  # red player moves up
        red.y -= velocity
    if keys_pressed[pygame.K_s]:  # red player moves down
        red.y += velocity


def handle_yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT]:  # yellow player moves left
        yellow.x -= velocity
    if keys_pressed[pygame.K_RIGHT]:  # yellow player moves right
        yellow.x += velocity
    if keys_pressed[pygame.K_UP]:  # yellow player moves up
        yellow.y -= velocity
    if keys_pressed[pygame.K_DOWN]:  # yellow player moves down
        yellow.y += velocity


def main():
    red = pygame.Rect(200, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGTH)
    yellow = pygame.Rect(700, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGTH)
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # get all keys listeners
        keys_pressed = pygame.key.get_pressed()

        # check red player movement
        handle_red_movement(keys_pressed, red)

        # check yellow player movement
        handle_yellow_movement(keys_pressed, yellow)

        draw_window(red, yellow)

    pygame.quit()


if __name__ == "__main__":
    main()
