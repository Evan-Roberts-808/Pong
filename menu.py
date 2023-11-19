import pygame
from two_player import main_2_player

pygame.init()

width, height = 1200, 900
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong - Main Menu")

title_font = pygame.font.SysFont("impact", 100)
font = pygame.font.SysFont("arial", 50)

title = title_font.render("Pong", 1, (255, 255, 255))
one_player_text = font.render("1 Player", 1, (255, 255, 255))
two_player_text = font.render("2 Players", 1, (255, 255, 255))

def draw_menu():
    window.fill((0, 0, 0))

    window.blit(title, (width // 2 - title.get_width() // 2, 50))
    window.blit(one_player_text, (width // 2 - one_player_text.get_width() // 2, height // 3))
    window.blit(two_player_text, (width // 2 - two_player_text.get_width() // 2, 2 * height // 3))

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
                    main_1_player()
                elif width // 2 - two_player_text.get_width() // 2 <= x <= width // 2 + two_player_text.get_width() // 2 \
                        and 2 * height // 3 <= y <= 2 * height // 3 + two_player_text.get_height():
                    main_2_player(main_menu)

    pygame.quit()

if __name__ == "__main__":
    main_menu()