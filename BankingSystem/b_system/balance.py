import os
import time
cls = lambda : os.system('clear')
def enquiry(data):
    global cls
    cls()
    print('\n\t\t*********[ Welcome To Enquiry Portal ]*********')
    print(f'\n\n\t\t\t Account Holder\t: {data[0]}')
    print(f'\t\t\t Age\t\t: {data[1]}')
    print(f'\t\t\t Mobile\t\t: {data[2]}')
    print(f'\n\n\t\t\t--[ Net Balance\t: {data[3]} ]--')
    time.sleep(6)
