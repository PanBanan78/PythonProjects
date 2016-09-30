__author__ = 'Oskar Matacz'


def grade_check(percentage):
    if totalPercentage < 4:
        return grades[0]
    elif percentage >= 4 and percentage < 13:
        return grades[4]
    elif percentage >= 13 and percentage < 22:
        return grades[13]
    elif percentage >= 22 and percentage < 31:
        return grades[22]
    elif percentage >= 31 and percentage < 41:
        return grades[31]
    elif percentage >= 41 and percentage < 54:
        return grades[41]
    elif percentage >= 54 and percentage < 67:
        return grades[54]
    elif percentage >= 67 and percentage < 80:
        return  grades[67]
    elif percentage >= 80:
        return grades[80]


analysis = int(input("Enter the marks for the analysis: "))
design = int(input("Enter the marks for the design: "))
implementation = int(input("Enter the marks for the implementation: "))
evaluation = int(input("Enter the marks for evaluation: "))

grades = {0: "U", 4: "G", 13: "F", 22: "E", 31: "D", 41: "C", 54: "B", 67: "A", 80: "A*"}

totalPercentage = analysis + design + implementation + evaluation

print("Your total score is:", totalPercentage)

print("Your grade is:", grade_check(totalPercentage))
