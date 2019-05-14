"""
Assignment 5 - Simple Black Jack Game.
"""
import random


def decoration_prgm():
    """
    This function is a header for the game
    """
    print("==========Welcome to BlackJack! ===========")


def card_dealer():
    """
    This function deals the card
    """
    card = random.randint(1, 10)

    return card


def card_counter(hand):
    """
    This function counts the cards in a hand
    """
    kount = 0
    for num_card in hand:
        kount = kount + num_card
    return kount



def hit_stand(hand, dealer_hand):
    """
    This function asks the usr to hit or stand card
    """
    hand.append(card_dealer())
    tmp_card = 0
    print(f"You are dealt a {hand[0]} and a {hand[1]} for a total"
          + f" of {card_counter(hand)}")
    print(f"The dealer is dealt a {dealer_hand[0]} and a hidden card")

    while True:
        usr_stand = get_choice()
        if  usr_stand.upper() == 'H':
            tmp_card = card_dealer()
            hand.append(tmp_card)
            if card_counter(hand) <= 21:
                print(f"You draw a {tmp_card} for a total of "
                      + f"{card_counter(hand)}")
            else:
                print(f"Bust: You draw a {tmp_card} for a total of "
                      + f"{card_counter(hand)}")
                break
            continue

        else:
            print("You stand.")
            tmp_card = card_dealer()
            dealer_hand.append(tmp_card)
            print(f"The dealers hidden card is {tmp_card} for a total "
                  + f"of {card_counter(dealer_hand)}")
            while True:
                if card_counter(dealer_hand) <= 16:
                    tmp_card = card_dealer()
                    dealer_hand.append(tmp_card)
                    print(f"The dealer draws a {tmp_card} for a total of "
                          + f"{card_counter(dealer_hand)}")
                    continue
                else:
                    if card_counter(dealer_hand) > 21:
                        print("You win! The dealer's total is: "
                              + f"{card_counter(dealer_hand)}")
                    elif card_counter(dealer_hand) >= card_counter(hand):
                        print("Dealer wins. The dealer's total is: "
                              +  f"{card_counter(dealer_hand)}. Your total"
                              + f" is: {card_counter(hand)} ")
                    else:
                        print("You win! The dealer's total is:  "
                              + f"{card_counter(dealer_hand)} and your total"
                              + f" is: {card_counter(hand)}")
                    break
                return
        return


def get_choice():
    """
    Returns a Hit or Stand choice
    """
    while True:
        usr_stand = input(str("Hit or Stand (h/s): "))
        if not valid_input(usr_stand):
            print("Invalid input")
            continue
        else:
            return usr_stand.upper()
        break


def valid_input(usr_stand):
    """
    Check for valid hit or stand command
    """
    if usr_stand.upper() == "H" or usr_stand.upper() == "S":
        return True
    else:
        return False


def main():
    """
    This is the main usr input function
    """

    while True:
        try:
            hand = []
            dealer_hand = []
            usr_start_game = input(str("Do you wish to start the game? (y/n)"))

            if usr_start_game.upper() == 'Y':
                hand.append(card_dealer())
                dealer_hand.append(card_dealer())
                hit_stand(hand, dealer_hand)

            elif usr_start_game.upper() == 'N':
                print("See you next time!")
                break
            else:
                print("Please enter a y or n")
        except ValueError:
            print("Unknown Error. Please try again.")
            continue


if __name__ == '__main__':
    decoration_prgm()
    main()
