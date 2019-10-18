#this class is to take attendance of student
import time
import random
import datetime
class student:
    def __init__(self):
        self.atd = {}
    def register(self, nm, rno):
        while len(self.atd) is not 5:
            name = random.choice(nm)
            if name in self.atd.values():
                continue
            self.atd[next(rno)] = name

class attendance(student):
    def display(self):
        show = lambda x,y: print(f'\t {x} : {y}')
        for x,y in self.atd.items():
            show(x,y)

        return
print('Registration started.....\nEnter the names :')
nms = [input() for _ in range(5)]
r_no =(x for x in range(10051,10056))

n = datetime.datetime.now()
print('\n\n\tAttendance\t\t\tDate : ',datetime.date(n.year,n.month,n.day))
#print(time.perf_counter())

#print('Attendance....')
mca = attendance()
mca.register(nms,r_no)
mca.display()
print('Attendance done.')
print('Programs Terminated')
