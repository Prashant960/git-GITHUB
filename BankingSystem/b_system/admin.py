import os
import time
cls = lambda : os.system('clear')
def all_account(m_db):
    print('\n\n\t\t\t[ All Account Holders ]')
    print('\n\n|User_ID\t|A/c Holders\t|Age\t|Mobile\t\t|A/c Balance\n')
    for k, v in m_db.items():
        print(f'{k}\t{v[0]}\t\t{v[1]}\t{v[2]}\t\t{v[3]}')
    print('\n\n\t\t\t\tPowerby By Bank')
    time.sleep(7)

def delete_acc(m_db):
    dd = input('\n\t\t   Enter the UserID to delete : ')

    if dd in m_db.keys():
        print('\n\t ***[Remember : Once deleted, a/c cannot be recoverd.]***')
        if input('\n\t\t\tAre You Sure (y/n) : ') == 'y':
            del(m_db[dd])
            print('\n\n\t\t\t-[SUCCESSFULLY DELETED]-')
        else:
            print('\n\n\t\t\t- [Deletion Terminated] -')
    else:
        print('\n\t\t\tUserID not Available in Database.')

    time.sleep(3)
    return m_db


def bank_amt(m_db):
    tot = 0
    for i in m_db.values():
        tot = tot + i[-1]
    print(f'\n\n\t\t    --[ Total Cash in Bank : {tot} ]--')
    time.sleep(3)
         
def portal(meta_db):
    global cls
    while True:
        cls()
        print('\n\t\t*********[ Welcome To ADMIN Portal ]*********')
        print('\n\n\t\t   All Account details\t: 1')
        print('\t\t   Delete an Account\t: 2')
        print('\t\t   Net Amount in Bank\t: 3')
        print('\t\t   Logout\t\t: 4')
        a_ch = input('\n\t\t\t  Enter the Choice : ')
        if a_ch == '1':
            all_account(meta_db)
        elif a_ch == '2':
            meta_db = delete_acc(meta_db)
        elif a_ch == '3':
            bank_amt(meta_db)
        elif a_ch == '4':
            break
        else:
            print('\n\t\tWrong Choice, try again')
    cls()
    print('\n\n\t\t*********[ Admin Logout ]*********')
    time.sleep(2)
    return meta_db
