import pygame
from entities import Paddle, Ball
from game import draw, handle_collision, handle_paddle_movement

pygame.init()

width, height = 1200, 900
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

fps = 60

def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, height // 2 - 75, 20, 150)
    right_paddle = Paddle(width - 30, height // 2 - 75, 20, 150)
    ball = Ball(width // 2, height // 2, 10)

    left_score = 0
    right_score = 0

    while run:
        clock.tick(fps)
        draw(window, [left_paddle, right_paddle], ball, left_score, right_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle, height)

        ball.move()
        left_score, right_score = handle_collision(window, ball, left_paddle, right_paddle, height, left_score, right_score)

        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > width:
            left_score += 1
            ball.reset()
        
        won = False
        if left_score >= 10:  
            won = True
            win_text = "Left Player wins"
        elif right_score >= 10: 
            won = True
            win_text = "Right Player wins"

        if won:
            text = pygame.font.SysFont("arial", 50).render(win_text, 1, (255, 255, 255))
            window.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0

    pygame.quit()

if __name__ == "__main__":
    main()
