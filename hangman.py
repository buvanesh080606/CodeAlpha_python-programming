import random

# List of predefined words
words = ["apple", "banana", "orange", "grapes", "mango"]

# Choose a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("🎮 Welcome to Hangman Game!")

while wrong_guesses < max_wrong:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word.")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
    elif guess in word:
        print("✅ Good guess!")
        guessed_letters.append(guess)
    else:
        print("❌ Wrong guess!")
        guessed_letters.append(guess)
        wrong_guesses += 1

    print("Wrong guesses left:", max_wrong - wrong_guesses)

if wrong_guesses == max_wrong:
    print("\n💀 Game Over!")
    print("The word was:", word)
