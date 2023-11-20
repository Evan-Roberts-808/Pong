import pygame
from two_player import main_2_player
from one_player import main_1_player
import neat
import os
import pickle

pygame.init()

width, height = 1200, 900
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, "config.txt")
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                        neat.DefaultSpeciesSet, neat.DefaultStagnation,
                        config_path)

title_font = pygame.font.SysFont("impact", 100)
font = pygame.font.SysFont("arial", 50)
control_font = pygame.font.SysFont("arial", 30)

title = title_font.render("Pong", 1, (255, 255, 255))
one_player_text = font.render("1 Player", 1, (255, 255, 255))
two_player_text = font.render("2 Players", 1, (255, 255, 255))
controls_title = control_font.render("Controls", 1, (255, 255, 255))
p1_controls = control_font.render("P1: W: Move Up, S: Move Down", 1, (255, 255, 255))
p2_controls = control_font.render("P2: Up Arrow: Move Up, Down Arrow: Move Down", 1, (255, 255, 255))

with open("best.pickle", "rb") as f:
    winner = pickle.load(f)

def draw_menu():
    window.fill((0, 0, 0))

    window.blit(title, (width // 2 - title.get_width() // 2, 50))
    window.blit(one_player_text, (width // 2 -
                one_player_text.get_width() // 2, height // 3))
    window.blit(two_player_text, (width // 2 -
                two_player_text.get_width() // 2, 2 * height // 3))
    window.blit(controls_title, (width // 2 -
                controls_title.get_width() // 2, 700))
    window.blit(p1_controls, (width // 2 - p1_controls.get_width() // 2, 750))
    window.blit(p2_controls, (width // 2 - p2_controls.get_width() // 2, 790))

    pygame.display.update()


def main_menu():
    run_menu = True
    clock_menu = pygame.time.Clock()

    while run_menu:
        clock_menu.tick(60)
        draw_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if width // 2 - one_player_text.get_width() // 2 <= x <= width // 2 + one_player_text.get_width() // 2 \
                        and height // 3 <= y <= height // 3 + one_player_text.get_height():
                    main_1_player(main_menu, winner, config)
                elif width // 2 - two_player_text.get_width() // 2 <= x <= width // 2 + two_player_text.get_width() // 2 \
                        and 2 * height // 3 <= y <= 2 * height // 3 + two_player_text.get_height():
                    main_2_player(main_menu)

    pygame.quit()


if __name__ == "__main__":
    main_menu()
