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

