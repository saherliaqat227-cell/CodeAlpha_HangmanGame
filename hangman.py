import random


words = ["apple", "tiger", "chair", "robot", "plant"]


word = random.choice(words)

guessed_letters = []
wrong_attempts = 6

print(" Welcome to Hangman Game")

while wrong_attempts > 0:

    display_word = ""

    
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)

    
    if display_word == word:
        print("Congratulations! You guessed the word.")
        break

  
    guess = input("Enter a letter: ").lower()

 
    if len(guess) != 1:
        print(" Please enter only one letter.")
        continue

    
    if guess in guessed_letters:
        print(" You already guessed this letter.")

    elif guess in word:
        guessed_letters.append(guess)
        print("Correct Guess!")

    else:
        guessed_letters.append(guess)
        wrong_attempts -= 1
        print(" Wrong Guess!")
        print("Remaining Attempts:", wrong_attempts)


if wrong_attempts == 0:
    print("\ Game Over!")
    print("The correct word was:", word)