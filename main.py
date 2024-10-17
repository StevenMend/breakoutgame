import pygame
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

# Colores mejorados
WHITE = (255, 255, 255)
RED = (255, 100, 100)
GREEN = (100, 255, 100)
BLUE = (100, 100, 255)
YELLOW = (255, 255, 100)

# FPS (Velocidad del juego)
FPS = 60
clock = pygame.time.Clock()

# Tamaños de la barra y la pelota
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BALL_RADIUS = 10

# Barra (paddle)
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 7

# Pelota
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, BALL_RADIUS)
ball_speed = [3, -3]

# Bloques
block_width = 60
block_height = 20
blocks = [pygame.Rect(x * block_width, y * block_height, block_width, block_height) for x in range(10) for y in
          range(4)]

# Vidas del jugador
lives = 3


def move_paddle():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-paddle_speed, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(paddle_speed, 0)


def move_ball():
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Rebote en las paredes
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]

    # Rebote en la barra
    if ball.colliderect(paddle):
        offset = (ball.centerx - paddle.centerx) / (PADDLE_WIDTH / 2)
        ball_speed[0] = offset * 5  # Controla el ángulo de rebote según el impacto
        ball_speed[1] = -ball_speed[1]


def check_collisions():
    for block in blocks[:]:
        if ball.colliderect(block):
            ball_speed[1] = -ball_speed[1]
            blocks.remove(block)


def reset_ball():
    global ball_speed
    ball.x = WIDTH // 2
    ball.y = HEIGHT // 2
    ball_speed = [random.choice([-3, 3]), -3]


def game_over_screen():
    screen.fill(YELLOW)
    font = pygame.font.Font(None, 50)
    text = font.render("Game Over! Play Again? (Y/N)", True, RED)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()

    # Esperar entrada del jugador
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                elif event.key == pygame.K_n:
                    return False


# Loop principal del juego
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLUE)

    # Movimiento de la barra y la pelota
    move_paddle()
    move_ball()

    # Colisiones
    check_collisions()

    # Dibujar la barra, pelota y bloques
    pygame.draw.rect(screen, GREEN, paddle)
    pygame.draw.circle(screen, WHITE, (ball.x + BALL_RADIUS // 2, ball.y + BALL_RADIUS // 2), BALL_RADIUS)
    for block in blocks:
        pygame.draw.rect(screen, RED, block)

    # Comprobar si la pelota se pasa
    if ball.bottom >= HEIGHT:
        lives -= 1
        if lives > 0:
            reset_ball()
        else:
            # Pantalla de "Game Over"
            if game_over_screen():
                # Reiniciar el juego
                lives = 3
                blocks = [pygame.Rect(x * block_width, y * block_height, block_width, block_height) for x in range(10)
                          for y in range(4)]
                reset_ball()
            else:
                running = False

    # Eventos de salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mostrar vidas restantes
    font = pygame.font.Font(None, 30)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(lives_text, (10, HEIGHT - 30))

    # Actualizar la pantalla
    pygame.display.flip()

pygame.quit()

