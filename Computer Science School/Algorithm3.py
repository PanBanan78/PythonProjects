__author__ = 'Oskar Matacz'


def check_input(usr_input):
    if usr_input in ("Li", "Lithium"):
        print("Element:", group1["Li"][0])
        print("Atomic weight:", group1["Li"][1])
        print("Group: Alkali metals")
    elif usr_input in ("Na", "Sodium"):
        print("Element:", group1["Na"][0])
        print("Atomic weight:", group1["Na"][1])
        print("Group: Alkali metals")
    elif usr_input in ("K", "Potassium"):
        print("Element:", group1["K"][0])
        print("Atomic weight:", group1["K"][1])
        print("Group: Alkali metals")
    elif usr_input in ("Rb", "Rubidium"):
        print("Element:", group1["Rb"][0])
        print("Atomic weight:", group1["Rb"][1])
        print("Group: Alkali metals")
    elif usr_input in ("Cs", "Caesium"):
        print("Element:", group1["Cs"][0])
        print("Atomic weight:", group1["Cs"][1])
        print("Group: Alkali metals")
    elif usr_input in ("Fr", "Francium"):
        print("Element:", group1["Fr"][0])
        print("Atomic weight:", group1["Fr"][1])
        print("Group: Alkali metals")
    elif usr_input in ("Alkali metals", "Group 1"):
        print("Element:", group1["Li"][0])
        print("Atomic weight:", group1["Li"][1])
        print("Group: Alkali metals\n")
        print("Element:", group1["Na"][0])
        print("Atomic weight:", group1["Na"][1])
        print("Group: Alkali metals\n")
        print("Element:", group1["K"][0])
        print("Atomic weight:", group1["K"][1])
        print("Group: Alkali metals\n")
        print("Element:", group1["Rb"][0])
        print("Atomic weight:", group1["Rb"][1])
        print("Group: Alkali metals\n")
        print("Element:", group1["Cs"][0])
        print("Atomic weight:", group1["Cs"][1])
        print("Group: Alkali metals\n")
        print("Element:", group1["Fr"][0])
        print("Atomic weight:", group1["Fr"][1])
        print("Group: Alkali metals")
    elif usr_input in ("F", "Fluorine"):
        print("Element:", group7["F"][0])
        print("Atomic weight:", group7["F"][1])
        print("Group: Alkali metals")
    elif usr_input in ("Cl", "Chlorine"):
        print("Element:", group7["Cl"][0])
        print("Atomic weight:", group7["Cl"][1])
        print("Group: Alkali metals")
    elif usr_input in ("Br", "Bromine"):
        print("Element:", group7["Br"][0])
        print("Atomic weight:", group7["Br"][1])
        print("Group: Alkali metals")
    elif usr_input in ("I", "Iodine"):
        print("Element:", group7["I"][0])
        print("Atomic weight:", group7["I"][1])
        print("Group: Alkali metals")
    elif usr_input in ("At", "Astatine"):
        print("Element:", group7["At"][0])
        print("Atomic weight:", group7["At"][1])
        print("Group: Alkali metals")
    elif usr_input in ("Halogens", "Group 7"):
        print("Element:", group7["F"][0])
        print("Atomic weight:", group7["F"][1])
        print("Group: Halogens\n")
        print("Element:", group7["Cl"][0])
        print("Atomic weight:", group7["Cl"][1])
        print("Group: Halogens\n")
        print("Element:", group7["Br"][0])
        print("Atomic weight:", group7["Br"][1])
        print("Group: Halogens\n")
        print("Element:", group7["I"][0])
        print("Atomic weight:", group7["I"][1])
        print("Group: Halogens\n")
        print("Element:", group7["At"][0])
        print("Atomic weight:", group7["At"][1])
        print("Group: Alkali metals\n")

group1 = {
    "Li": ["Lithium", "7", "Group 1"],
    "Na": ["Sodium", "23", "Group 1"],
    "K": ["Potassium", "39", "Group 1"],
    "Rb": ["Rubidium", "85", "Group 1"],
    "Cs": ["Caesium", "133", "Group 1"],
    "Fr": ["Francium", "233", "Group 1"]
}

group7 = {
    "F": ["Fluorine", "19", "Group 7"],
    "Cl": ["Chlorine", "35.5", "Group 7"],
    "Br": ["Bromine", "80", "Group 7"],
    "I": ["Iodine", "127", "Group 7"],
    "At": ["Astatine", "210", "Group 7"]
}

print("This program will out the name, atomic weight and group of a certain \n"
      "it currently only works with elements in groups 1,2 and 7")
print("______________________________________________________________________\n")

userInput = input("Please enter the symbol or name of a element or a group name: ")
print("______________________________________________________________________\n")

check_input(userInput)