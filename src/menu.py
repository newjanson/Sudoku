from __future__ import annotations
from typing import Optional
import pygame


class Menu:
    """
    This class represents the Main Menu.

    === Private Attributes ===
    _running: to show if the game is running or not, represented by a boolean.

    === Public Attributes ===
    screen: the GUI screen that pops up when main.py is ran.
    stage_width: the width of the stage.
    stage_height: the height of the stage.
    size: the size of the screen.
    buttons_pressed: represents the buttons for when the user wants to do something.
    """
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    BUTTON_COLOR = (30, 30, 80)
    TEXT_COLOR = (250, 250, 250)
    x: int
    y: int
    mx: int
    my: int
    button_width: int
    button_height: int
    _running: bool
    screen: pygame.Surface
    stage_width: int
    stage_height: int
    size: tuple
    buttons_pressed: None
    button: pygame.rect

    def __init__(self, w, h) -> None:
        """
        Initialize a Main Menu that has a display screen and Main Menu buttons.
        """
        pygame.init()
        self._running = False

        self.screen = None
        self.stage_width, self.stage_height = w, h - 1
        self.button_height = 70
        self.button_width = 220
        self.x = 250 - self.button_width//2
        self.y = 250 - self.button_width//2
        self.z = self.x
        self.w = self.y + 100
        self.mx = 0
        self.my = 0
        self.size = (w, h)
        self.button = None

        self.buttons_pressed = None
        self.BUTTON_FONT = pygame.font.SysFont('consolas', 30)

    def on_init(self) -> None:
        """
        Initialize the Main Menu's screen, and begin running the game.
        """
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event: pygame.Event) -> None:
        """
        React to the given <event> as appropriate.
        """
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self) -> None:
        """
        Check if the buttons are pressed in the Main Menu.
        """
        pass

    def on_render(self) -> None:
        """
        Render all the Main Menu's elements onto the screen.
        """
        self.screen.fill(self.BLACK)

        center_x, center_y = self.x + self.button_width//2, self.y + self.button_height//2
        font = pygame.font.SysFont('consolas', 75)
        text = font.render("Sudoku", True, self.YELLOW)

        pygame.draw.rect(self.screen, self.BUTTON_COLOR, (self.x, self.y, self.button_width, self.button_height))
        pygame.draw.rect(self.screen, self.BUTTON_COLOR, (self.z, self.w, self.button_width, self.button_height))
        textSurfaceOne = self.BUTTON_FONT.render("Play", True, self.TEXT_COLOR)
        textSurfaceTwo = self.BUTTON_FONT.render("Quit", True, self.TEXT_COLOR)

        self.screen.blit(text, text.get_rect(center=(center_x, center_y - 100)))
        self.screen.blit(textSurfaceOne, textSurfaceOne.get_rect(center=(center_x, center_y)))
        self.screen.blit(textSurfaceTwo, textSurfaceTwo.get_rect(center=(center_x, center_y + 100)))

        pygame.display.flip()

    def on_cleanup(self) -> None:
        """
        Clean up and close the Main Menu.
        """
        pygame.quit()

    def on_execute(self) -> None:
        """
        Run the Main Menu until the Menu is closed.
        """
        self.on_init()

        while self._running:
            pygame.time.wait(1000)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def menu_close(self) -> None:
        """
        Close the Menu when a button is pressed.
        """
        pass

