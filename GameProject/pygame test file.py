import pygame
import pygame_gui
from pygame_gui import UIManager
from pygame_gui.elements import UITextBox

import player

pygame.init()

pygame.display.set_caption('Averneth')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#1a1a2e'))

font = pygame.font.SysFont('Arial', 20)

text_surface = font.render("Welcome to Averneth!", True, pygame.Color(254, 254, 254))

game_display = UITextBox(relative_rect=pygame.Rect((50, 50, 100, 100)),
                         html_text="",)

manager = pygame_gui.UIManager((800, 600), theme_path="Theme.json")


#all the buttons the game will use
Inventory = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 450, 100, 100)),
                                            text="Inventory",
                                            manager=manager)

Attack = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((650, 450, 100, 100)),
                               text="Swing",
                               manager=manager)

placeholder1= pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 50, 100, 100)),
                               text="Test button 1",
                               manager=manager)

placeholder2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 50, 100, 100)),
                               text="Test button 1",
                               manager=manager)
clock = pygame.time.Clock()
is_running = True



while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == test_button:
                print("Test button 1 pressed!")

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))

    manager.draw_ui(window_surface)

    window_surface.blit(text_surface, (50, 50))

    pygame.display.update()

pygame.quit()
