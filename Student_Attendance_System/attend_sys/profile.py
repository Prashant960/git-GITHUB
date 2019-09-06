import os
import time
cls = lambda : os.system('clear')
class stu_op:
    sr = 0
    rno = 11001
    cls = lambda : os.system('clear')

    def __init__(self):
        self.file = '/home/anne/Desktop/Student_Attendance_System/attend_sys/stu_db.txt'
        self.file_m = '/home/anne/Desktop/Student_Attendance_System/attend_sys/stu_marks.txt'
        self.r_no = ''
        f = open(self.file,'r')
        f.readline()
        self.lt_db = [i.split('\n')[0].split('\t') for i in f]
        stu_op.sr = int(self.lt_db[-1][0])
        stu_op.rno = int(self.lt_db[-1][1])
#        self.lt_db = [i for i in self.temp_f if i[2] == r_no]
        f.close()

    def show_pro(self):
        cls()
        print('\n\t\t*****[ Profile Information ]*****')
        f = open(self.file,'r')
        lt = [i.split('\n')[0].split('\t') for i in f]
        for i in lt:
            if self.r_no in i:
                print(f'\n\t\t [   Roll No\t: {i[1]}   ]')
                print(f'\n\t\t [   Name\t: {i[2]}  ]')
                print(f'\n\t\t [   Gender\t: {i[3]}  ]')
                print(f'\n\t\t [   Mobile\t: {i[4]}   ]')
        f.close()
        time.sleep(4)
        
    def show_marks(self):
        cls()
        print('\n\t\t   *****[ Marks Information ]*****')
        f = open('/home/anne/Desktop/Student_Attendance_System/attend_sys/stu_marks.txt','r')
        print('\n\n\tRoll.no		sub1	sub2	sub3	sub4	sub5	total')
        for i in f:
            if self.r_no in i:
                print(f'\n\t{i}')

        f.close()
        time.sleep(4)

    def register(self):
        cls()
        print('\t\t-----[ Registration Page ]-----')
        name = input('\n\n\t\tFirst Name\t: ')
        gen = input('\t\tGender\t\t: ')
        mob = input('\t\tMobile\t\t: ')
        print('\t\tMarks :-')
        mm = list(int(input(f'\t\tSub_{i+1} :')) for i in range(5))
        tot = mm[0] + mm[1] + mm[2] + mm[3] + mm[4]
        aat = int(input('\t\tTotal attend\t: '))
        stu_op.sr += 1
        stu_op.rno += 1
        f = open(self.file,'a')
        fm = open(self.file_m,'a')
        f.write(f'{stu_op.sr}\t{stu_op.rno}\t{name}\t{gen}\t{mob}\t{tot}\t{aat}\t{(aat*100)/60}')
        fm.write(f'{stu_op.rno}\t\t{mm[0]}\t{mm[1]}\t{mm[2]}\t{mm[3]}\t{mm[4]}\t{tot}')
        f.close()
        fm.close()
        print(f'\n\t\t    [Your Roll_No : {stu_op.rno} ]\n\t\t[ Registration Successfull ]')
        time.sleep(2)


    def stu_portal(self):
        global cls
        rr = input('\n\t\tEnter Roll_no : ')
        for i in self.lt_db:
            if rr == i[1]:
                self.r_no = rr
                break
        else:
            print('\n\t\t[ Roll Number not found ]')
            return

        while True:
             cls()
             print('\n\t\t*********[ Welcome To Student Portal ]*********')
             print('\n\n\t\t   View Profile\t\t: 1')
             print('\t\t   View Marks\t\t: 2')
             print('\t\t   Logout\t\t: 3')
             a_ch = input('\n\t\t\t  Enter the Choice : ')
             if a_ch == '1':
                 self.show_pro()
             elif a_ch == '2':
                 self.show_marks()
             elif a_ch == '3':
                 break
             else:
                 print('\n\t\tWrong Choice, try again')
        cls()
        print('\n\n\t\t*********[ Logout ]*********')
        time.sleep(2)


#    def update_db(self):
#        cls()
#        print('\n\t\t *****[ Update Information ]*****')
#
#        print('\n\t\tUpdate Name\t: 1')
#        print('\t\tUpdate Gender\t: 2')
#        print('\t\tUpdate Mobile\t: 3')
#        chh = int(input('\n\n\t\t\tSelect Option : ' ))
#        if chh == 1:
#           self.temp_stu_db[4] = input('\n\n\t\tEnter new name : ')
#        elif chh == 2:
#            self.temp_stu_db[6] = int(input('\n\n\t\tEnter gender : '))
#        elif chh == 3:
#            self.temp_stu_db[8] = int(input('\n\n\t\tEnter new mobile no. : '))
#        else:
#            print('\n\n\t\tWrong choice, try again')
#
#        f = open(self.f_nm,
#        
#        print('\t\tSuccessfully Updated')
#        time.sleep(3)

