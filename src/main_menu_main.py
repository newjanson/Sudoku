"""
This module loads, configures and runs the main menu.
"""

from menu import Menu

if __name__ == "__main__":

    width = 500
    height = 500

    menu = Menu(width, height)
    menu.on_execute()
