# colors.py
from pyfiglet import Figlet
import os

"""COLORS dict: These are color codes to use in terminal to make the text different colors"""
COLORS= {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "underline": "\033[4m",
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "black": "\033[90m",
    "bg_red": "\033[41m",
    "bg_green": "\033[42m",
    "bg_yellow": "\033[43m",
    "bg_blue": "\033[44m",
    "bg_magenta": "\033[45m",
    "bg_cyan": "\033[46m",
    "bg_white": "\033[47m",
    "bg_black": "\033[40m"
}

def ascii_txt(text, color='cyan', font='marquee'):
    """ 
    Wrapper function to print ascii art text using figlet, choosing the the color and font.
    Arguments: 1. str of the text to transform. 2. (optional) color (from the COLOR dict) 3. (optional) font.
    List of figlet fonts can be found at http://www.figlet.org/examples.html
    """
    f = Figlet(font=font)
    ascii_art = f.renderText(text)
    # should check to make sure color is in COLORS --> .get() does it.
    return f"{COLORS.get(color, COLORS['cyan'])}{ascii_art}{COLORS['reset']}"

def clear_screen():
    """Clears the terminal screen on any platform, theoretically."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')