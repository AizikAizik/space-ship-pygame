import pygame
import os
pygame.font.init()
pygame.mixer.init()

# set game text font for health
HEALTH_FONT = pygame.font.SysFont('Juice ITC', 45)

# set game winner display font
WINNER_FONT = pygame.font.SysFont('Juice ITC', 55)

# Width and Height of the game window
WIDTH, HEIGHT = 900, 500

# screen background color
WHITE = (255, 255, 255)

# border seperator color
BLACK = (0, 0, 0)

# yellow bullet color
YELLOW = (255, 255, 0)

# red bullet color
RED = (255, 0, 0)

velocity = 5

# bullet speed
BULLET_VEL = 10

# maximum number of bullets for each character
MAX_BULLETS = 3

WIN = pygame.display.set_mode((WIDTH, HEIGHT))


# create 2 custom user events
RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2

# set window title name
pygame.display.set_caption('Space Shooter')

# frame rate per second for the Game
FPS = 60

# Bullet sounds
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))

# Game Seperator border
BORDER = pygame.Rect((WIDTH // 2) - 5, 0, 10, HEIGHT)

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

# space background image
SPACE_BG = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT)
)


def draw_winner(text):
    pygame.font.init()
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH //2 - draw_text.get_width() //2, HEIGHT //2 - draw_text.get_height()//2))

    pygame.display.update()
    pygame.time.delay(4000)


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE_BG, (0,0))

    pygame.draw.rect(WIN, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render('Live(s): ' + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render('Live(s): ' + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (10, 10))
    WIN.blit(yellow_health_text, (WIDTH - yellow_health_text.get_width() - 10, 10))

    WIN.blit(YELLOW_SPACE_SHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACE_SHIP, (red.x, red.y))

    # draw red bullets on screen
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

     # draw yellow bullets on screen
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    
    pygame.display.update()


def handle_red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_a] and red.x - velocity > 0:  # red player moves left
        red.x -= velocity
    if keys_pressed[pygame.K_d] and (red.x + velocity + red.width) < BORDER.x + BORDER.width:  # red player moves right
        red.x += velocity
    if keys_pressed[pygame.K_w] and red.y - velocity > 0:  # red player moves up
        red.y -= velocity
    if keys_pressed[pygame.K_s] and (red.y + velocity + red.height) < HEIGHT -15:  # red player moves down
        red.y += velocity


def handle_yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and (yellow.x - velocity) > BORDER.x + BORDER.width:  # yellow player moves left
        yellow.x -= velocity
    if keys_pressed[pygame.K_RIGHT] and yellow.x + velocity + yellow.width < WIDTH:  # yellow player moves right
        yellow.x += velocity
    if keys_pressed[pygame.K_UP] and yellow.y - velocity > 0:  # yellow player moves up
        yellow.y -= velocity
    if keys_pressed[pygame.K_DOWN] and (yellow.y + velocity + yellow.height) < HEIGHT -15:  # yellow player moves down
        yellow.y += velocity


def handle_bullets(red_bullet, yellow_bullet, red, yellow):
    # loop through red bullets to check for collisions
    for bullet in red_bullet:
        bullet.x += BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullet.remove(bullet)
        elif bullet.x > WIDTH:
            red_bullet.remove(bullet)

     # loop through yellow bullets to check for collisions
    for bullet in yellow_bullet:
        bullet.x -= BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullet.remove(bullet)
        elif bullet.x < 0:
            yellow_bullet.remove(bullet)


def main():
    red = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGTH)
    yellow = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGTH)

    # store number of bullets for both players
    red_bullets = []
    yellow_bullets = []

    # no of lives for red player
    red_health = 10

    # no of lives for yellow player
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect((red.x + red.width), (red.y + red.height // 2 - 2), 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x, (yellow.y + yellow.height // 2 - 2), 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        winner_text = ""

        if red_health <= 0:
            winner_text = "Yellow spaceship won!"

        if yellow_health <= 0:
            winner_text = "Red spaceship won!"

        # keep checking if there is a winner
        if winner_text != "":
            draw_winner(winner_text)
            break


        # get all keys listeners
        keys_pressed = pygame.key.get_pressed()

        # check red player movement
        handle_red_movement(keys_pressed, red)

        # check yellow player movement
        handle_yellow_movement(keys_pressed, yellow)

        # draw both bullets on screen if bullet event is fired
        handle_bullets(red_bullets,yellow_bullets, red, yellow)

        # draw the main game window
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    main()


if __name__ == "__main__":
    main()
