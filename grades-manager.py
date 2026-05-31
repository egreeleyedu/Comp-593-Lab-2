# Discussion Question 1:
# Why are tuples considered more secure than lists in some situations?
# They cannot be modified — they act as write-protected data structures.
# This prevents bugs caused by accidental changes to data that should remain constant.

# Discussion Question 2:
# Why is error handling important in security scripting?
# It prevents unexpected program crashes and allows code to gracefully recover from runtime failures.

# filters out students who are passing based on a grade threshold
def passing_students(students, grades):
    PASS = 80  # passing grade threshold
    passing = []  # empty list to store passing students
    for student, grade in zip(students, grades):  # loop through both lists at the same time
        if grade >= PASS:  # check if the student is passing
            passing.append(student)  # add passing student to the list
    return passing  # return the list of passing students

# generic display function, can print any list or tuple
def display(object):
    for item in object:  # loop through each element
        print(item)  # print each element on its own line

# calculates the average of a list of grades
def calculate_average(grades):
    total = 0  # start total at 0
    for grade in grades:  # loop through each grade
        total += grade  # add each grade to the total
    average = total / len(grades)  # divide total by number of grades
    return average  # return the average

# writes the student grades report to a text file
def save_report(students, grades):
    report_file = open("report.txt", "w")  # open file in write mode
    report_file.write("Student Grades Report\n")  # write header
    report_file.write("----------------------\n")  # write separator
    for i in range(len(students)):  # loop through each student
        report_file.write(students[i] + " : " + str(grades[i]) + "\n")  # write name and grade
    report_file.close()  # close the file when done
    print("\nReport file created successfully.")

# reads and prints the contents of the report file
def read_report():
    report_file = open("report.txt", "r")  # open file in read mode
    content = report_file.read()  # read entire file into a string
    print("\nReading Report File:")
    print(content)  # print the file contents
    report_file.close()  # close the file when done

def main():
    students = ["Ali", "Sara", "John", "David"]  # array with 4 elements
    grades = [85, 92, 78, 90]  # list of corresponding grades

    print(students)  # print the students list
    print(grades)  # print the grades list

    course_info = ("Scripting Application", "comp593", 2)  # tuple storing course info, cant be changed after creation

    print(f'The course information is : {course_info}')  # print tuple with f-string
    for student in students:  # loop through students list
        print(f'{student.capitalize()}')  # print each student name with f-string

    average_grade = calculate_average(grades)  # call calculate_average function
    print(f'Average grade: {average_grade}')  # print the result

    passing = passing_students(students, grades)  # get list of passing students
    print("Passing students:")
    display(passing)  # use display function to print each passing student

    # Part 3 - save and read report
    save_report(students, grades)  # save grades to report.txt
    read_report()  # read and print report.txt

    # Part 4 - error handling
    try:
        filename = input("Enter filename to read: ")  # get filename from user
        file = open(filename, "r")  # try to open the file
        print(file.read())  # print the file contents
        file.close()  # close the file
    except FileNotFoundError:  # catches the case where the file doesnt exist
        print("Error: File not found.")
    except Exception as e:  # catches any other unexpected errors
        print("Unexpected error:", e)

if __name__ == '__main__':
    main()
