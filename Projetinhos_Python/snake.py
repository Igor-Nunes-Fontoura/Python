import pygame, random
from pygame.locals import *

def on_grid_random(): # Gera uma posição aleatoria na tela
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x // 10 * 10, y // 10 * 10)

def collision(c1, c2): # Detecta a colisao
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

# Variaveis
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600)) # Tamanho da jenala
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

snake = [(200, 200), (210, 200), (220, 200)] # Tamanho inicial da cobra
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((0, 0, 255))
my_direction = LEFT

apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

game_over = False
while not game_over:
    clock.tick(10) # "Velocidade" do jogo
    for event in pygame.event.get(): # Acaba o jogo quando fechar a janela
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN: # Movimentação
            if event.key == K_w and my_direction != DOWN:
                my_direction = UP
            if event.key == K_s and my_direction != UP:
                my_direction = DOWN
            if event.key == K_a and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_d and my_direction != LEFT:
                my_direction = RIGHT
    
    if collision(snake[0], apple_pos): # Detecta se a cobra pegou a maça
        apple_pos = on_grid_random()
        snake.append((0, 0))
        score += 1
    
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0: # Detecta se a cobra saiu da tela
        game_over = True
        break

    for i in range(1, len(snake) - 1): # Detecta se a cobra bateu nela mesma
        if snake[0][0] ==  snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break
    
    if game_over:
        break

    for i in range(len(snake) -1 , 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    # Movimentaçao
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])

    screen.fill((175, 215, 70)) # Pinta a tela
    screen.blit(apple, apple_pos) # Desenha a maça na tela

    for pos in snake: # Desenha a cobra
        screen.blit(snake_skin, pos)

    score_font = font.render(f'Score: {score}', True, (255, 255, 255)) # Mostra os pontos na tela
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)
    
    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255)) # Mostra "Game Over" na tela quando perder
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()