# ~~~~~ Class Imports, Imports, Helper Functions ~~~~~
from standardCard import Card
from standardDeck import Deck


# ~~~~~ MAIN DEFINTION ~~~~~
def main():
    # testCard1 = Card("Ace", "Diamonds")
    # testCard2 = Card()
    # testCard3 = Card("Two", "Clubs")

    # print(testCard1)
    # print(testCard1.rank)

    testDeck = Deck()

    testDeck.shuffle()
    print(len(testDeck.drawPile))
    print(testDeck)


# ~~~~~ MAIN CALL ~~~~~
if __name__ == "__main__":
    main()
