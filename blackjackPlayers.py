from random import choice

class BJPlayer:

    CARDVALUES = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
                  "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

    def __init__(self, name="Bob"):
        self.name = name
        self.hand = []
        self.score = 0


    def __str__(self):
        return self.name
    

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        if other.name != self.name:
            return False
        if len(other.hand) != len(other.hand):
            return False
        for idx in range(len(self.hand)):
            if other.hand[idx] != self.hand[idx]:
                return False
        return True


    def showHand(self):
        print(f"~~~~~ {self.name}'s Hand ~~~~~")
        print("")
        if len(self.hand) > 0:
            for idx in range(len(self.hand)):
                print(f"{idx+1}. [{self.hand[idx]}]")
        else:
            print("No cards in hand")
        print("")


    # def showHand(self):
    #     print(f"~~~~~ {self.name}'s Hand ~~~~~")
    #     print("")
    #     if len(self.hand) > 0:
    #         print("1. [??? of ???]")
    #         for idx in range(1, len(self.hand)):
    #             print(f"{idx+1}. [{self.hand[idx]}]")
    #     else:
    #         print("No cards in hand")
    #     print("")


    def giveScore(self):
        return self.score


    def drawCard(self, drawnCard):
        self.hand.append(drawnCard)


    def discardCard(self, cardIdx):
        return self.hand.pop(cardIdx)
    

    def calcScore(self):
        self.score = 0
        aces = 0
        if len(self.hand) > 0:
            for card in self.hand:
                self.score += self.CARDVALUES[card.rank]
                if card.rank == "Ace":
                    aces += 1
            while self.score > 21 and aces > 0:
                aces -= 1
                self.score -= 10
        else:
            self.score = 0


    def makeChoice(self):
        self.calcScore()
        self.showHand()
        if self.score > 17:
            return "stay"
        else:
            return "hit"



class HumanBJPlayer(BJPlayer):

    def makeChoice(self):
        validChoice = False
        while not validChoice:
            print("")
            self.showHand()
            print("Would you like to hit or stay?")
            playerChoice = input(" --> ").lower()
            if playerChoice in ["hit", "h"]:
                return "hit"
            elif playerChoice in ["stay", "s"]:
                return "stay"
            else:
                print("That's not a valid choice - try again")
