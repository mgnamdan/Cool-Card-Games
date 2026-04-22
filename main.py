# ~~~~~ Class Imports, Imports, Helper Functions ~~~~~
from blackjackManager import BlackjackManager


# ~~~~~ MAIN DEFINTION ~~~~~
def main():

    BJGame = BlackjackManager()
    appOn = True

    while appOn:
        print("")
        print("~~~~ MENU ~~~~~")
        print("1. Blackjack")
        print("2. Quit")
        print("")
        print("Choose an option")
        userChoice = input(" --> ").lower()
        print("")

        if userChoice in ["1", "1.", "blackjack"]:
            BJGame.playGame()
        elif userChoice in ["2", "2.", "quit"]:
            appOn = False
        else:
            print("Invalid option - try again!")


# ~~~~~ MAIN CALL ~~~~~
if __name__ == "__main__":
    main()
