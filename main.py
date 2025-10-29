import random
import clues as clues_module
import medium_clues as medium_clues_module
import Hard_clues as Hard_clues_module


print ("Crazy Crosswords")

from clues import clues
from medium_clues import medium_clues
from Hard_clues import Hard_clues


grid = [
    ['', '', '', '', ''],
    ['', '', '', '', ''], 
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', '']
]

def display_grid():
    for row in grid:
        print(' | '.join(cell if cell != '' else ' ' for cell in row))
        print('-' * 21)


word_list = ['PYTHON', 'JAVA', 'RUBY', 'SWIFT', 'KOTLIN']
clues = clues_module.clues

clues = {
    “PYTHON”: “A popular programming language”,
    “LOOP”: “A code structure that repeats”}

for word, clue in clues.items():
    print(f“Clue: {clue}”)
    guess = input(“Your guess: “).upper()

    if guess == word:
        print(“Correct!”)
    else:
        print(“Try again.”)

correct_guesses = 0

for word, clue in clues.items():
    print(f“Clue: {clue}”)
    guess = input(“Your guess: “).upper()

    if guess == word:
        print(“Correct!”)
        correct_guesses += 1
    else:
        print(“Try again.”)

if correct_guesses == len(clues):
    print(“You solved the crossword puzzle!”)
else:
    print(“Keep trying!”)


def display_clues():
    print("Clues:")
    for word, clue in clues.items():
        print(f"{word}: {clue}")

display_clues()
def place_word_horizontally(word, row, col):
    for i in range(len(word)):
        grid[row][col + i] = word[i]
def place_word_vertically(word, row, col):
    for i in range(len(word)):
        grid[row + i][col] = word[i]
place_word_horizontally("JAVA", 0, 0)
place_word_vertically("RUBY", 0, 5)
display_grid()
place_word_horizontally("SWIFT", 3, 0)
place_word_vertically("KOTLIN", 0, 4)
display_grid()
grid[0][0] = "J"
grid[0][1] = "A"
grid[0][2] = "V"
grid[0][3] = "A"
grid[1][0] = "P"
grid[2][0] = "Y"
grid[3][0] = "T"
grid[4][0] = "H"
grid[5][0] = "O"
grid[6][0] = "N"
display_grid()
print("Congratulations! You've completed the crossword puzzle.")")
grid[1][0] = ("P")
grid[1][1] = ("Y")
grid[1][2] = ("T")
grid[1][3] = ("H")
grid[1][4] = ("O")
grid[1][5] = ("N")


display_grid()print("Congratulations! You've completed the crossword puzzle.")