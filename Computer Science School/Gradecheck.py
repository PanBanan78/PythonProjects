__author__ = 'Oskar Matacz'

from time import sleep

def grade_check(total_score):
    if totalScore < 4:
        return grades[0]
    elif total_score >= 4 and total_score < 13:
        return grades[1]
    elif total_score >= 13 and total_score < 22:
        return grades[2]
    elif total_score >= 22 and total_score < 31:
        return grades[3]
    elif total_score >= 31 and total_score < 41:
        return grades[4]
    elif total_score >= 41 and total_score < 54:
        return grades[5]
    elif total_score >= 54 and total_score < 67:
        return grades[6]
    elif total_score >= 67 and total_score < 80:
        return grades[7]
    elif total_score >= 80:
        return grades[8]


#def next_grade_check(total_score, grade):


while True:
    analysis = input("Enter the marks for the analysis: ")
    design = input("Enter the marks for the design: ")
    implementation = input("Enter the marks for the implementation: ")
    evaluation = input("Enter the marks for evaluation: ")
    try:
        analysis = int(analysis)
        design = int(design)
        implementation = int(implementation)
        evaluation = int(evaluation)
        break
    except ValueError:
        print("One of the values entered is not a integer, please try again...")
        sleep(1)

#        0  1  2   3   4   5   6   7   8
score = [0, 4, 13, 22, 31, 41, 54, 67, 80]
#          0    1    2    3    4    5    6    7    8
grades = ["U", "G", "F", "E", "D", "C", "B", "A", "A*"]

totalScore = analysis + design + implementation + evaluation

print("Your total score is:", totalScore)

finalGrade = grade_check(totalScore)

print("Your grade is:", finalGrade)
