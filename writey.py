#Just a simple input/loop example

from pyfiglet import Figlet

f = Figlet(font='ogre')

game_on = True
while game_on:
    response = input("Write something > ")
    # print(response.upper())
    print(f.renderText(response))
    again = input('again? (Y/N) ').lower()
    if not again.startswith("y"):
        game_on = False
print("game over")
exit(0)