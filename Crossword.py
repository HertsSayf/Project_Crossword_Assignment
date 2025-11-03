print("Loaded Crossword.py")                        #help check if the correct file is loaded
from flask import Flask, render_template, request   #the flask web framework

app = Flask(__name__)                               #Creates the flask application instance 

#Clues
#These clues give a description on each word of their respective crossword
#They are important as needed to validate guesses and display the clue list

easy_clues = {
    'PYTHON': 'A popular programming language known for its readability.',
    'JAVA': 'A programming language that is class-based and object-oriented.',
    'RUBY': 'A dynamic, open source programming language with a focus on simplicity.',
    'SWIFT': 'A powerful programming language for iOS and macOS development.',
    'KOTLIN': 'A modern programming language that interoperates fully with Java.'
}

medium_clues = {
    'VARIABLE': 'A named storage location in a program that holds a value that can change.',
    'FUNCTION': 'A reusable block of code that performs a specific task when called.',
    'SYNTAX': 'The set of rules that defines how code must be written so the computer understands it.',
    'BOOLEAN': 'A type of value that can only be true or false.',
    'LOOP': 'A way to repeat a block of code several times until a condition is met.'
}

hard_clues = {
    'COMPILE': 'Turning your code into something the computer can actually run.',
    'ENCRYPTION': 'The process of scrambling information so only those with the key can read it.',
    'ALGORITHM': 'A logical set of steps used to solve a problem or perform a task.',
    'RECURSION': 'When a function calls itself to solve a problem.',
    'DEBUGGING': 'The process of finding and fixing errors in code.'
}

clue_sets = {"easy": easy_clues, "medium": medium_clues, "hard": hard_clues} #stores the clue sets under-
#different difficulties for easy access, stored within variable clue_sets


#Grid Builder - Builds grids using coordinates
#Creates a List of rows and columns filled with none (built in python null value), then adds the letters/words
#Each word has a responsible coord these help to find the words info which is necesary and listed below
#(WORD, start_row, start_col, direction) - direction can be either across or down

def build_grid(words):
    """Creates crossword grid from the provided positions."""
    #Compute the number of rows needed: for 'down' words add length to row, else +1 row
    max_row = max(r + (len(w) if d.lower() == "down" else 1) for _, w, r, c, d in words)  
    #Compute the number of columns needed: for 'across' words add length to col, else +1 col
    max_col = max(c + (len(w) if d.lower() == "across" else 1) for _, w, r, c, d in words)  
    #Initializes an empty grid using none
    grid = [[{"letter": None, "number": None} for _ in range(max_col)] for _ in range(max_row)]  

    #Places each letter of each word into the grid at the correct coords
    for num, word, row, col, direction in words:
        for i, ch in enumerate(word):           #loop over letters of the word using enumerate, ch - the letter at index position
            if direction.lower() == "across":   #If across advance column by the index number
                grid[row][col + i]["letter"] = ch
                if i == 0:
                    grid[row][col + i]["number"] = num
            elif direction.lower() == "down":   #If down, advance row by i
                grid[row + i][col]["letter"] = ch
                if i == 0:
                    grid[row + i][col]["number"] = num
    return grid                                 #Returns the filled grid, including None where there are no letters)


##Grid Contents
# This shows what words are going to be in each different grid
easy_words = [
    (1, "SWIFT", 1, 2, "down"),
    (2, "JAVA", 2, 3, "across"),
    (3, "PYTHON", 5, 0, "across"),
    (4, "KOTLIN", 4, 4, "down"),
    (5, "RUBY", 6, 1, "down"),
]

medium_words = [
    (1, "VARIABLE", 1, 5, "down"),
    (2, "SYNTAX", 2, 2, "down"),
    (3, "FUNCTION", 4, 0, "across"),
    (4, "BOOLEAN", 6, 5, "across"),
    (5, "LOOP", 6, 8, "down"),
]

hard_words = [
    (1, "COMPILE", 1, 4, "down"),
    (2, "ENCRYPTION", 7, 4, "across"),
    (3, "ALGORITHM", 2, 11, "down"),
    (4, "RECURSION", 7, 7, "down"),
    (5, "DEBUGGING", 15, 0, "across"),
]

grid_sets = {                             #this links each difficulty to its own crossword grid 
    "easy": build_grid(easy_words),
    "medium": build_grid(medium_words),
    "hard": build_grid(hard_words),
}

#This links each difficulty to a numbered set of clues for easier clue referencing
numbered_clues = {
    "easy": {1: "SWIFT", 2: "JAVA", 3: "PYTHON", 4: "KOTLIN", 5: "RUBY"},
    "medium": {1: "VARIABLE", 2: "SYNTAX", 3: "FUNCTION", 4: "BOOLEAN", 5: "LOOP"},
    "hard": {1: "COMPILE", 2: "ENCRYPTION", 3: "ALGORITHM", 4: "RECURSION", 5: "DEBUGGING"},
}


#Game State
guessed_words = []
current_difficulty = "easy"


#Routes
@app.route("/", methods=["GET", "POST"])
def home():
    global guessed_words, current_difficulty

    message = None 

    if request.method == "POST":
                                           #Handle difficulty change
        if "difficulty" in request.form:
            current_difficulty = request.form["difficulty"]
            guessed_words = []
            message = None

                                           #Handle guessed words
        elif "word" in request.form:
            word = request.form["word"].upper()
            if word in clue_sets[current_difficulty]:
                if word not in guessed_words:
                    guessed_words.append(word)
                message = f"✅ Correct! {word} has been revealed."
            else:
                message = f"❌ Incorrect! '{word}' is not in this crossword."

        elif "reset" in request.form:      #when the user resets the board 
            guessed_words = []
            message = None

    full_grid = grid_sets[current_difficulty]
                                          
    visible_grid = []                      #this shows the words when guessed and fills the rest with question marks 
    for row in full_grid:
        visible_row = []
        for cell in row:
                                           #If cell contains a letter, check if it should be revealed
            if cell["letter"]:
                                           #Reveal if the letter belongs to any guessed word
                revealed = any(cell["letter"] in word for word in guessed_words)
                visible_row.append({
                    "letter": cell["letter"] if revealed else "?",
                    "number": cell["number"]
                })
            else:
                                           #Keep empty spaces as None
                visible_row.append({"letter": None, "number": None})
        visible_grid.append(visible_row)

    return render_template(                #links data to the webpage 
        "index.html",
        grid_layout=visible_grid,
        difficulty=current_difficulty,
        clues=clue_sets[current_difficulty],
        guessed_words=guessed_words,
        message=message,
        numbered_clues=numbered_clues[current_difficulty],
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
