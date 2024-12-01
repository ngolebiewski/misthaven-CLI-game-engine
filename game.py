# game.py
import re
import csv

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

    def unescape_line_breaks(self):
        # When importing data from CSV, escape characters are escaped, and this fixes line breaks
        self.description = re.sub(r'\\n', '\n', self.description)
        self.options_text = re.sub(r'\\n', '\n', self.options_text)

    def get_fancy_text(self):
        return (self.fancy_text, self.color, self.font)
    
    def game_over_now(self):
        pass




### TESTS #####
# dynamic_name = 'intro'
# scenario_index[dynamic_name] = Scenario('Intro', 'Welcome to Misthaven\nThis is a medieval city, and the streets are bustling.', '1. Begin the ADVENTURE or 2. Call it QUITS', 'Welcome to Misthaven')
# scenario_index['quits'] = Scenario('Quist', 'You quit, game over', '1. start over or 2. goodbye', 'Game Over', color = 'red')
# scenario_index['adventure'] = Scenario('Adventure', "You're running down the street of Misthaven, away from the cops. They're in hot pursuit and want to take you back to the orphanage.", 'Do you want to run to the TAVERN or jump into a moving horse driven CART?', 'The Pursuit...')
# scenario_index['cart'] = Scenario(  'Cart', 
#                                     "You make it!\nYou jump into the cart and hide under a pile of hay. After what seems like hours, the cart stops and you hop out. You're no longer in the city and out in the farmlands...", 
#                                     'TBD...', 
#                                     'The Cart...',
#                                     score=20)

######## Set of print tests
# print(scenario_index['intro'].get_all())
# print(scenario_index['intro'].get_fancy_text())
# print(keyword_index)
# print(scenario_index['quits'].get_all())


def check_keyword_links(object_index, keywords):
    # Function to make sure there are no loose ends. Each keyword should point to an object for the story to continue.
    # Sort of like a tree made up of nodes...
    pass

def unescape_line_break(text):
    return re.sub(r'\\n', '\n', text)
    
def csv_to_scenarios(csv_file, default_font = 'ogre'):
    """Read CSV with scenarios, and loop over them to create scenarios and keep track of them in the scenario_index. (optional) Choose default pyfiglet font."""
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            dynamic_name = row['name'].lower()
            print(dynamic_name)
            scenario_index[dynamic_name] = Scenario(
                name=row['name'],
                description=row["description"],  
                options_text=row["options_text"], 
                fancy_text=row["fancy_text"],
                color=row.get('color', 'cyan') if row.get('color') != "" else default_font,  # Check for empty string
                font=row.get('font', 'ogre') if row.get('font') != "" else 'ogre', # Check for empty string
                score=int(row.get('score', 0)),
                game_over=row.get('game_over', 'False') == 'True',
                game_over_text=row.get("game_over_text", ""),
                special_function=row.get('special_function', None),
            )
            scenario_index[dynamic_name].unescape_line_breaks()
            print(scenario_index[dynamic_name].get_all())

# Populate the Scenarios from the CSV!!!
csv_to_scenarios('data.csv')
    
print(unescape_line_break('This is a choose your own adventure game\\nHere are the rules...'))

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
        
    