import pygame
import pygame_gui
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Averneth")

clock = pygame.time.Clock()
running = True

pygame.Rect()

# Layout rectangles
location_rect = pygame.Rect(0, 0, screen_width, 60)
message_rect = pygame.Rect(0, 60, screen_width, 420)
stats_rect = pygame.Rect(0, 480, screen_width, 60)
input_rect = pygame.Rect(0, 540, screen_width, 60)

font = pygame.font.SysFont("Arial", 20)

while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    screen.fill((26, 26, 46))
    pygame.draw.rect(screen, (40, 40, 60), location_rect)
    pygame.draw.rect(screen, (20, 20, 40), message_rect)
    pygame.draw.rect(screen, (40, 40, 60), stats_rect)
    pygame.draw.rect(screen, (30, 30, 50), input_rect)

    pygame.draw.line(screen, (100, 100, 140), (0, 60), (screen_width, 60), 1)
    pygame.draw.line(screen, (100, 100, 140), (0, 480), (screen_width, 480), 1)
    pygame.draw.line(screen, (100, 100, 140), (0, 640), (screen_width, 640), 1)

    pygame.display.update()
    clock.tick(60)

pygame.quit()

