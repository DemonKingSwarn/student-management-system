import mysql.connector as mc

con = mc.connect(host='localhost', user='root', passwd='root', database='student')

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
    sql = 'select * from s1'
    c1 = con.cursor()
    c1.execute(sql)
    b = c1.fetchall()
    for i in b:
        print(i)

def updateStud():
    print('\nEnter student details you want to update...')
    a1 = input('Enter roll no.:' )
    a2 = input('Enter name: ')
    a3 = input('Enter father\'s name: ')
    a4 = input('Enter mother\'s name: ')
    a5 = input('Enter address: ')
    a6 = input('Enter phone no.: ')
    a7 = input('Enter email: ')

    data = (a1,a2,a3,a4,a5,a6,a7)
    sql = 'update s1 set Name = %s, FName = %s, MName = %s, Address = %s, Phone = %s, Email = %s where Rno = %s'
    c1 = con.cursor()
    c1.execute(sql,data)
    con.commit()
    print('\nData updated successfully...')

def deleteStud():
    print('\nEnter student roll no. you want to delete...')
    a1 = input('Enter Roll no.: ')

    data = (a1)
    sql = "delete from s1 where Rno = '%s'"
    c1 = con.cursor()
    c1.execute(sql,data)
    con.commit()
    print('\nData deleted successfully...')

def addStudExam():
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
