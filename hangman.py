import random

# List of predefined words
words = ["python", "apple", "computer", "school", "mobile"]

# Select a random word
word = random.choice(words)

# Create blanks for the word
guessed_word = ["_"] * len(word)

# Track letters already guessed
guessed_letters = set()

# Number of incorrect guesses allowed
attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Attempts left:", attempts)
    print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "None")

    guess = input("Enter a letter: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_word[i] = guess
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

# Final result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
