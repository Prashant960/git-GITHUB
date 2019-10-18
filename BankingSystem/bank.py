import os
#import datetime
from b_system import *
import time

#db = {'admin': '1234'}
db = {}
sr = 0
#B_date = lambda : print(f'Date/Time : {time.asctime()}')
def register():
    global db, sr, cls, dd_tt
    cls()
    print(f'\t\t-----[ Registration Page ]-----\n\t\tDate/Time : {dd_tt}')
    name = input('\n\n\t\tFirst Name\t: ')
    age = input('\t\tAge\t\t: ')
    mob = input('\t\tMobile\t\t: ')
    amt = int(input('\t\tDepositing amt\t: '))
    sr += 1
    db[name+age+'_'+str(sr)] = [name,age,mob,amt]
    print('\n\t\t    [ Account Created ]')
    print('\n\t\t  Your USERID : ',name+age+'_'+str(sr))

def login():
    global cls, db, dd_tt
    cls()
    b_oper = {'1': update.update ,'2': balance.enquiry ,'3': cash.withdraw ,'4': cash.deposite}
    print(f'\n\t\t*****[ LOGIN Portal ]*****\n\t\tDate/Time : {dd_tt}')
    u_id = input('\n\t\tEnter the UserID : ')
    if u_id == 'admin' and input('\t\tEnter Password  : ') == '1234':
        db = admin.portal(db)
        print()
    elif u_id in db.keys():
        while True:
            cls()
            print(f'\n\t\t---[ USER_ID  : {u_id} ]---\n\n\t\tDate/Time : {dd_tt}')
            print('\n\n\t\tUpdate Information\t: 1 ')               
            print('\t\tBalance Enquiry\t\t: 2')
            print('\t\tCash Withdrawal\t\t: 3')
            print('\t\tCash Deposit\t\t: 4')
            print('\t\tLogout\t\t\t: 5')
            ch = input('\n\n\t\tChoose Option : ')

            b_oper.get(ch, lambda x: print())(db[u_id])
            if ch == '5':
                print('\n\t\t  -[You\'re logged out]-')
                break
#            elif ch not in '12345':
#                cls()
#                print('\t\tWrong Choice, try again.')
#            if ch == '1':
#                update.update(db[u_id])
#            elif ch == '2':
#                balance.enquiry(db[u_id])
#            elif ch == '3':
#                cash.withdraw(db[u_id])
#            elif ch == '4':
#                cash.deposite(db[u_id])
#            elif ch == '5':
#                break
#            else:
#                cls()
#                print('\t\tWrong Choice, try again')
    else:
        print('\n\n\t\tUser Not Available, try again.')

print('\t\tLoading..............')
conti = ''
cls = lambda : os.system('clear')
dd_tt = time.asctime()
while True:
    cls()
    print(f'\t\t*************[ Welcome to Bank ]*************\n\n\t\tDate/Time : {dd_tt}\n')
    print('\t\tRegistration : r\t\tLogIN : l')
    ch = input('\n\t\t\t\tChoice : ')
    if ch == 'r':
        register()
    elif ch == 'l':
        login()
    else:
        cls()
        print('\n\n\t\t\tWrong Choice, try again')

    conti = input('\n\n\t\tDo you want to continue (y/n) : ')
    if conti == 'n':
        break
cls()
print('\t\tExit Banking Portal.\n\t\tHave a nice day.')
