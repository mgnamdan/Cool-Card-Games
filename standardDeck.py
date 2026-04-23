from standardCard import Card
import random


class Deck:

    RANKS = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    SUITS = ["Clubs", "Hearts", "Spades", "Diamonds"]

    def __init__(self, numDecks=1):
        self.NUMDECKS = numDecks
        self.resetDeck()


    def resetDeck(self):
        self.drawPile = []
        self.discardPile = []
        self.outPile = []
        for _ in range(self.NUMDECKS):
            for suit in self.SUITS:
                for rank in self.RANKS:
                    newCard = Card(rank, suit)
                    self.drawPile.append(newCard)


    def __repr__(self):
        return f"Deck()"
    

    def __str__(self):
        return "\n".join(str(card) for card in self.drawPile)
        # return "A deck of standard cards"


    def shuffle(self):
        # random.shuffle(self.drawPile)

        # Bridge
        for _ in range(random.randint(3, 5)):
            midIdx = len(self.drawPile) // 2
            left = self.drawPile[:midIdx]
            right = self.drawPile[midIdx:]
            self.drawPile = []
            for cardIdx in range(len(left)):
                self.drawPile.append(left[cardIdx])
                self.drawPile.append(right[cardIdx])

        # Chunk
        for _ in range(random.randint(3, 5)):
            helperNumOne = len(self.drawPile) // 4
            upperRange = random.randint(helperNumOne, helperNumOne * 3)
            left = self.drawPile[:upperRange]
            right = self.drawPile[upperRange:]
            
            helperNumTwo = (len(right) // 4)
            rightSubOne = right[:helperNumTwo]
            rightSubTwo = right[helperNumTwo:(helperNumTwo*2)]
            rightSubThree = right[(helperNumTwo*2):(helperNumTwo*3)]
            rightSubFour = right[(helperNumTwo*3):]

            self.drawPile = [] + left + rightSubFour + rightSubThree + rightSubTwo + rightSubOne


    def drawCard(self):
        if len(self.drawPile) == 0:
            self.resetDeck()
        toGive = self.drawPile.pop(0)
        self.outPile.append(toGive)
        return toGive


    def discardCard(self, toDiscard):
        try:
            self.outPile.remove(toDiscard)
        except Exception:
            pass
        finally:
            self.discardPile.append(toDiscard)

        # if toDiscard in self.outPile:
        #     self.discardPile.append(toDiscard)
        #     self.outPile.remove(toDiscard)
