import os
import time
cls = lambda : os.system('clear')
def deposite(data):
    global cls
    cls()
    print('\n\t\t*********[ Welcome To Deposite Portal ]*********')
    amt = int(input('\n\n\t\t\tEnter the Amount to deposite\n\t\tAmount : '))
    data[3] = data[3] + amt
    print(f'\n\n\t\t\tUpdated Net Balance : {data[3]}')
    time.sleep(6)
    return data

def withdraw(data):
    global cls
    cls()
    print('\n\t\t*********[ Welcome To Withdraw Portal ]*********')
    amt = int(input('\n\n\t\t\tEnter the Amount to withdraw\n\t\tAmount : '))
    if data[3] == 0:
        print('\n\n\t\tYour Have Zero Balance')
    elif amt > data[3]:
        print('\n\n\t\t-[SORRY, You dont have sufficient balance to withdraw]-')
    else:
        data[3] = data[3] - amt
        print(f'\n\n\t\t\tPlease take your cash : {amt}\n\n\t\t\t Updated Net Balance : {data[3]}')
    time.sleep(6)
    return data
