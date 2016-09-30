__author__ = 'Oskar'
"""
MathChallenge:
A game randomly creating and testing math sums with 4 operators: addition, subtraction, multiplication and division.
Difficulty levels are incremented after each correct answer.
No more than 3 incorrect answers are accepted.
"""

from random import randint, choice

class Math(object):
    """Class to generate different math sums based on operator and difficulty levels"""

    def __init__(self):
        """To initialise difficulty on each run"""
        self.difficulty = 1

    def addition(self, a, b):
        """To return 'addition', '+' sign , and answer of operation"""
        return ('addition', '+', a+b)

    def subtraction(self, a, b):
        """To return 'subtraction', '-' sign , and answer of operation"""
        return ('subtraction', '-', a-b)

    def multiplication(self, a, b):
        """To return 'multiplication', '*' sign , and answer of operation"""
        return ('multiplication', '*', a*b)

    def division(self, a, b):
        """To return 'division', '/' sign , and answer of operation"""
        return ('division', '/', a/b)

    def mathsum(self, difficulty):
        """Function that generates random operator and math sum checks against your answer"""

        print ("Difficulty level %d." % difficulty)

        #let's initialize some random digits for the sum
        a = randint(1,5)*difficulty
        b = randint(1,5)*difficulty

        #Now let's choose a random operator
        op = choice(self.operator)(a, b)

        print ("Now lets do a %s calculation and see how clever you are." % op[0])
        print ("So what is %d %s %d?" % (a, op[1], b))

        correct = False
        incorrect_count = 0                         #No more than 3 incorrect answers
        while not correct and incorrect_count<3:
            ans = int(input(">"))

            if ans == op[2]:
                correct = True
                print ("Correct!")
                self.difficulty += 1
                self.mathsum(self.difficulty)       #Restart the function with higher difficulty

            else:
                incorrect_count += 1
                if incorrect_count == 3: print ("That's 3 incorrect answers.  The end.")
                else:
                    print("That's not right.  Try again.")



class Engine(Math):
    """Game engine"""

    def __init__(self):
        """To initialise certain variables and function-lists"""

        #Initialise list of math functions inherited to randomly call from list
        self.operator = [
            self.addition,
            self.subtraction,
            self.multiplication,
            self.division
            ]

        #Initialise difficulty level
        self.difficulty = 1

        print ("Welcome to the MathChallenge game. I hope you enjoy!")

    def play(self):
        """To start game"""

        #start game
        self.mathsum(self.difficulty)

        #print returned difficulty level achieved
        print ("Difficulty level achieved: ", self.difficulty)


# Start game
game = Engine()
game.play()
