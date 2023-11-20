import pygame
from entities import Paddle, Ball
from game import draw, handle_collision, handle_paddle_movement
import neat

pygame.init()

width, height = 1200, 900
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

fps = 60

def main_1_player(main_menu, genome, config):
    run = True
    clock = pygame.time.Clock()
    
    net = neat.nn.FeedForwardNetwork.create(genome, config)

    ai_paddle = Paddle(width - 30, height // 2 - 75, 20, 150)
    player_paddle = Paddle(10, height // 2 - 75, 20, 150)
    ball = Ball(width // 2, height // 2, 10)

    player_score = 0
    ai_score = 0

    while run:
        clock.tick(fps)
        draw(window, [player_paddle, ai_paddle], ball, player_score, ai_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, player_paddle, None, height, ai_paddle)

        ai_output = net.activate((ai_paddle.y, ball.y, abs(ai_paddle.x - ball.x)))
        ai_decision = ai_output.index(max(ai_output))

        if ai_decision == 1:
            ai_paddle.move(up=True)
        elif ai_decision == 2:
            ai_paddle.move(up=False)

        ball.move()
        player_score, ai_score = handle_collision(window, ball, player_paddle, ai_paddle, height, player_score, ai_score)

        if ball.x < 0:
            ai_score += 1
            ball.reset()
        elif ball.x > width:
            print("player scored")
            player_score += 1
            ball.reset()

        won = False
        if player_score >= 10:  
            won = True
            win_text = "You win!"
        elif ai_score >= 10: 
            won = True
            win_text = "AI wins!"

        if won:
            text = pygame.font.SysFont("arial", 50).render(win_text, 1, (255, 255, 255))
            window.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(5000)
            main_menu()
            ball.reset()
            player_paddle.reset()
            ai_paddle.reset()
            player_score = 0
            ai_score = 0

    pygame.quit()
