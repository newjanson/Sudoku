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
    _running: bool
    screen: pygame.Surface
    stage_width: int
    stage_height: int
    size: tuple
    buttons_pressed: None
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)

    def __init__(self, w, h) -> None:
        """
        Initialize a Main Menu that has a display screen and Main Menu buttons.
        """
        self._running = False

        self.screen = None
        self.stage_width, self.stage_height = w, h - 1
        self.size = (w, h)

        self.buttons_pressed = None

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

        font = pygame.font.SysFont('consolas', 75)
        text = font.render("Sudoku", True, self.YELLOW)
        textRect = text.get_rect()
        textRect.center = (self.stage_width // 2, self.stage_height // 2)
        self.screen.blit(text, textRect)

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
