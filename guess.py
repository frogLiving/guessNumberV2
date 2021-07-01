from random import *
from os import system, name

class Guess:
    def __init__(self, high, low):
        """Class the guess my number game."""
        self.high = high
        self.low = low
        self.exit = False
        self.tries = int(0)
        self.number = int(0)
        self.score = int(0)
        self.guess = 0

    # Class methods (functions)
    def clearScreen(self):
        """Clears the screen."""
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def randNum(self):
        self.number = randint(1,101)

    def reset(self):
        self.tries = 0
        self.score = 0
        self.randNum()
        self.clearScreen()

    def exitGame(self):
        print("Thank you for playing...")

    def scoring(self):
        """Setup scoring for game completion."""
        if self.tries < 5:
            self.score += 100

        elif self.tries < 9:
            self.score += 50

        else:
            self.score += 25

    def enterGuess(self):
        """Collect Guess from user."""
        while(True):
            self.guess = input("Please enter your guess: ")
            
            if self.guess.isalpha():
                print("Please enter a number between 1 & 100")
            else:
                self.guess = int(self.guess)
                break

    def greeting(self):
        self.clearScreen()
        print(f"\tWelcome to\nGuess a random number Ver {self.high}.{self.low}")
        print("The number will be between 1 and 100.")

    def runGame(self):
        """Body of the game"""
        while(self.exit != True):
            self.enterGuess()
            self.tries += 1  
            if self.guess == self.number:
                self.score += 50
                self.scoring()
                print(f"\nCongrats for guess the number {self.number}")
                print(f"It took you {self.tries} tries to win.")                
                print(f"Score: {self.score}")     
                while(True):
                    ans = str(input("\nDo you wish to play again? (Y/N)"))

                    #Remove a check and covert to lower case
                    ans = ans.lower()

                    if ans == 'y':
                        self.reset()                        
                        break
                    elif ans == 'n':
                        self.exit = True
                        break
                    else:
                        print("Incorrect response.")

            elif self.guess < self.number:
                print("Guess to low.")
                
            else:
                print("Guess to high.")
