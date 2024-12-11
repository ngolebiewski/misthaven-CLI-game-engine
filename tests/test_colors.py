from ..colors import COLORS, ascii_txt, clear_screen

def test_COLORS():
    assert COLORS["reset"] == "\033[0m"