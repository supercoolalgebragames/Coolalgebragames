import random
import time

# Based on the PDF, these are the 6 categories
CATEGORIES = ["Term", "Expression", "Equation", "Inequality", "Formula", "Identity"]

# A list of 20+ "cards" as required
# This list provides the examples and their correct classification.
ALL_CARDS = [
    ("5x", "Term"),
    ("3x + 2y", "Expression"),
    ("y = 2x + 1", "Equation"),
    ("x > 5", "Inequality"),
    ("A = lw", "Formula"),
    ("(x+y)^2 = x^2 + 2xy + y^2", "Identity"),
    ("7y^2", "Term"),
    ("4a - b + c", "Expression"),
    ("5x - 3 = 12", "Equation"),
    ("y <= 2x - 1", "Inequality"),
    ("P = 2(l+w)", "Formula"),
    ("3(x+2) = 3x + 6", "Identity"),
    ("-8", "Term"),
    ("x^2 + 5", "Expression"),
    ("a^2 + b^2 = c^2", "Equation"),
    ("3x + 1 < 10", "Inequality"),
    ("d = rt", "Formula"),
    ("a+b = b+a", "Identity"),
    ("2(x+3)", "Expression"),
    ("2x = 10", "Equation"),
    ("F = ma", "Formula"),
    ("a >= b", "Inequality"),
    ("E = mc^2", "Formula"),
    ("z", "Term"),
]

def play_game():
    """
    This function runs the main game loop.
    It includes instructions, the sorting test, and final scoring.
    """

    # Instructions for play
    print("--- 🎮 Algebraic Vocabulary Sort 🎮 ---")
    print("\nWelcome! This game is based on the 'Algebra Sort' challenge.")
    print(f"You will be shown 10 algebraic examples, one by one.")
    print("Your job is to categorize each one as a:")

    # Display category options
    for i, category in enumerate(CATEGORIES, 1):
        print(f"  {i}. {category}")

    print("\nLet's see how fast you can sort them!")
    print("-------------------------------------------------")

    # Wait for user to start
    input("Press Enter to start the timer and begin...")
    print("\nTimer started! Here's your first card:\n")

    # Prepare the deck for this round
    random.shuffle(ALL_CARDS)
    # Draw 10 cards for the game
    game_deck = ALL_CARDS[:10]

    score = 0
    start_time = time.time() # Start the timer

    # Loop through the 10 chosen cards
    for i, (example, correct_category) in enumerate(game_deck, 1):
        print(f"\n--- Card {i} of 10 ---")
        print(f"Example:  ** {example} **")

        # Display category options again for clarity
        for j, category in enumerate(CATEGORIES, 1):
            print(f"  {j}. {category}")

        choice = 0
        # Loop to get valid user input
        while True:
            try:
                choice_input = input("Your choice (1-6): ")
                choice = int(choice_input)
                if 1 <= choice <= len(CATEGORIES):
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Check the answer
        user_category = CATEGORIES[choice - 1]

        if user_category == correct_category:
            print(f"✅ Correct! '{example}' is a(n) {correct_category}!")

play_game()
