import os.path

def get_file_name():
    file_name = input("What is the name of the input file? ")
    while not os.path.isfile(file_name):
        print("That file does not exist!")
        file_name = input("What is the name of the input file? ")
    return file_name

def extract_grades(file_name):
    grades = []
    with open(file_name, 'r', errors='replace') as file:
        for line in file:
            line = line.rstrip()
            grade = ""
            for char in line:
                if char.isdigit():
                    grade += char
                elif grade:
                    break
            if grade:
                grades.append(int(grade))
    return grades

def display_statistics(grades):
    print("There are this many grades in the gradebook:", len(grades))
    print("The highest grade was a:", max(grades))
    print("The lowest grade was a:", min(grades))
    average = sum(grades) / len(grades)
    print("The average of the class was a:", round(average, 2))
    grades.sort()
    print("Here is a list of all the scores from low to high:", grades)

def main():
    all_grades = []
    continue_program = True

    while continue_program:
        file_name = get_file_name()
        new_grades = extract_grades(file_name)
        all_grades.extend(new_grades)
        display_statistics(all_grades)


        response = input("Do you want to add more grades through another input file? (yes to continue): ").strip().lower()
        continue_program = (response == "yes")

if __name__ == "__main__":
    main()


