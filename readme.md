# Command Line Interface Game Engine for 'Choose Your Own Adventure' style interactive fiction.

## Run the project

0. Do you have Python3 and a recent version of PIP?
1. Clone github repo (This is the SSH command): `git@github.com:ngolebiewski/misthaven-CLI-game-engine.git`
2. Create/Activate Virtual Environment:
    1. Create venv directory in the project folder: `python -m venv venv`
    2. Activate
        - Mac/Linux: `$ source venv/bin/activate`
        - Windows Power Shell (IDK, haven't used Windows in over a decade): `PS C:\> venv\Scripts\Activate.ps1`
    * more help: https://docs.python.org/3/library/venv.html#creating-virtual-environments
3. Install required packages via `pip3 install -r requirements.txt`
4. Run program on CLI in Terminal, etc.: `python3 main.py`

## Concept
- Run a Command Line Interface text adventure, in the style of a Choose Your Own Adventure Book. 
- Import adventure from a CSV file, so easy to write in a Google Sheet for non-programmers (but AHA, it IS programming!). 
    - Options/branches are in ALL CAPS and link the scenarios together, the code parses these out
- Make it look cool, use pyfiglet for display font.

## How to make
- See CSV file for template: `data.csv`
- Must include a row with name "Intro" to kick off the story
	
## See the Docs

- Write this in your terminal: `python3 -m pydoc -p 8080` 

## Note to self:
- `pip3 freeze > requirements.txt`

![Intro Screen](images/book_cover.png)
