print ("Crazy Crosswords")

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

display_grid()

word_list = ['PYTHON', 'JAVA', 'RUBY', 'SWIFT', 'KOTLIN']

clues = {
    'PYTHON': 'A popular programming language known for its readability.', 
    'JAVA': 'A programming language that is class-based and object-oriented.',
    'RUBY': 'A dynamic, open source programming language with a focus on simplicity.',
    'SWIFT': 'A powerful programming language for iOS and macOS development.',
    'KOTLIN': 'A modern programming language that interoperates fully with Java.'
}

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