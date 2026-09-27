========== STUDENT MARKS & ATTENDANCE MANAGEMENT SYSTEM ============

1. OVERVIEW :
              This is a small program that keeps a student's marks and attendance in one place. You add a student,
              enter marks for three subjects (Python, Maths and English) along with the number of classes held and
                attended, and the program works out the total, the percentage, the grade, and whether the student meets
                   the 75% attendance requirement. The records can be saved to a CSV file, which opens directly in
                     Excel.



2. FEATURES :
              1. ADD STUDENT :  
                             Takes roll number, name and course. Marks and attendance start at 0.

2 STUDENT SEARCH : 
                Finds a student by roll number and shows the details.

3 UPDATE STUDENT : 
                 hanges the name and course of an existing student.

4 DELETE STUDENT : 
                Removes a student using the roll number.

5 ENTER MARKS AND ATTENDANCE : 
                            Python, Maths and English marks, classes held and classes attended.

6 SHOW RESULT : 
                Prints total, percentage, grade, attendance percentage and eligibility.

7 SAVE DATA TO CSV :
                    Writes all students to students.csv with the date of saving.

8 CHECK CSV FILE :
                    Tells whether students.csv exists yet.

9 EXIT : Ends the program.

3. HOW THE PROGRAM IS ORGANISED :
                                  Every student as adictonary with the key roll, name, course, python, maths, english, held, attendance.



                                   FILE: main.py
                                   PURPOSE: The whole programe

                                   FILE: students.CSV
                                   PUPOSE: create in the same folder  when choose  option 7.

4. TECHNOLOGIES AND TOOL USED:
                                 python 3
                                 CSV file handing
                                 vs code / python IDLE
                                 python modules: CSV, OS,datetime

5. INSTALLATION AND RUNNIG: 
                            Step 1; Install Python 3 on your computer.

                            Step 2; Download or clone the project.

                            Step 3; Open the project folder in VS Code or Terminal.

                            Step 4; Run the program
 
                            python student_manager.py

6. 5. TESTING INSTRUCTIONS:

                       Test the following features:
                        Add a student with roll number, name and course.
                        Search the student using the roll number.
                         Update the student's name or course.
                        Delete a student.
                        Enter marks and attendance.
                        Check the calculated percentage, grade and attendance status.
                        Save the data using the CSV option.
                        Check whether students.csv is created.