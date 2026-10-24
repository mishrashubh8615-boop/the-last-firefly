import pygame
import random
import math

# background = pygame.image.load("playful-forest-sprites-leaving-trails-laughter-mischief-their-wake-generative-ai-realm-fantasy-bring-joy-to-293729757.webp").convert()
pygame.init()


screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Little Guy: The Last Firefly")

pygame.init()

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

player_x = 300
player_y = 200
player_direction = "right"

firefly_x = 100
firefly_y = 50.0

firefly_start_y = firefly_y
firefly_direction = 1

health = 3
score = 0
firefly_collected = False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            if score >= 5:
               score = 0
               firefly_collected = False
               firefly_x = random.randint(30, 740)
               firefly_y = random.randint(30, 540)
               firefly_start_y = firefly_y
               firefly_direction = 1

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= 1
        player_direction = "left"

    if keys[pygame.K_RIGHT]:
        player_x += 1
        player_direction = "right"

    if keys[pygame.K_UP]:
        player_y -= 1
        player_direction = "up"

    if keys[pygame.K_DOWN]:
        player_y += 1
        player_direction = "down"


    if player_x < 0:
        player_x = 0

    if player_x > 770:
        player_x = 770

    if player_y < 0:
        player_y = 0

    if player_y > 570:
        player_y = 570

    screen.fill((12, 20, 28))


    # Pixel-art forest ground
    for x in range(0, 800, 16):
        for y in range(0, 600, 16):
            pygame.draw.rect(screen, (18, 35, 35),(x, y, 16, 16))

# Random-looking grass pixels
    for x in range(10, 800, 32):
        for y in range(10, 600, 32):pygame.draw.rect(screen, (35, 65, 48),(x, y, 4, 4))


# Pixel-art trees on the left
    for x, y in [(20, 80), (90, 180), (25, 300), (110, 360)]:
        pygame.draw.rect(screen, (45, 30, 28), (x + 12, y + 20, 12, 30))
        pygame.draw.rect(screen, (14, 45, 35), (x, y, 36, 36))
        pygame.draw.rect(screen, (20, 60, 42), (x + 6, y - 8, 36, 36))
        pygame.draw.rect(screen, (28, 75, 48), (x + 12, y, 24, 24))

# Pixel-art trees on the right
    for x, y in [(700, 70), (735, 200), (680, 320), (735, 400)]:
        pygame.draw.rect(screen, (45, 30, 28), (x + 12, y + 20, 12, 30))
        pygame.draw.rect(screen, (14, 45, 35), (x, y, 36, 36))
        pygame.draw.rect(screen, (20, 60, 42), (x + 6, y - 8, 36, 36))
        pygame.draw.rect(screen, (28, 75, 48), (x + 12, y, 24, 24))
# Left bush
    pygame.draw.rect(screen, (63, 57, 57), (60, 420, 60, 25))
    pygame.draw.rect(screen, (63, 57, 57), (75, 400, 35, 25))
    pygame.draw.rect(screen, (46, 41, 50), (85, 410, 25, 20))

# Right bush
    pygame.draw.rect(screen, (63, 57, 57), (650, 420, 70, 25))
    pygame.draw.rect(screen, (63, 57, 57), (670, 400, 35, 25))
    pygame.draw.rect(screen, (46, 41, 50), (675, 410, 25, 20)) 

# Winding forest path
    for y in range(0, 600, 16):
        path_x = 350 + int(35 * math.sin(y / 70))

        pygame.draw.rect(
        screen,
        (48, 43, 38),
        (path_x, y, 64, 16)
    )

        pygame.draw.rect(
        screen,
        (60, 53, 43),
        (path_x + 8, y + 4, 8, 4)
    )

# Magical forest lights
    for x, y in [(160, 120), (240, 350), (570, 180), (620, 390), (400, 100)]:
       pygame.draw.rect(screen, (45, 85, 65), (x - 4, y - 4, 12, 12))
       pygame.draw.rect(screen, (110, 160, 105), (x, y, 4, 4))
       pygame.draw.rect(screen, (220, 230, 150), (x + 1, y + 1, 2, 2))
# grass
    for x in range(10, 800, 25):
        for y in range(430, 590, 20):
            pygame.draw.rect(screen,(86, 142, 104),(x, y, 4, 4))
# Magical mushrooms
    for x, y in [(150, 250), (610, 300), (270, 470), (540, 450)]:
        pygame.draw.rect(screen, (220, 90, 100), (x, y, 12, 6))
        pygame.draw.rect(screen, (230, 180, 140), (x + 4, y + 6, 4, 6))
        pygame.draw.rect(screen, (255, 220, 180), (x + 3, y + 2, 3, 2))
# player
    # Hood
    pygame.draw.circle(
    screen, (55, 45, 65),
    (player_x + 15, player_y + 10), 13
)

# Dark face inside the hood
    pygame.draw.circle(
    screen, (25, 22, 32),
    (player_x + 15, player_y + 12), 8
)

# Cloak
    pygame.draw.polygon(
    screen, (75, 55, 85),
    [
        (player_x + 5, player_y + 12),
        (player_x + 25, player_y + 12),
        (player_x + 27, player_y + 28),
        (player_x + 3, player_y + 28)
    ]
)


    # Glowing eyes
    if player_direction == "left":
        eye1_x, eye2_x = player_x + 7, player_x + 14
        eye_y = player_y + 10

    elif player_direction == "right":
        eye1_x, eye2_x = player_x + 12, player_x + 19
        eye_y = player_y + 10

    elif player_direction == "up":
        eye1_x, eye2_x = player_x + 10, player_x + 17
        eye_y = player_y + 6

    else:
        eye1_x, eye2_x = player_x + 10, player_x + 17
        eye_y = player_y + 15

    pygame.draw.rect(screen, (217, 217, 138), (eye1_x, eye_y, 3, 2))
    pygame.draw.rect(screen, (217, 217, 138), (eye2_x, eye_y, 3, 2))
# Little boots
    pygame.draw.rect(
    screen, (35, 28, 38),
    (player_x + 4, player_y + 26, 8, 4)
)

    pygame.draw.rect(
    screen, (35, 28, 38),
    (player_x + 18, player_y + 26, 8, 4)
)


# Firefly movement
    if not firefly_collected:
        firefly_y += firefly_direction * 0.2

        if firefly_y >= firefly_start_y + 20:
            firefly_direction = -1
        elif firefly_y <= firefly_start_y - 20:
            firefly_direction = 1



       # Collision detection
    firefly_rect = pygame.Rect(
        firefly_x, int(firefly_y), 10, 10
    )
    player_rect = pygame.Rect(player_x, player_y, 30, 30)

    if not firefly_collected and player_rect.colliderect(firefly_rect):
        score += 1

        if score < 5:
            firefly_x = random.randint(30, 740)
            firefly_y = random.randint(30, 540)
            firefly_start_y = firefly_y
            firefly_direction = 1
        else:
            firefly_collected = True


       # Firefly and glow
    if not firefly_collected:
        pygame.draw.circle(
    screen, (86, 142, 104),
    (firefly_x + 5, int(firefly_y) + 5), 18
)

        pygame.draw.circle(
    screen, (160, 170, 110),
    (firefly_x + 5, int(firefly_y) + 5), 13
)
        pygame.draw.circle(
            screen,
            (217, 217, 138),
            (firefly_x + 5, int(firefly_y) + 5),
            10
        )

        pygame.draw.rect(
    screen,
    (255, 240, 170),
    (firefly_x + 2, int(firefly_y) + 2, 6, 6)
)

    # Score
    score_text = font.render(
        f"Fireflies: {score}", True, (255, 255, 255)
    )
    screen.blit(score_text, (20, 20))


    if score >= 5:
        screen.fill((11, 11, 24))
        win_text = font.render("YOU SAVED THE FOREST!", True, (217, 217, 138))
        screen.blit(win_text, (170, 250))
        restart_text = font.render("Press R to play again", True, (255, 255, 255))
        screen.blit(restart_text, (220, 310))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

