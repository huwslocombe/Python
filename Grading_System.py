#Program to store grades for pupils 

from statistics import mean as m

admins = {'User1':'Pass1','User2':'Pass2'} #This is a dictionary. All the users and their passwords are stored here

studentDict = {'Jeff':[78,88,93],
               'Louise':[89,91,83],
               'Jim':[75,67,55],
               'Susan':[61,59,58],
               'Alex':[59,71,68],
               'Marie':[70,78,80]}

def enterGrades():
    nameToEnter = input('Student name: ')
    gradeToEnter = input('Grade: ')

    if nameToEnter in studentDict:
        print('Adding grade...')
        studentDict[nameToEnter].append(int(gradeToEnter))
    else:
        print('Student does not exist!')

    print(studentDict)    

def removeStudent():
    nameToRemove = input('What student would you like to remove?: ')
    if nameToRemove in studentDict:
        print('Removing student...')
        del studentDict[nameToRemove]
        
    print(studentDict)

def studentAverages():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        averageGrade = m(gradeList)

        print(eachStudent,' has an average grade of: ', averageGrade)
def main():
    print("""

    Welcome to Grade Centre

          [1] - Enter Grade
          [2] - Remove student
          [3] - Student Average Grade
          [4] - Exit

    """)
    
    action = input('What would you like to do? (Enter a number) ')    

    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        studentAverages()
    elif action == '4':
        exit()
    else:
        print('No valid choice was given, please try again')

login = input('Username: ')
password = input('Password: ')

if login in admins:
    if admins[login] == password:
        print('Welcome, ',login)
        while True:
            main()
    else:
        print('Invalid password')
else:
    print('Invalid username')
