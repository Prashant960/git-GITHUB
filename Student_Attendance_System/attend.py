import os
import time
import datetime
from attend_sys import *

class attend:
    cls = lambda : os.system('clear')
#    def __init__(self):
#        pass
    def student(self):
        while True:
            cls()
            print('\t\t*************[ Welcome to Student Portal ]*************')
            st = profile.stu_op()
            print('\t\tRegistration : r\t\tLogIN : l')
            ch = input('\n\t\t\t\tChoice : ')
            if ch == 'r':
                p = profile.stu_op()
                p.register()
            elif ch == 'l':
                p = profile.stu_op()
                p.stu_portal()
            else:
                cls()
                print('\n\n\t\t\tWrong Choice, try again')
            cls()
            conti = input('\n\n\t\tWanna continue to Student Portal (y/n) : ')
            if conti == 'n':
                break

    def faculty(self):
        cls()
        print('\t\t*************[ Welcome to Faculty Portal ]*************')
        adm = input('\n\t\t UserId : ')
        if adm == 'admin' and input('\n\t\t Password : ') == '12345':
            f = faculty.faculty_op()
            f.portal()
        else :
            print('\n\n\t\tWrong user_id or password. Try again.')

a = attend()
print('\n\t\tLoading'+'.'*20)
conti = ''
cls = lambda : os.system('clear')
while True:
    cls()
    print('\n\t\t'+'*'*5+'[ Welcome To Attendance System ]'+'*'*5)
    print('\n\t\t\t [ STUDENT\t: s ]')
    print('\n\t\t\t [ ADMIN\t: a ]')
    ch = input('\n\t\t\tEnter the choice : ')
    if ch == 's':
        a.student()
    elif ch == 'a':
        a.faculty()
    else:
        cls()
        print('\n\t\t\tWrong Choice, try again')
    cls()
    conti = input('\n\n\t\tWanna continue to Home Screen(y/n) : ')
    if conti == 'n':
        break

cls()
print('\n\t\tExit Attendance Portal.\n\t\tHave a vice day.') 
