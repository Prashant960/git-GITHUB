import os
import time
cls = lambda : os.system('clear')
def update(data):
    global cls
    cls()
    print('\n\t\t*********[ Welcome To Update Portal ]*********')
    print('\n\t\tUpdate Name\t: 1')
    print('\t\tUpdate Age\t: 2')
    print('\t\tUpdate Mobile\t: 3')
    chh = int(input('\n\n\t\t\tSelect Option : ' ))
    if chh == 1:
        data[0] = input('\n\n\t\tEnter new name : ')
    elif chh == 2:
        data[1] = int(input('\n\n\t\tEnter new age : '))
    elif chh == 3:
        data[2] = int(input('\n\n\t\tEnter new mobile no. : '))
    else:
        print('\n\n\t\tWrong choice, try again')

    print('\t\tSuccessfully Updated')
    time.sleep(6)
    return data
