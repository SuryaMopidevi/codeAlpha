# initialising dictionary for collecting data
studentGrade={}
def avgCalc(grade):
    if grade == 'O' :
        return 10
    elif grade == 'A' :
        return 9
    elif grade == 'B' :
        return 8
    elif grade == 'C' :
        return 7
    elif grade == 'D' :
        return 6
    elif grade == 'P':
        return 5 
    else :
        return 4 

# adding student details 
def addStudentGrade():
    name=input("Enter Student name : ").lower()
    print("Enter grades (O/A/B/C/D/P/F) only \n")
    Python=input("Enter Python Grade : ").upper()
    SQL=input("Enter SQL Grade : ").upper()
    Django=input("Enter Django Grade : ").upper()
    studentGrade[name]={
        'Python': Python,
        'SQL': SQL,
        'Django': Django
    }
    print(f"{name} is added to student's list")

# viewing student details 
def viewStudentGrade():
    if not studentGrade:
        print("student's list is empty ")
    else:
        for name in studentGrade.keys():
            avg=0
            print(f"{name} student details : ")
            print(studentGrade[name])
            for sub in studentGrade[name]:
                avg+=avgCalc(studentGrade[name][sub])
            print("Average : ",avg/3)
            


print("welcome to studentGrade management system ")
while(True):
    print("a.Add studentGrade")
    print("v.View studentGrade")
    print("press any other keys for Exit")
    
    # chooosing operation
    operation=input("Choose operation : ").lower()

    # checking the operation 
    if operation=='a' :
        addStudentGrade()
    elif operation == 'v' :
        viewStudentGrade()
    else :
        print("Invalid operation ")
        break
print("Thank you ! Have a good day ..... ")
