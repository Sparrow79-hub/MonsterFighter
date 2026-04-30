import pygame
import pygame_gui
from pygame_gui import UIManager
from pygame_gui.elements import UITextBox
from pygame.locals import *

pygame.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Averneth")

# all the buttons the game will use
Inventory = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 635, 100, 50)),
                                            text="Inventory",
                                            manager=manager)

Attack = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 635, 100, 50)),
                               text="Swing",
                               manager=manager)

placeholder1= pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 635, 100, 50)),
                               text="Pick Up",
                               manager=manager)

placeholder2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 635, 100, 50)),
                               text="Run",
                               manager=manager)

clock = pygame.time.Clock()
running = True

# Layout rectangles
location_rect = pygame.Rect(0, 0, SCREEN_WIDTH, 60)
message_rect = pygame.Rect(0, 60, SCREEN_WIDTH, 460)
stats_rect = pygame.Rect(0, 520, SCREEN_WIDTH, 50)
input_rect = pygame.Rect(0, 570, SCREEN_WIDTH, 50)
button_rect = pygame.Rect(0, 620, SCREEN_WIDTH, 80)

font = pygame.font.SysFont("Arial", 20)

message = []

def add_message(text):
    message.append(text)
    if len(message) > 20:
        message.pop(0)

while running:
    manager.update(clock.tick(60) / 1000.0)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                add_message("up arrow pressed - Go North")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                add_message("up arrow pressed - Go South")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                add_message("up arrow pressed - Go West")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                add_message("up arrow pressed - Go East")

    screen.fill((26, 26, 46))
    pygame.draw.rect(screen, (40, 40, 60), location_rect)
    pygame.draw.rect(screen, (20, 20, 40), message_rect)
    pygame.draw.rect(screen, (40, 40, 60), stats_rect)
    pygame.draw.rect(screen, (30, 30, 50), input_rect)
    pygame.draw.rect(screen, (40, 40, 60), button_rect)

    pygame.draw.line(screen, (100, 100, 140), (0, 60), (SCREEN_WIDTH, 60), 1)
    pygame.draw.line(screen, (100, 100, 140), (0, 520), (SCREEN_WIDTH, 520), 1)
    pygame.draw.line(screen, (100, 100, 140), (0, 570), (SCREEN_WIDTH, 570), 1)
    pygame.draw.line(screen, (100, 100, 140), (0, 620), (SCREEN_WIDTH, 620), 1)

    for i, msg in enumerate(message):
        text_surface = font.render(msg, True, (255, 255, 255))
        screen.blit(text_surface, (10, 70 + (i * 22)))

    manager.draw_ui(screen)

    pygame.display.update()


pygame.quit()

