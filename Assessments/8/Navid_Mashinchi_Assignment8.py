import mysql.connector

mydb = mysql.connector.connect(
 user='root',
 passwd='fortunad95',
 database='PDA',
 host='127.0.0.1',
 allow_local_infile='1')

myc = mydb.cursor()

# We use the PDA database that I have been working on throughout the quarter.
myc.execute("use PDA")

# Create a while loop so once the program is over it allows the user to get back to the start. If he user input is No the program will quit.
while True:

 # Ask the user if he/she would like to make any changes.
 userInput2 = str(input("Would you like to make any changes to the Employee: ")).lower()

 # If yes user will be asked what kind of changes he/she would like to do. Add, Delete or Edit.
 if userInput2 == "yes":

    userInput_Question = str(input("Would you like to Add,Delete or Edit an employee?: "))

    # If user says Edit he will be asked to enter the EmployeeID of the user so he is able to edit all the attributes of an employee.
    if userInput_Question == "Edit":
         userInput1 = int(input("Please enter an employee's EmployeeID: "))

         # Prints the Employee information.
         myc.execute("Select * From Employee E Where E.EmployeeID = %s", (userInput1,))
         for x in myc:
            print(x)

         # Asks user to specify which attribute to change. Options are below in userInput3 variable.
         userInput3 = str(input("Please enter the attribute you would like to change. Your choices are: EmployeeID, ESSN, Sex, Dob, Title, Fname,Lname, ProjectID: "))
         if userInput3 == "EmployeeID":
            userInput4 = int(input("Please enter the integer so the EmployeeID gets changed: "))
            myc.execute("Update Employee SET EmployeeID = %s Where Employee.EmployeeID = %s", (userInput4,userInput1,))
            print("Please see the update:")
            myc.execute("Select * From Employee E Where E.EmployeeID = %s", (userInput4,))
            for x in myc:
                print(x)
         elif userInput3 == "ESSN":
            userInput5 = int(input("Please enter the integer so the ESSN gets changed: "))
            myc.execute("Update Employee SET ESSN = %s Where Employee.EmployeeID = %s", (userInput5,userInput1,))
            print("Please see the update:")
            myc.execute("Select * From Employee E Where E.EmployeeID = %s", (userInput1,))
            for x in myc:
                print(x)
         elif userInput3 == "Sex":
            userInput6 = str(input("Please enter the gender so the Sex gets changed to M or F: "))
            myc.execute("Update Employee SET Sex = %s Where Employee.EmployeeID = %s", (userInput6,userInput1,))
            print("Please see the update:")
            myc.execute("Select * From Employee E Where E.EmployeeID = %s", (userInput1,))
            for x in myc:
                print(x)
         elif userInput3 == "Dob":
            userInput7 = str(input("Please enter the date so the date of birth gets changed: "))
            myc.execute("Update Employee SET Dob = %s Where Employee.EmployeeID = %s", (userInput7,userInput1,))
            print("Please see the update:")
            myc.execute("Select * From Employee E Where E.EmployeeID = %s", (userInput1,))
            for x in myc:
                print(x)
         elif userInput3 == "Title":
            userInput8 = str(input("Please enter the title so title gets changed: "))
            myc.execute("Update Employee SET Title = %s Where Employee.EmployeeID = %s", (userInput8,userInput1,))
            print("Please see the update:")
            myc.execute("Select * From Employee E Where E.EmployeeID = %s", (userInput1,))
            for x in myc:
                print(x)
         elif userInput3 == "Fname":
            userInput9 = str(input("Please enter the first name so it gets changed: "))
            myc.execute("Update Employee SET Fname = %s Where Employee.EmployeeID = %s", (userInput9,userInput1,))
            print("Please see the update:")
            myc.execute("Select * From Employee E Where E.EmployeeID = %s", (userInput1,))
            for x in myc:
                print(x)
         elif userInput3 == "Lname":
            userInput10 = str(input("Please enter the last name so it gets changed: "))
            myc.execute("Update Employee SET Lname = %s Where Employee.EmployeeID = %s", (userInput10,userInput1,))
            print("Please see the update:")
            myc.execute("Select * From Employee E Where E.EmployeeID = %s", (userInput1,))
            for x in myc:
                print(x)
         elif userInput3 == "ProjectID":
            userInput11 = int(input("Please enter the project id so it gets changed: "))
            myc.execute("Update Employee SET ProjectID = %s Where Employee.EmployeeID = %s", (userInput11,userInput1,))
            print("Please see the update:")
            myc.execute("Select * From Employee E Where E.EmployeeID = %s", (userInput1,))
            for x in myc:
                print(x)

    # If user says Add he will be able to add an employee. User will be asked to type in information of employee one by one.
    if userInput_Question == "Add":
         userInputAdd_1 = int(input("Please enter the EmployeeID: "))
         userInputAdd_2 = int(input("Please enter the 9 digit ESSN (Employee SSN): "))
         userInputAdd_3 = str(input("Please enter the Sex. Choices are M or F: "))
         userInputAdd_4 = str(input("Please enter the date of birth year-month-day: "))
         userInputAdd_5 = str(input("Please enter the title: "))
         userInputAdd_6 = str(input("Please enter the first name: "))
         userInputAdd_7 = str(input("Please enter the last name: "))
         userInputAdd_8 = int(input("Please enter the project id: "))
         myc.execute("Insert Into Employee Values (%s,%s,%s,%s,%s,%s,%s,%s)", (userInputAdd_1,userInputAdd_2,userInputAdd_3,userInputAdd_4,userInputAdd_5,userInputAdd_6,userInputAdd_7,userInputAdd_8,))
         print("Please see the update:")
         myc.execute("Select * From Employee E Where E.EmployeeID = %s", (userInputAdd_1,))
         for x in myc:
             print(x)

    # If user says Delete he will able to delete an employee by typing in the employee id.
    if userInput_Question == "Delete":
        userInputDelete_1 = int(input("Please enter the EmployeeID, so we delete the Employee: "))
        myc.execute("Delete From Employee E Where E.EmployeeID = %s", (userInputDelete_1,))
        print("Employee has been Deleted.")

 # User will be thanked to use the database and the while loop returns back to the top where it asks the user whether he would like to make any changes. If yes he/she can start again if no the program will quit.
 else:
    print("Thank you for using our database.")
    break

mydb.commit()
mydb.close()
