# This is a README file for blackjack-game

This is a simple Blackjack game that does not include a full deck of cards and treats each card with equal probability.

The game begins by dealing two visible cards to the player (face up), and two cards to the dealer. However, in the case of the dealer, one card is visible to other players while the other is hidden.

##Instructions
Run python blackjack.py in the interpreter

Press Y to start the game

Press H to  "hit" (draw another card from the deck), or "stand" which ends turn.

The player may hit any number of times. Should the total of the cards exceed 21, the player "busts" and loses the game to the dealer.

If the player reaches 21, the player stands.

The dealer's turn begins by revealing the hidden card

The dealer must hit if the total is 16 or less, and must stand if the value is 17 or more.

The dealer wins all ties (i.e. if both the dealer and the player reach 21, the dealer wins)

After each game press Y or N to start a new game.
