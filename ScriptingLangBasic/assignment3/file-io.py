"""

You are given a file in which the grades for the ‘scripting languages’ exam are stored. Download the
file ‘data.csv’ from the Pointcarre website. Each line in this file contains the information of 1 student
in the following format:NAME;firstname;classname;grade, sorted on NAME.

1. Write a function that reads the file and returns the data as a nested list. Each element in that
list is a list that contains the information of a student. Tip: you can use the function method
split(separator) to break up a string into a list of substrings (the parameter separator
determines how to split the string).

2. Write a function that looks up the grades of a student in the list created in question 1 and
returns it. Besides the list itself, this function is given a name and a first name and returns a
number (i.e. the grade of the student).

3. Write a function that can alter the grades of a certain student in the list and write a second
function that can store this list in a file.

4. Write a function that takes the list of question 1 as an argument and returns 6 different lists,
one per group (IA-A, IA-B, IR-A, IR-B, IR-C, IR-D).

"""

def readGradesFile(path):
    file = open(path, 'r')
    fileContent = []
    for line in file:
        #print(line)
        studentInfo = line.split(";")
        fileContent.append(studentInfo)
    return fileContent

def readStudentGrade(studentData, firstName, lastName):
    for student in studentData:
        if firstName == student[1] and lastName == student[0]:
            return student[3]
    return None

def alterGrade(studentData, firstName, lastName, newGrade):
    for student in studentData:
        if firstName == student[1] and lastName == student[0]:
            student[3] = newGrade
            return True
    return False

def saveData(studentData,path):
    f = open(path, 'w')
    for student in studentData:
        temp = student[0] + ";" + student[1] + ";" + student[2] + ";" + str(student[3]) + "\n"
        f.write(temp)
    f.close()

def groubByGrade(studentData):

    IAA = []
    IAB = []
    IRA = []
    IRB = []
    IRC = []
    IRD = []

    for student in studentData:
        if student[2] == "IA-A":
            IAA.append(student)
        if student[2] == "IA-B":
            IAB.append(student)
        if student[2] == "IR-A":
            IRA.append(student)
        if student[2] == "IR-B":
            IRB.append(student)
        if student[2] == "IR-C":
            IRC.append(student)
        if student[2] == "IR-D":
            IRD.append(student)

    return [IAA,IAB,IRA,IRB,IRC,IRD]

    
studentData = readGradesFile("data.csv")

studentGrade = readStudentGrade(studentData,"Ryan","VAN VOLSEM")

grouped = groubByGrade(studentData)

saveData(studentData,"output.txt")
