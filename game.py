# game.py
import re

scenario_index = dict()
keyword_index = list()

class Scenario:
    def __init__(self, name, description, options_text, fancy_text = None, color = 'cyan', font = 'ogre', score = 1, game_over=False, game_over_text=None, special_function=None):
        self.name = name.upper()
        self.description = description
        self.options_text = options_text
        self.forks = self.parse_forks(options_text)
        self.fancy_text = fancy_text
        self.color = color
        self.font = font
        self.score = score
        self.game_over = game_over
        self.game_over_text = game_over_text
        self.special_function = special_function
        
    @staticmethod 
    def parse_forks(options_text):
        keywords = re.findall(r"\b[A-Z]+\b", options_text)
        for word in keywords:
            keyword_index.append(word)
        return keywords
    
    def get_all(self):
        return {
            'name': self.name,
            'description': self.description,
            'options_text': self.options_text,
            'forks': self.forks,
            'fancy_text': self.fancy_text,
            'color': self.color,
            'font': self.font,
            'score': self.score,
            'game_over': self.game_over,
            'game_over_text': self.game_over_text
        }

    def get_fancy_text(self):
        return (self.fancy_text, self.color, self.font)
    
    def game_over_now(self):
        pass


# Read CSV with scenarios, and loop over them to create scenarios and keep track of them in the scenario_index
# def create_scenarios_from_csv(file_name):
# TKTKTKTK
dynamic_name = 'intro'
scenario_index[dynamic_name] = Scenario('Intro', 'Welcome to Misthaven\nThis is a medieval city, and the streets are bustling.', '1. Begin the ADVENTURE or 2. Call it QUITS', 'Welcome to Misthaven')
scenario_index['quits'] = Scenario('Quist', 'You quit, game over', '1. start over or 2. goodbye', 'Game Over', color = 'red')
scenario_index['adventure'] = Scenario('Adventure', "You're running down the street of Misthaven, away from the cops. They're in hot pursuit and want to take you back to the orphanage.", 'Do you want to run to the TAVERN or jump into a moving horse driven CART?', 'The Pursuit...')
scenario_index['cart'] = Scenario(  'Cart', 
                                    "You make it!\nYou jump into the cart and hide under a pile of hay. After what seems like hours, the cart stops and you hop out. You're no longer in the city and out in the farmlands...", 
                                    'TBD...', 
                                    'The Cart...',
                                    score=20)

def check_keyword_links(object_index, keywords):
    # Function to make sure there are no loose ends. Each keyword should point to an object for the story to continue.
    # Sort of like a tree made up of nodes...
    pass

# # Set of tests
# print(scenario_index['intro'].get_all())
# print(scenario_index['intro'].get_fancy_text())
# print(keyword_index)
# print(scenario_index['quits'].get_all())

class Character:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.health = 100
    
    def get_name(self):
        return self.name
    
    def get_health(self):
        return self.health
    
    def get_score(self):
        return self.score
    
    def update_health(self, num):
        self.health += num
        
    def update_score(self, num):
        self.score += num
        
    def reset_score(self):
        self.score = 0
        
    