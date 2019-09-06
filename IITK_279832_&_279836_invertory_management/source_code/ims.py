from im_system import *
import pymysql as p
import time
import os
cls = lambda : os.system('clear')

conn = p.connect("localhost","root","MySQL@123","inventory_db")
cur = conn.cursor()
cur.execute("create table if not exists product(productID int(5) PRIMARY KEY, productName varchar(30), purchasePrice int(6), salePrice decimal(8,2), productQty int(5))")
cur.execute("create table if not exists sale(saleid int(5),productID int(5), price decimal(8,2), date date, saleQty int(5), FOREIGN KEY (productID) REFERENCES product(productID))")

def admin_portal():
    global cls,logo
    cls()
    b_oper = {'1': manage.m_stock ,'2': manage.m_sale ,'3': manage.m_product ,'4': profit.details}
    while True:
        cls()
        logo()
        print('\n\t\t---[ USER_ID  : Admin ]---')
        print('\n\n\t\tManage Stock\t\t: 1 ')
        print('\t\tSale\t\t\t: 2')
        print('\t\tManage Product\t\t: 3')
        print('\t\tProfit Details\t\t: 4')
        print('\t\tLogout\t\t\t: 5')
        ch = input('\n\n\t\tChoose Option : ')
        if ch == '5':
            print('\n\t\t  -[You\'re logged out]-')
            return
        b_oper.get(ch, lambda: print('\n\n\t\tWrong Choice, try again'))()
        time.sleep(2)

if __name__ == '__main__':
    while True:
        cls()
        logo = lambda : os.system('toilet -f small " Inventory System " --filter border:metal')
        logo()
        print('\n\t\t ******[ Home Page ]******')
        print('\n\n\t\t    [ Login : l ]')
        print('\n\t\t    [ Exit : x ]')
        ch = input('\n\t\t    Choice : ')
        if ch == 'l':
            cls()
            logo()
            print('\n\t\t  *****[ LOGIN Portal ]*****')
            u_id = input('\n\t\t  Enter the UserID : ')
            if u_id == 'admin' and input('\t\t  Enter Password  : ') == '1234':
                admin_portal()
            else:
                print('\n\n\t\t Invalid UserID or Password')
        elif ch == 'x':
            break
        else:
            cls()
            print('\n\n\t\t\tWrong Choice, try again')
        
    cls()
    logo()
    print('\n\n\n\n\n')
    os.system('toilet -f small "    Have a nice day."')
    print('\n\n\n\n\n\n\n\n')
    time.sleep(3)
    cls()

