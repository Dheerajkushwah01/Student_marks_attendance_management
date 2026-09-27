import csv
import os
from datetime import datetime

students  =  []

#student management syestem
#====STUDENT MANEGMENT===
def add_student():                                    #Add a new student
    roll = input("enter roll no: " )                  #Take student detials from user
    name = input("enter student name: ")
    course = input("enter course: ")


    student = { "roll": roll,                        #Store student detials from user, student name ,course, 
               "name": name,                          #subject marks python, maths, english
               "course": course,
               "python": 0,
               "maths": 0,
               "english":0,
               "held": 0,                              #enter class held and attendance
               "attendance": 0}

    students.append(student)                           #Add student to the list
    print("!!student added successfuly!!")           #Display student add successfully

# search stuydent by there roll number , take roll no form user
# check student in the list or not
def search_student():                         
    roll = input("enter roll no: ")

    for student in students:
        if student["roll"]==roll:
            print("\nstudent found")
            print("roll no:", student["roll"]) 
            print("name:", student["name"])
            print("course:", student["course"]) 
            return student
        

    else:
        print("****student not found****")
        return None

# Updte student details 
def update_student():
    student = search_student()


    if student:
        student["name"]=input("enter new name: ")          #Enter new student name
        student["course"]=input("enter course: ")           #course name 
        print("****student update successfully****")        # Last show student update successfully

#Delete student by roll no
def delete_student():
    roll = input("enter roll no to delete  : ")

    for student in students:
        if  student["roll"] == roll:       #take roll number from user
            students.remove(student)

            print("student delet successfully!!!!")
            return

    print("student not found...")

#===ATTENDANCE AND MARKS===
#student marks and attendance
def enter_marks():
    student = search_student()

    if student:
        student["python"]= float(input("python marks: "))
        student["maths"]= float(input("maths marks:  "))
        student["english"] =float(input("english marks: "))
        student["held"]= int(input("class held: "))
        student["attendance"]= int(input("class attendance: "))
        print("marks and data saved..")

#calculate  student result
def calculate_result(student):
        
        total= (student["python"]+student["maths"]+student["english"])       #Calculate student marks
        percentage = total/3                                                   #calculate student percentage 
       

        if percentage >= 90:                               #percentage and grade
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

#check student attendance eligibility
        if student ["held"] > 0:
            attendance = (student["attendance"]/student["held"])*100
        else:
            attendance = 0
        if attendance >= 75:                #when student attendance >75 then student eligible
            status = "eligible"
        else:
            status = "shortage"              #when student attendance <75 then student not eligible

#enter student name, total, percentagte , grade, attendance, 
        print("\n=====RESULT=====")
        print("name:", student["name"])
        print("total:", total)
        print("percentage:", round(percentage, 2))
        print("grade:", grade)
        print("attendance:",round(attendance,2), "%")
        print("attendance student:", status)

#show student result , search student ,calculate and display result
def show_result():
    student = search_student()

    if student:
        calculate_result(student)
        
#===FILE MANAGEMENT===
#save student data in  cvs file , open csv file
def save_data():
    filename= "students.csv"
    with open(filename,"w",newline="") as file:      #open file in written mode
        writer = csv.writer(file)                    # creat a csv writer for write data
        #save every student data in csv file               
        writer.writerow(["roll", "name", "course", "python", "maths", "english", "classes held", "classes attendence", "date"])

        for student in students:
            writer.writerow([student["roll"],
                             student["name"],
                             student["course"],
                             student["python"],
                             student["maths"],
                            student["english"],
                            student["held"],
                            student["attendance"],
                            datetime.now().strftime("%d-%m-%Y")])      #save current date
        print("data saved in students.csv")                            

#check if csv file exists , check file availability , display file status
def check_file():
    if os.path.exists("students.csv"):                    #os.path.exists() check file exist or not
        print("csv file is available..")      
    else:
        print("csv file does not exist yet..")



# main menu 
#take choice from user
while True:


    print("\n ===============")
    print("STUDENT MARKS & ATTENDANCE ")
    print("==============")
    print("1. add student")                    #add the student
    print("2. search student")                  #search student
    print("3. update student")                 #Update student
    print("4. delete student")                  #delete student
    print("5. enter marks and attendance ")      #enter marks and attendance
    print("6. show result")                      #show result
    print("7. save data to csv")                  #save data in to the csv
    print("8. check csv file")                   #check csv file
    print("9. exit")                             #and las exit the program

#Enter your choice which choice you want
    choice = input("enter your choice: ") 

    if choice == "1":                        # in this procces you can search your choice
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        enter_marks()
    elif choice == "6":
        show_result()
    elif choice == "7":
        save_data()
    elif choice == "8":
        check_file()
    elif choice == "9":
        print("thankyou!!")
        break

    else:
        print("invalid choice.please try again.")         #Display invalid choice message