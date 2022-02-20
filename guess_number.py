import random
print("""<<< WELCOME TO THE NUMBER GUESSING GAME :)
I'M THINKING OF A NUMBER BETWEEN 1 AND 100 >>>\n""")

# To do: Count Lives

difficulty = input("Choose a difficulty. Easy/Hard... ")
numbers = []
lives = 0

for x in range(1, 101):
    numbers.append(x)  # Adds the numbers to the list.
guessed_number = random.choice(numbers)  # Chooses the random number between 1-100 from the list.

if difficulty.lower() == "easy":
    lives = 10
else:
    lives = 5

game_over = False

while not game_over:
    number = int(input("Make a guess... "))

    if number == guessed_number:
        print(f"{number} was the correct answer.")
        game_over = True
    elif lives == 0:
        print("You've run out of lives.")
        game_over = True
    elif number > guessed_number:
        lives -= 1
        print(f"{number} is too high.")
        print(f"You hacve {lives} remaining.")
    elif number < guessed_number:
        lives -= 1
        print(f"{number} is too low.")
        print(f"You have {lives} attempts>")
