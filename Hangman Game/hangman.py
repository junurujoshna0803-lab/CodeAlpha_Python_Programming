import random

# List of words
words = ["python", "computer", "program", "developer", "internship"]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses
incorrect_guesses = 0

# Maximum allowed incorrect guesses
max_guesses = 6

print("=" * 40)
print("🎮 WELCOME TO HANGMAN GAME 🎮")
print("=" * 40)
print("Guess the hidden word one letter at a time.")
print("You have 6 incorrect guesses.")
print("=" * 40)

while incorrect_guesses < max_guesses:

    display_word = ""

    # Display the guessed letters
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the player has guessed the word
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

    # Ask the user for a letter
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if the guess is correct
    if guess in secret_word:
        print("✅ Correct!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong!")
        print("Remaining Chances:", max_guesses - incorrect_guesses)

# If the player loses
if incorrect_guesses == max_guesses:
    print("\n💀 Game Over!")
    print("The correct word was:", secret_word)