import pygame
import random
import sys


def save_high_score(high_score):
    with open("high_score.txt", "w") as file:
        file.write(str(high_score))


def load_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0


def game_over(game_window, white, high_score):
    my_font = pygame.font.SysFont('arial', 50)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, white)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    options_font = pygame.font.SysFont('arial', 30)
    restart_option = options_font.render('Press R to Restart', True, white)
    quit_option = options_font.render('Press Q to Quit', True, white)

    restart_rect = restart_option.get_rect()
    quit_rect = quit_option.get_rect()

    restart_rect.midtop = (window_x / 2, window_y / 2)
    quit_rect.midtop = (window_x / 2, window_y / 2 + 40)

    game_window.blit(restart_option, restart_rect)
    game_window.blit(quit_option, quit_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_high_score(high_score)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart_game()
                elif event.key == pygame.K_q:
                    save_high_score(high_score)
                    pygame.quit()
                    sys.exit()


def restart_game():
    global snake_position, snake_body, fruit_position, fruit_spawn, direction, change_to, score, snake_speed, high_score

    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                      random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True
    direction = 'RIGHT'
    change_to = direction
    score = 0
    snake_speed = 10

    game_loop()


def show_score(game_window, choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()

    if choice == 1:
        score_rect.midtop = (window_x / 10, 15)
    else:
        score_rect.midtop = (window_x / 2, window_y / 1.25)

    game_window.blit(score_surface, score_rect)


def show_high_score(game_window, choice, color, font, size, high_score):
    high_score_font = pygame.font.SysFont(font, size)
    high_score_surface = high_score_font.render('High Score : ' + str(high_score), True, color)
    high_score_rect = high_score_surface.get_rect()

    if choice == 2:
        high_score_rect.midtop = (window_x - 120, 15)  # Top right corner
        game_window.blit(high_score_surface, high_score_rect)


def game_loop():
    global high_score, change_to, direction, fruit_position, snake_position, snake_body, fruit_spawn, score, snake_speed
    global window_x, window_y, game_window, white

    pygame.init()
    pygame.joystick.init()

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    snake_speed = 10

    window_x = 600
    window_y = 400

    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 150, 255)

    pygame.display.set_caption('Easy Snake Game')
    game_window = pygame.display.set_mode((window_x, window_y))

    fps = pygame.time.Clock()

    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                      random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True
    direction = 'RIGHT'
    change_to = direction
    score = 0
    high_score = load_high_score()

    controller_input = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_high_score(high_score)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over(game_window, white, high_score)
            elif event.type == pygame.JOYAXISMOTION:
                if abs(joystick.get_axis(0)) > 0.1 or abs(joystick.get_axis(1)) > 0.1:
                    controller_input = True
                else:
                    controller_input = False

        if controller_input:
            x_speed = joystick.get_axis(0)
            y_speed = joystick.get_axis(1)
            snake_position[0] = (snake_position[0] + round(x_speed * 10)) % window_x
            snake_position[1] = (snake_position[1] + round(y_speed * 10)) % window_y

        snake_head_rect = pygame.Rect(snake_position[0], snake_position[1], 10, 10)
        fruit_rect = pygame.Rect(fruit_position[0], fruit_position[1], 10, 10)

        if snake_head_rect.colliderect(fruit_rect):
            score += 1
            snake_body.insert(0, list(snake_position))
            fruit_spawn = False
        else:
            snake_body.insert(0, list(snake_position))  # Insert new head position at the beginning of the snake body
            snake_body.pop()  # Remove the last segment of the snake body

        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                              random.randrange(1, (window_y // 10)) * 10]
        fruit_spawn = True
        game_window.fill(black)

        for pos in snake_body:
            pygame.draw.rect(game_window, blue,
                             pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, green, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))

        show_score(game_window, 1, white, 'arial', 20)
        show_high_score(game_window, 2, white, 'arial', 20, high_score)
        pygame.display.update()
        fps.tick(snake_speed)


game_loop()
