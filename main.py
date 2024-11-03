import pygame
from pygame.locals import *
import sys

pygame.init()

screen_width = 845
screen_height = 565
console = pygame.image.load("Console 2.png")
console = pygame.transform.scale(console,(845,565) )
#set window size
window_size = (1690/2,1130/2)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("It's Raining Coconuts and Dinos")

def render_text(text, font_size, color=(255, 255, 255)):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()


    screen.blit(console, (0, 0))

    welcome_text, welcome_rect = render_text("Welcome to Text Adventure!", 48)
    welcome_rect.center = (screen_width // 2, screen_height // 2)
    screen.blit(welcome_text, welcome_rect)


    pygame.display.update()

