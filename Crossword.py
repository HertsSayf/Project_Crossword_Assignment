from flask import Flask, render_template, request

app = Flask(__name__)

#Clues

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

clue_sets = {"easy": easy_clues, "medium": medium_clues, "hard": hard_clues}


#Grid Builder - Builds grids using coordinates

def build_grid(words):
    """Creates crossword grid."""
    max_row = max(r + (len(w) if d.lower() == "down" else 1) for w, r, c, d in words)
    max_col = max(c + (len(w) if d.lower() == "across" else 1) for w, r, c, d in words)
    grid = [[None for _ in range(max_col)] for _ in range(max_row)]

    for word, row, col, direction in words:
        for i, ch in enumerate(word):
            if direction.lower() == "across":
                grid[row][col + i] = ch
            elif direction.lower() == "down":
                grid[row + i][col] = ch
    return grid


##Grid Contents

easy_words = [
    ("SWIFT", 1, 2, "down"),
    ("JAVA", 2, 3, "across"),
    ("PYTHON", 5, 0, "across"),
    ("KOTLIN", 4, 4, "down"),
    ("RUBY", 6, 1, "down"),
]

medium_words = [
    ("VARIABLE", 1, 5, "down"),
    ("SYNTAX", 2, 2, "down"),
    ("FUNCTION", 4, 0, "across"),
    ("BOOLEAN", 6, 5, "across"),
    ("LOOP", 6, 8, "down"),
]

hard_words = [
    ("COMPILE", 1, 4, "down"),
    ("ENCRYPTION", 7, 4, "across"),
    ("ALGORITHM", 2, 11, "down"),
    ("RECURSION", 7, 7, "down"),
    ("DEBUGGING", 15, 0, "across"),
]

grid_sets = {
    "easy": build_grid(easy_words),
    "medium": build_grid(medium_words),
    "hard": build_grid(hard_words),
}


#Game State

guessed_words = []
current_difficulty = "easy"

#Route

@app.route("/", methods=["GET", "POST"])
def home():
    global guessed_words, current_difficulty

    if request.method == "POST":
        if "difficulty" in request.form:
            current_difficulty = request.form["difficulty"]
            guessed_words = []
        elif "word" in request.form:
            word = request.form["word"].upper()
            if word in clue_sets[current_difficulty] and word not in guessed_words:
                guessed_words.append(word)

    full_grid = grid_sets[current_difficulty]

    # Start with placeholders so crossword shape appears
    visible_grid = [[("?" if cell else None) for cell in row] for row in full_grid]

    # Reveal guessed words
    for word in guessed_words:
        for r, row in enumerate(full_grid):
            row_str = "".join(c if c else "." for c in row)
            if word in row_str:
                start = row_str.index(word)
                for i in range(len(word)):
                    visible_grid[r][start + i] = full_grid[r][start + i]
        for c in range(len(full_grid[0])):
            col_str = "".join(full_grid[r][c] if full_grid[r][c] else "." for r in range(len(full_grid)))
            if word in col_str:
                start = col_str.index(word)
                for i in range(len(word)):
                    visible_grid[start + i][c] = full_grid[start + i][c]

    return render_template(
        "index.html",
        grid_layout=visible_grid,
        difficulty=current_difficulty,
        clues=clue_sets[current_difficulty],
        guessed_words=guessed_words
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)


