# Guess Number Version 2
Purpose:  Update the previous version of the game to include a class that handles the bulk of the heavy lifting allow me to keep the body of the program clean.  From this point I can quickly easily see the entry point, main body and exit with easy.

### Supported Operating Systems:<br/>
* Windows
* Linux
* MacOS

### Requirements:<br/>
* Have python installed [Here](https://www.python.org/) (right for new tab)

### Updates
* Created a class to handle all the heavy lifting
* Added a reset method
* Added scoring system
* Input validation for guesses
* Input validation for "do you wish to continue"
* created a versioning
* Omitted number validation as it is half handled by high low guesses
* Set all answers to "continue" to lower case to simplfy logic
* Restructured program for class configuration

### issues with the program as I see it
* Hard to read in its present form
* No input validation on, "Do you wish to play again"
* No input validation on "Guesses"
* Entering a string or char will crash the program in guess input
* Resetting the game needs to moved into a method
* Hard to see entry point of the program
* Fuctions declared over the main program (Hard to understand)
* No scoring system
