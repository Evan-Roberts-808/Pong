import pygame
from entities import Paddle, Ball

def draw(window, paddles, ball, left_score, right_score):
    window.fill((0, 0, 0))

    left_score_text = pygame.font.SysFont("arial", 50).render(f"{left_score}", 1, (255, 255, 255))
    right_score_text = pygame.font.SysFont("arial", 50).render(f"{right_score}", 1, (255, 255, 255))

    window.blit(left_score_text, (window.get_width() // 4 - left_score_text.get_width() // 2, 30))
    window.blit(right_score_text, (window.get_width() * (3/4) - right_score_text.get_width() // 2, 30))

    for paddle in paddles:
        paddle.draw(window)

    for i in range(10, window.get_height(), window.get_height() // 20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(window, (255, 255, 255), (window.get_width() // 2 - 5, i, 10, window.get_height() // 20))

    ball.draw(window)
    pygame.display.update()

def handle_collision(window, ball, left_paddle, right_paddle, window_height, left_score, right_score):
    if ball.y  + ball.radius >= window_height:
        ball.y_velocity *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_velocity *= -1

    if ball.x_velocity < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_velocity *= -1

                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.max_velocity
                y_velocity = difference_in_y / reduction_factor
                ball.y_velocity = -1 * y_velocity

    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_velocity *= -1

                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / ball.max_velocity
                y_velocity = difference_in_y / reduction_factor
                ball.y_velocity = -1 * y_velocity

        if ball.x_velocity < 0 and ball.x - ball.radius <= 0:
            right_score += 1
            ball.reset()
        elif ball.x_velocity > 0 and ball.x + ball.radius >= window.get_width():
            left_score += 1
            ball.reset()

    return left_score, right_score

def handle_paddle_movement(keys, left_paddle, right_paddle, window_height):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.velocity >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.velocity + left_paddle.height <= window_height:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.velocity >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.velocity + right_paddle.height <= window_height:
        right_paddle.move(up=False)
