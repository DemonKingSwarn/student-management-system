import mysql.connector as mc

con = mc.connect(host='localhost', user='root', passwd='root')

def createDatabase():
    global con
    cursor=con.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS STUDENT")
    cursor.execute("USE STUDENT")
    cursor.execute("CREATE TABLE IF NOT EXISTS s1(Rno int, SName varchar(40), FName varchar(40), MName varchar(40), Address varchar(40), Phone int, Email varchar(40))")
    cursor.execute("CREATE TABLE IF NOT EXISTS s2(Rno int, SName varchar(40), Class varchar(40), Section varchar(40), TotalMarks int, Percentage int, Grade varchar(40))")

def Main_Menu():
    print('\n')
    print('*'*60)
    print('*** Welcome to Student Management System ***')
    print('1. Add new student details...')
    print('2. Display all student details...')
    print('3. Update student\'s details...')
    print('4. Delete student\'s details...')
    print(50*'=')
    print('5. Add new student\'s examination details...')
    print('6. Display all students examination details...')
    print('7. Update student\'s examination details...')
    print('8. Delete student\'s examination details...')
    print('9. Exit...')
    print(60*'*')

def addStud():
    global con
    a1 = input('Enter roll no.: ')
    a2 = input('Enter name: ')
    a3 = input('Enter father\'s name: ')
    a4 = input('Enter mother\'s name: ')
    a5 = input('Enter address: ')
    a6 = input('Enter phone no.: ')
    a7 = input('Enter email: ')

    data = (a1,a2,a3,a4,a5,a6,a7)
    sql = 'insert into s1 values(%s,%s,%s,%s,%s,%s,%s)'
    c1 = con.cursor()
    c1.execute(sql,data)
    con.commit()
    print('\nData entered successfully...')

def displayStud():
    global con
    sql = 'select * from s1'
    c1 = con.cursor()
    c1.execute(sql)
    b = c1.fetchall()
    for i in b:
        print(i)

def updateStud():
    global con
    print('\nEnter student details you want to update...')
    a1 = input('Enter roll no.:' )
    a2 = input('Enter name: ')
    a3 = input('Enter father\'s name: ')
    a4 = input('Enter mother\'s name: ')
    a5 = input('Enter address: ')
    a6 = input('Enter phone no.: ')
    a7 = input('Enter email: ')

    data = (a1,a2,a3,a4,a5,a6,a7)
    sql = 'update s1 set SName = %s, FName = %s, MName = %s, Address = %s, Phone = %s, Email = %s where Rno = %s'
    c1 = con.cursor()
    c1.execute(sql,data)
    con.commit()
    print('\nData updated successfully...')

def deleteStud():
    global con
    print('\nEnter student roll no. you want to delete...')
    a1 = input('Enter Roll no.: ')

    data = (a1)
    sql = "delete from s1 where Rno = '%s'"
    c1 = con.cursor()
    c1.execute(sql,data)
    con.commit()
    print('\nData deleted successfully...')

def addStudExam():
    global con
    a1 = input('Enter Roll no.: ')
    a2 = input('Enter name: ')
    a3 = input('Enter class: ')
    a4 = input('Enter section: ')
    a5 = input('Enter total marks (Out of 500): ')
    a6 = input('Enter percentage: ')
    a7 = input('Enter grade: ')

    data = (a1,a2,a3,a4,a5,a6,a7)
    sql = 'insert into s2 values(%s,%s,%s,%s,%s,%s,%s)'
    c1 = con.cursor()
    c1.execute(sql,data)
    con.commit()
    print('\nData entered successfully...')

def displayStudExam():
    global con
    sql = 'select * from s2'
    c1 = con.cursor()
    c1.execute(sql)
    b = c1.fetchall()
    for i in b:
        print(i)

def updateStudExam():
    global con
    print('\nEnter student details you want to update')
    a1 = input('Enter Roll no.: ')
    a2 = input('Enter name: ')
    a3 = input('Enter class: ')
    a4 = input('Enter section: ')
    a5 = input('Enter total marks (Out of 500): ')
    a6 = input('Enter percentage: ')
    a7 = input('Enter grade: ')

    data = (a1,a2,a3,a4,a5,a6,a7)
    sql = "update s2 set SName = %s, Class = %s, Section = %s, TotalMarks = %s, Percentage = %s, Grade = %s where Rno = '%s'"
    c1 = con.cursor()
    c1.execute(sql,data)
    con.commit()
    print('\nData updated successfully...')

def deleteStudExam():
    global con
    print('\nEnter student roll no. you want to delete')
    a1 = input('Enter Roll no.: ')

    data = (a1)
    sql = "delete from s2 where Rno = '%s'"
    c1 = con.cursor()
    c1.execute(sql,data)
    con.commit()
    print('\nData deleted successfully...')

createDatabase()

while True:
    Main_Menu()
    ch = input('Enter your choice: ')
    if ch == '1':
        addStud()
    elif ch == '2':
        displayStud()
    elif ch =='3':
        updateStud()
    elif ch == '4':
        deleteStud()
    elif ch == '5':
        addStudExam()
    elif ch == '6':
        displayStudExam()
    elif ch == '7':
        updateStudExam()
    elif ch == '8':
        deleteStudExam()
    elif ch == '9':
        break
    else:
        print('\n*** Enter a valid choice ***')
