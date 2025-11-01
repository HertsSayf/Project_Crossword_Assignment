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

#Grid Builder - Builds grids using coordinates

def build_grid(words):
    max_row = max(r + (len(w) if d in ["down", "up"] else 1) for w, r, c, d in words)
    max_col = max(c + (len(w) if d == "across" else 1) for w, r, c, d in words)
    grid = [[None for _ in range(max_col)] for _ in range(max_row)]

    for word, row, col, direction in words:
        for i, ch in enumerate(word):
            if direction == "across":
                grid[row][col + i] = ch
            elif direction == "down":
                grid[row + i][col] = ch
            elif direction == "up":
                grid[row - i][col] = ch
    return grid

easy_words = [
    ("SWIFT", 1, 2, "down"),      # Starts above “PYTHON”, connects with T
    ("JAVA", 2, 3, "across"),     # Right of W in SWIFT
    ("PYTHON", 5, 0, "across"),   # Base horizontal word
    ("KOTLIN", 4, 4, "down"),     # Connects to O in PYTHON
    ("RUBY", 6, 1, "down"),       # Starts directly below the 'Y' in PYTHON
]
easy_grid = build_grid(easy_words)

#Game State

guessed_words = []

#Route

@app.route("/", methods=["GET", "POST"])
def home():
    global guessed_words

    if request.method == "POST":
        if "word" in request.form:
            word = request.form["word"].upper()
            if word in easy_clues and word not in guessed_words:
                guessed_words.append(word)

    full_grid = easy_grid

    #Create blank grid to fill
    visible_grid = [[("" if cell else None) for cell in row] for row in full_grid]

    #Reveal guessed words
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
        clues=easy_clues,
        guessed_words=guessed_words
    )


if __name__ == "__main__":
    app.run(debug=True)
