from guess import *

# Create game object
game = Guess(int(0), int(8))

# Intro / Setup
game.greeting()
game.randNum()

# Insert play game here.
game.runGame()

#exit the game
game.exitGame()
