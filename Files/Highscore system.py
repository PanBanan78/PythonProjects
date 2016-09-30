__author__ = 'Oskar'

score = int(input("Enter a score: "))

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
