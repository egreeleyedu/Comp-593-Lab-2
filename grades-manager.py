# Why are tuples considered more secure than lists in some situations?
# They can not be modifiedd, they act as write-prtected data structures this prevents bugs caused by accidental changes to data that should remain constant


# Why is error handling important in security scripting?
# it prevents unexpected program crashes and allows code to gracefully recover from runtime failiures.

def passing_students(students,grades):
    PASS = 80
    passing = []
    for student, grade in zip(students, grades):
        if grade >= PASS:
            passing.append(student)
    return passing




#    for student, grade in zip(students, grades):
#        if grade >= 80:
#            passing.append(student)
#        else:
#            return
#        
#
#    return

def display(object):

    for _ in object: 
        print(_)

    return


def calculate_average(grades):
    total = 0
    for grade in grades:
        total += grade

    average = total/len(grades)

    return average


def main():
    
    students = ["Ali", "Sara", "John", "David"] #array with 4 elements
    grades = [85, 92, 78, 90]

   # print(students)
   # print(grades)

    course_info = ("Scripting Application", "comp593", 2)




    print(f'The course information is : {course_info}')

   # for student in students:
   #     print(f'{student.capitalize()}')

    average_grade = calculate_average(grades)
    passing = passing_students(students, grades)
    print("Passing students:")
    display(passing)

if __name__ == '__main__':
    main()
