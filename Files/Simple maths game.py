__author__ = 'Oskar'
import random

def high_score_system(score):
    with open("highScores.txt", "r") as file:
        read = file.read()
        read = int(read)
        if read == 0:
            file.close()
            with open("highScores.txt", "w") as file:
                print(score, file=file)
        elif read < score:
            file.close()
            with open("highScores.txt", "w") as file:
                print(score, file=file)

i = 0

while i < 10:
    print(round(random.random() * 100),)
    i += 1