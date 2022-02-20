# I'm proud of myself. Got it without hints. Yoooo <3. Andrés Montes sex000
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def blackjack():
    """The whole game"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    print(logo)

    def machine_new_card():
        """Chooses a random card from the list."""
        machine_card = random.choice(cards)
        return machine_card

    def user_new_card():
        """Chooses a random card from the list."""
        user_card = random.choice(cards)
        return user_card

    first_card = user_new_card()
    second_card = user_new_card()
    drawn_cards = [first_card, second_card]  # The cards the user has.

    pc_fcard = machine_new_card()
    pc_scard = machine_new_card()
    pc_drawn_cards = [pc_fcard, pc_scard]  # The cards the PC has.

    user_total = sum(drawn_cards)  # Sums the values of the cards to obtain the total :).
    print(f"These are your cards: {drawn_cards} // Total: {user_total}")

    pc_total = sum(pc_drawn_cards)
    print(f"Computer first card {pc_drawn_cards[0]}\n")

    # If pc_total is less than 17, it adds more cards.
    while pc_total < 17:
        pc_drawn_cards.append(machine_new_card())
        pc_total = sum(pc_drawn_cards)

    # Tells if the user wants another card.
    new = True
    while new:
        new = input("Do you want another card? yes/no ... ")

        # Adds new cards in case the user wants to.
        if new == "yes":
            drawn_cards.append(user_new_card())
            user_total = sum(drawn_cards)
            print(f"These are your cards: {drawn_cards} // Total: {user_total}\n")

            if user_total > 21:  # Checks if the user has more than 21 points.
                print(f"""You overpassed the 21 limit. You lose.
Your final score was {user_total}, computer score was {pc_total}""")
                new = False

        else:
            new = False
            print(f"Your final score was {user_total}, computer score was {pc_total}")

            if user_total == 21:
                print("You got a blackjack <<< you win >>>".upper())

            elif user_total > pc_total:
                print("\n <<< YOU WIN >>> ")

            elif user_total == pc_total:
                print("\n <<< IT'S A DRAW >>> ")

            elif pc_total > 21:
                print("\n <<< PC OVERPASSED THE LIMIT, YOU WIN >>> ")

            else:
                print("\n <<< YOU LOSE >>> ")


play = True
while play:

    play = input("\nDo you want to play a blackjack game? yes/no... ")
    if play == "yes":
        blackjack()
    else:
        play = False
