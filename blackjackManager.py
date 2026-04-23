from standardDeck import Deck
from blackjackPlayers import *
from random import randint


class BlackjackManager:

    COMPNAMES = ["Angela", "Chelsea", "Daryl", "Elizabeth", "Fred", "Gabby",
                 "Harold", "Irene", "Julie", "Katie", "Lindsey", "Mike",
                 "Nancy", "Oliver", "Pat", "Richard", "Samantha", "Terrence",
                 "Ursula", "Vic", "Wendy", "Xavier", "Yanni", "Zach"]

    def __init__(self):
        self.reset()


    # ~~~~~ SETUP METHODS ~~~~~
    def reset(self, humanName="Danny", extraOpps=0):
        self.deck = Deck()
        self.dealer = BJPlayer()
        self.players = []
        self.players.append(HumanBJPlayer(humanName))
        if extraOpps > 0:
            for _ in range(len(extraOpps)):
                nameIdx = randint(0, len(self.COMPNAMES) - 1)
                self.players.append(BJPlayer(self.COMPNAMES[nameIdx]))
        self.deck.shuffle()
        self.starterDeal()


    def starterDeal(self):
        for _ in range(2):
            self.dealer.drawCard(self.deck.drawCard())
            for player in self.players:
                player.drawCard(self.deck.drawCard())


    # ~~~~~ GAME FUNCTIONALITY METHODS ~~~~~
    def calculateScore(self):
        pass


    def promptNextGame(self):
        pass


    def manageTurn(self):
        pass


    def determineWinners(self):
        pass


    # ~~~~~ GAME LOGIC ~~~~~
    def playGame(self):
        pass
    