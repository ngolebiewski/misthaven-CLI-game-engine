
from colors import COLORS, ascii_txt, clear_screen
import game

# About: A CLI Interactive Game Engine by Nick Golebiewski. 
# November/December 2024

#set this to your game title
game_title = 'Misthaven'

#should refactor functions to return the sets of strings, rather than print
def title_sequence():
    """AKA Book Cover"""
    clear_screen()
    print(ascii_txt(game_title, 'cyan'))
    print(ascii_txt('An Interactive Fiction Experience', 'yellow', 'ogre'))
    print(ascii_txt('By Vera and Nick Golebiewski', 'cyan', 'ogre'))
    input("Press enter to continue > ")

def player_setup():
    """Set your player's name and get the instructions, returns a Player object"""
    clear_screen()
    name = input("Dear Player, What is your name? ")
    clear_screen()
    player = game.Character(name) 
    print(ascii_txt(f"Welcome {player.get_name()}, your adventure awaits...", 'yellow', 'ogre'))
    print("This is how you play:\n1. Type in any of the CAPITALIZED words in the scene's options to move forward in the choose-your-own-adventure story.\n2. Other options include 'quit' and 'help' and 'status.\n3. Enjoy!\n\n")
    print(ascii_txt(f"Options", 'yellow', "Mini"))
    print("Are you ready to play? YES/NO")
    input("> ")
    clear_screen()
    return player

def engine(player):
    """The Choose Your Own Adventure Game Engine, takes in a Player object as an argument"""
    scene = game.scenario_index['intro']
    game_over = False
    while not game_over:
        clear_screen()
        #should have some keywords like help, quit, status...
        
        # Change fancy text to title and make mandatory
        if scene.get_fancy_text:
            print(ascii_txt(*scene.get_fancy_text()))
        print(scene.description)
        # Add a special function that defaults to a function that is a pass, that can take the name of a special set of insturctions.
            #i.e. a fight module, or a thing to lose/gain health, perhaps even add a new keywork? I don't know.
        print(ascii_txt(f"Options", 'yellow', "Mini"))
        print(scene.options_text)
        
        # input response should be a loop until there is a valid "answer"
        response = input("> ")
     
        valid_keyword = False
        try:
            for keyword in scene.forks:
                if response.upper() == keyword:
                    scene = game.scenario_index[keyword.lower()]
                    valid_keyword = True
                    player.update_score(scene.score)
                    break
        except KeyError as e:
            print(f"Unfortunately that part of the story isn't written yet: {e}")
            break
        if not valid_keyword:
        # if self.game_over is true, read that stuff IMPORTANT! TKTK
            if response.lower() == 'help':
                keywords = ", ".join(map(lambda x: f"<{x}>", scene.forks))
                print(f"type <QUIT> to exit. Or one of the Keywords: {keywords} to continue")
            if response.lower() == 'quit':
                game_over = True
            else:
                # print(f"try either 'quit', 'help', or one of these Keywords: {scene.forks}")
                input("Press enter to continue > ")
    input("Press enter to continue > ")
    clear_screen()
            
def game_over_default(player):
    """Game Over, gives player an option to restart the game loop"""
    print(ascii_txt('Game Over', 'red'))
    print(f'{COLORS['underline']}{player.get_name()}, thank you for playing\nYour score was {player.get_score()}')
    opt = input("Play again? > ").lower()
    if opt.startswith("y"):
        player.reset_score()
        engine(player)
        game_over_default(player)
    exit(0)

def main():
    title_sequence()
    player = player_setup()
    engine(player)
    game_over_default(player)
    
if __name__ == "__main__":
    main()