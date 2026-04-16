# ~~~~~ Class Imports, Imports, Helper Functions ~~~~~
from standardCard import Card
from standardDeck import Deck
from blackjackPlayers import BJPlayer, HumanBJPlayer


# ~~~~~ MAIN DEFINTION ~~~~~
def main():

    testCard1 = Card("Ace", "Clubs")
    testCard2 = Card("Ace", "Hearts")
    testCard3 = Card("Ace", "Spades")
    testCard4 = Card("Ace", "Diamonds")
    testCard5 = Card("Ten", "Diamonds")
    testCard6 = Card("Eight", "Hearts")
    testPlayer = BJPlayer()
    testPlayer2 = HumanBJPlayer("Rob")

    testPlayer.drawCard(testCard1)
    testPlayer.drawCard(testCard2)
    testPlayer.drawCard(testCard3)
    testPlayer.drawCard(testCard4)
    testPlayer.drawCard(testCard6)

    testPlayer2.drawCard(testCard5)
    testPlayer2.drawCard(testCard3)

    choice = testPlayer2.makeChoice()
    print(f"You chose to {choice}!")


# ~~~~~ MAIN CALL ~~~~~
if __name__ == "__main__":
    main()
