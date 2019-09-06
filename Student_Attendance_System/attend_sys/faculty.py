import os
import time
cls = lambda : os.system('clear')
class faculty_op:
    def __init__(self):
        self.f_nm = '/home/anne/Desktop/Student_Attendance_System/attend_sys/stu_db.txt'

    def stu_data(self):
        print('\n\n\t\t\t[ STUDENTS DATABASE ]')
        try:
            with open(self.f_nm,'r') as f:
                for i in f:
                    print(i)
        except:
            print('\n\t\t[ Data File not Found ]')
        
        print('\n\n\t\t\tPower By College')
        time.sleep(7)

    def del_data(self):
        dd = input('\n\t\t Enter the ROLL.NO to delete : ')
        f = open(self.f_nm,'r')
        f_m = open('/home/anne/Desktop/Student_Attendance_System/attend_sys/stu_marks.txt','r')
        if dd in f.read():
            print('\n\t ******[Remember : Once deleted, data cannot be recovered.]***')
            if input('\n\t\t\tAre You Sure (y/n) : ') == 'y':
                f.seek(0)
                f_m.seek(0)

                f_list = []
                f_mlist = []

                for i in f:
                    if dd in i:
                        continue

                    if i is not []:
                        f_list.append(i)
                f.close()

                for j in f_m:
                    if dd in j:
                        continue

                    if i is not []:
                        f_mlist.append(j)
                f_m.close()

                fm = open('/home/anne/Desktop/Student_Attendance_System/attend_sys/stu_marks.txt','w')
                for j in f_mlist:
                    fm.write(j)
                fm.close()

                f = open(self.f_nm,'w')
                for i in f_list:
                    f.write(i)
                f.close()

                print('\n\n\t\t\t-[SUCCESSFULLY DELETED]-')
            else:
                print('\n\n\t\t\t- [Deletion Terminated] -')

        else:
            print('\n\t\t\tRoll.no not Available in Database.')
        time.sleep(3)

    def update_att(self):
        r_no = input('\n\t\tEnter the Roll.no to update : ')
        f = open(self.f_nm,'r')
        lt = []
        lt = [i.split('\n')[0].split('\t') for i in f]
        f.close()
        for t in lt:
            if t[1] == r_no:
                print(f'\n\t\t Current Attendence: {t[-2]}')
                t[-2] = input('\n\t\t New Attendance : ')
                t[-1] = str((int(t[-2])*100)/60)

        f = open(self.f_nm,'w')
        for i in lt:
            f.write('\t'.join(i))
            f.write('\n')
        f.close()
        print('\n\n\t\t\t-[SUCCESSFULLY UPDATED]-')
        time.sleep(2)

    def portal(self):
        global cls
        while True:
            cls()
            print('\n\t\t*********[ Welcome To Faculty Portal ]*********')
            print('\n\n\t\t   View Student Database\t: 1')
            print('\t\t   Delete Student Data\t\t: 2')
            print('\t\t   Update Attendance\t\t: 3')
            print('\t\t   Logout\t\t\t: 4')
            a_ch = input('\n\t\t\t  Enter the Choice : ')
            if a_ch == '1':
                self.stu_data()
            elif a_ch == '2':
                self.del_data()
            elif a_ch == '3':
                self.update_att()
            elif a_ch == '4':
                break
            else:
                print('\n\t\tWrong Choice, try again')
        cls()
        print('\n\n\t\t*********[ Faculty Logout ]*********')
        time.sleep(2)
