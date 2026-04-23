from standardDeck import Deck
from blackjackPlayers import *
from random import randint
from time import sleep


class BlackjackManager:

    COMPNAMES = ["Angela", "Chelsea", "Daryl", "Elizabeth", "Fred", "Gabby",
                 "Harold", "Irene", "Julie", "Katie", "Lindsey", "Mike",
                 "Nancy", "Oliver", "Pat", "Richard", "Samantha", "Terrence",
                 "Ursula", "Vic", "Wendy", "Xavier", "Yanni", "Zach"]

    def __init__(self):
        self.reset()


    # ~~~~~ SETUP METHODS ~~~~~
    def reset(self, humanName="Danny"):
        self.deck = Deck()
        self.dealer = BJPlayer()
        self.players = []
        self.players.append(HumanBJPlayer(humanName))
        self.deck.shuffle()


    def starterDeal(self):
        for _ in range(2):
            for player in self.players:
                player.drawCard(self.deck.drawCard())


    # ~~~~~ GAME FUNCTIONALITY METHODS ~~~~~
    def manageTurn(self, player):
        takingTurn = True
        while takingTurn:
            player.calcScore()
            if len(player.hand) >= 5 or player.giveScore() >= 21:
                takingTurn = False
            else:
                playerChoice = player.makeChoice()
                if playerChoice == "hit":
                    player.drawCard(self.deck.drawCard())
                else:
                    takingTurn = False


    def determineWinners(self):
        highScore = 0
        self.winners = []

        for player in self.players:
            playerScore = player.giveScore()
            print("")
            print("Debug Check 1:")
            print(f"Player: {str(player)}")
            print(f"Player score: {playerScore}")
            print(f"Previous high score: {highScore}")
            print("")
            if playerScore > highScore and playerScore <= 21:
                print("Check 2 triggered!\n")
                highScore = playerScore

        for player in self.players:
            if player.giveScore() == highScore:
                self.winners.append(player)

        if len(self.winners) == 0:
            print("Everybody busts! Nobody wins! :'(")
        elif len(self.winners) == 1:
            print(f"{self.winners[0]} wins with a score of {highScore}")
        else:
            if self.dealer in self.winners:
                print(f"{self.dealer} wins with a score of {highScore}")
            else:
                winnerString = ""
                for idx in range(len(self.winners)):
                    if idx == len(self.winners) - 1:
                        winnerString += str(self.winners[idx])
                    else:
                        winnerString += f"{str(self.winners[idx])}, "
                print(winnerString + f" tie with a score of {highScore}")



    def promptNextGame(self):
        print("Would you like to play another game of blackjack? (y/n)")
        playAgain = input(" --> ").lower()
        if playAgain in ['y', 'yes', 'sure', 'please']:
            return True
        else:
            return False


    # ~~~~~ GAME LOGIC ~~~~~
    def playGame(self):

        blackjackOn = True
        while blackjackOn:
            print("")
            print("Welcome to Blackjack!")
            print("")
            print("How many other computers would you like to play with?")
            extraOpps = int(input(" --> "))

            if extraOpps > 0:
                for _ in range(len(extraOpps)):
                    nameIdx = randint(0, len(self.COMPNAMES) - 1)
                    self.players.append(BJPlayer(self.COMPNAMES[nameIdx]))

            self.players.append(self.dealer)
            self.starterDeal()

            print("")
            print("Setting up game, one moment please...")
            sleep(1)

            for player in self.players:
                self.manageTurn(player)

            self.determineWinners()
            print("")
            blackjackOn = self.promptNextGame()
