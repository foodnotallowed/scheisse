import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
lives = 6
chosen_word = random.choice(word_list)  # The random word that the program will choose.

print(stages[lives])

display = []  # The list where the guessed letters and blank spaces will be shown.

word_length = len(chosen_word)  # Since we're gonna use the length of the word a few times is conveniant to make it a
# variable :).
for blank in range(word_length):  # First, it adds as many blank spaces as letters the random word has.
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input('<<< ¿What letter are you choosing? >>>').lower()  # The letter the user wants to try.

    if guess in display:
        print(f"You've already chose {guess}")

    # Checks if the user's word is in the list. It repeats the same number of times than the length of the word.
    for position in range(word_length):

        # Letter will be equal to each one of the letters in the random word.
        letter = chosen_word[position]

        if letter == guess:  # If the letter is equal to one of the letters in the random word it replaces the blank.
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word")

        if lives == 0:
            end_of_game = True
            print("<<< YOU LOSE >>>")

        if "_" not in display:  # Checks if there are "_" remaining in the display.
            end_of_game = True
            print("<<< YOU WON >>>")

    print(stages[lives])
    print(display)
    print(f"You have {lives} lives remaining.\n ")

# Position represents the index of the letter in the word, for example the position of "c" in camel would be 0.
