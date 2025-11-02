print("Loaded Crossword.py")  # Help check if the correct file is loaded
from flask import Flask, render_template, request  

app = Flask(__name__)  # Create the Flask application instance


# Clues
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

clue_sets = {"easy": easy_clues, "medium": medium_clues, "hard": hard_clues} # stores all difficuties 



# Grid Builder

def build_grid(words):
    """Creates crossword grid from the provided positions and adds clue numbers."""
    max_row = max(r + (len(w) if d.lower() == "down" else 1) for _, w, r, c, d in words)
    max_col = max(c + (len(w) if d.lower() == "across" else 1) for _, w, r, c, d in words)
    grid = [[{"letter": None, "number": None} for _ in range(max_col)] for _ in range(max_row)] # creating a blank grid 

    # Place words and numbers
    for number, word, row, col, direction in words:
        for i, ch in enumerate(word):
            if direction.lower() == "across":
                grid[row][col + i]["letter"] = ch
            elif direction.lower() == "down":
                grid[row + i][col]["letter"] = ch

        # this puts the clue number at the start of the word
        grid[row][col]["number"] = number

    return grid



# Grid Contents
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

grid_sets = {
    "easy": build_grid(easy_words),
    "medium": build_grid(medium_words),
    "hard": build_grid(hard_words),
}


# Game State
guessed_words = []
current_difficulty = "easy"


# Routes

@app.route("/", methods=["GET", "POST"])
def home():
    global guessed_words, current_difficulty

    message = None

    if request.method == "POST":
        # Handle difficulty change
        if "difficulty" in request.form:
            current_difficulty = request.form["difficulty"]
            guessed_words = []
            message = None

        # Handle guessed words
        elif "word" in request.form:
            word = request.form["word"].upper()
            if word in clue_sets[current_difficulty]:
                if word not in guessed_words:
                    guessed_words.append(word)
                message = f"✅ Correct! {word} has been revealed."
            else:
                message = f"❌ Incorrect! '{word}' is not in this crossword."

        # Handle reset
        elif "reset" in request.form:
            guessed_words = []
            message = None

    full_grid = grid_sets[current_difficulty]

    # Create visible grid
    visible_grid = []
    for row in full_grid:
        visible_row = []
        for cell in row:
            letter = cell["letter"]
            number = cell["number"]
            if letter and any(letter in word for word in guessed_words):
                visible_row.append({"letter": letter, "number": number})
            else:
                visible_row.append({"letter": "?" if letter else None, "number": number})
        visible_grid.append(visible_row)

    return render_template(
        "index.html",
        grid_layout=visible_grid,
        difficulty=current_difficulty,
        clues=clue_sets[current_difficulty],
        guessed_words=guessed_words,
        message=message,
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)




