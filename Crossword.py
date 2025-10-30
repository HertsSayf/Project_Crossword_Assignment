from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Difficulty levels and clues
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
    'ALGORITHM': 'A logical set of steps used to solve a problem or complete a task.',
    'ENCRYPTION': 'A way of scrambling information so only people with the right key can read it.',
    'COMPILE': 'What happens when your code gets turned into something the computer can actually run.',
    'RECURSION': 'When a function calls itself to solve a problem.',
    'DEBUGGING': 'The process of finding and fixing mistakes in your code.'
}

clue_sets = {"easy": easy_clues, "medium": medium_clues, "hard": hard_clues}

# Crossword grid layout (like your image)
grid_layout = [
    [None, None, None, None, 'S', None, None, None],
    [None, None, None, None, 'W', 'J', 'A', 'V', 'A'],
    [None, None, None, None, 'I', None, None, None],
    [None, None, None, None, 'F', 'K', None, None],
    ['P', 'Y', 'T', 'H', 'O', 'N', None, None],
    [None, None, None, None, None, 'T', None, None],
    [None, None, None, None, None, 'L', None, None],
    [None, None, None, None, None, 'I', None, None],
    [None, None, None, None, None, 'N', None, None],
    [None, 'R', 'U', 'B', 'Y', None, None, None],
]

guessed_words = []
current_difficulty = "easy"

@app.route("/", methods=["GET", "POST"])
def home():
    global guessed_words, current_difficulty
    if request.method == "POST":
        if "difficulty" in request.form:
            current_difficulty = request.form["difficulty"]
            guessed_words = []
        elif "word" in request.form:
            word = request.form["word"].upper()
            if word in clue_sets[current_difficulty]:
                if word not in guessed_words:
                    guessed_words.append(word)
        elif "reset" in request.form:
            guessed_words = []
    return render_template(
        "index.html",
        grid_layout=grid_layout,
        difficulty=current_difficulty,
        clues=clue_sets[current_difficulty],
        guessed_words=guessed_words
    )

if __name__ == "__main__":
    app.run(debug=True)