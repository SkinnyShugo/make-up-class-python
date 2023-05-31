#Array -> sequential collections of elements with a fixed size, They are used to store multiple values of the same data type in a single variable
#Lists, Dict, Numpy arrays 

#Grades

grades = []

def add_grade():
    grade = float(input("Enter student's grade: "))
    grades.append(grade)
    print("You have added your student's grade!!!")

def display_grades():
    if len(grades) == 0:
        print("No grades found!!!")
    else:
        print("Student Grades: ")
        for grade in grades:
            print(grade)

def calculate_average():
    if len(grades) == 0:
        print("No grades found!!!")
    else:
        total = sum(grades)
        average =  total / len(grades) # sum(grades) / len(grades)
        print(f"Average grade is: {average}")

def find_highest_lowest_grades():
    if len(grades) == 0:
        print("No grades found!!!")
    else:
        highest = max(grades)
        lowest = min(grades)
        print(f"Highest grade is: {highest}")
        print(f"Lowest grade is: {lowest}")


def program():
    while True:
        print("\n Student Grade Tracker")
        print("1. Add Grade")
        print("2. Display Grades")
        print("3. Calculate Average Grade")
        print("4. Find the Highest and Lowest Grades")
        print("5. Exit")

        choice = input("Enter Your choice")

        if choice == "1":
            add_grade()
        elif choice == "2":
            display_grades()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            find_highest_lowest_grades()
        elif choice == "5":
            print("Exiting the System")
            break
        else:
            print("Invalid Choice, Please try again")

if __name__ == "__main__":
    program()
