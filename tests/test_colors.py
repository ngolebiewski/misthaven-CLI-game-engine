from ..colors import COLORS, ascii_txt, clear_screen

def test_COLORS():
    assert COLORS["reset"] == "\033[0m"
    assert COLORS["cyan"] == "\033[96m"
    assert type(COLORS) == dict

def test_ascii_txt():
    assert ascii_txt("Hello World!") is not None  

def test_clear_screen():
    pass