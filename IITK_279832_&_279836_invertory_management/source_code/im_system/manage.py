import os
import time
import pymysql as p

conn = p.connect("localhost","root","MySQL@123","inventory_db")
cur = conn.cursor()

cls = lambda : os.system('clear')
logo = lambda : os.system('toilet -f small " Inventory System " --filter border:metal')
def m_stock():
    global conn, cur, cls, logo
    while True:
        cls()
        logo()
        print('\n\t\t*********[ Stock Portal ]*********')
        print('\n\n\t\t[ Update Product Qty\t: 1 ]')
        print('\t\t[ View Stock\t\t: 2 ]')
        print('\t\t[ Exit\t\t\t: 3 ]')
        a_ch = input('\n\t\t\t  Enter the Choice : ')
        if a_ch == '1':
            try:
                pro_nm = input('\n\n\t\t Product Name : ')
                cur.execute(f'select productName from product where productName = "{pro_nm}"')
                ch = cur.fetchone()
            
                if ch[0] == pro_nm:
                    pro_qty = int(input('\n\n\t\t Add Quantity : '))
#                    cur.execute(f'select productQty from product where productName = "{pro_nm}"')
#                    r = cur.fetchone()
                    cur.execute(f'update product set productQty = productQty + {pro_qty} where productName = "{pro_nm}"')
                    print('\n\t\t[ Product Updated ]')
            except:
                print('\n\n\t\t[ Product not Found ]')
            time.sleep(2)
        elif a_ch == '2':
            cur.execute('select * from product, sale where product.productID = sale.productID')
            res = cur.fetchall()
            print('\nProduct_id\tProduct_name\tPurchase_price\tSale_price\tProduct_qty\tSale_id\t\tPrice\t\tdate\t\tSale_qty')
            for i in res:
                print(f'\n{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t{i[3]}\t{i[4]}\t\t{i[5]}\t\t{i[7]}\t{i[8]}\t{i[9]}')
            time.sleep(10)
        elif a_ch == '3':
            break
        else:
            print('\n\t\tWrong Choice, try again')
        conn.commit()
    cls()
    print('\n\n\t\t*********[ Portal Exit ]*********')
    time.sleep(2)


def m_product():
    global con, cur, cls, logo
    while True:
        cls()
        logo()
        print('\n\t\t*********[ Product Portal ]*********')
        print('\n\n\t\t [ Add New Product\t: 1 ]')
        print('\t\t [ View All Product\'s\t: 2 ]')
        print('\t\t [ Remove Product\t: 3 ]')
        print('\t\t [ Exit\t\t\t: 4 ]')
        a_ch = input('\n\t\t\t  Enter the Choice : ')
        if a_ch == '1':
            cls()
            logo()
            print('\n\t\t[ Add Product ]')
            pro_id = int(input('\n\t\tProduct ID : '))
            pro_nm = input('\n\t\tProduct Name : ')
            pur_pr = int(input('\n\t\tPurchase Price : '))
            sal_pr = float(input('\n\t\tSale Price : '))
            pro_qt = int(input('\n\t\tProduct Quantity : '))
            cur.execute(f'insert into product values({pro_id},"{pro_nm}",{pur_pr},{sal_pr},{pro_qt})')
            print('\n\t\t [ Inventory Updated ]')
            time.sleep(2)
        elif a_ch == '2':
            cur.execute('select * from product')
            res = cur.fetchall()
            print('\n\tProduct_ID\tProduct_Name\tPurchase_Price\tSale_Price\tProduct_Qty')
            for i in res:
                print(f'\n\t{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t{i[3]}\t\t{i[4]}')
            time.sleep(4)
        elif a_ch == '3':
            d_pro = input('\n\t\tProduct Name to Delete : ')
            cur.execute(f'select productName from product where productName = "{d_pro}"')
            ch = cur.fetchone()
            try:
                if ch[0] == d_pro:
                    cur.execute(f'delete from product where productName = "{d_pro}"')
                    print('\n\t\t [ Product Deleted]')
            except:
                print('\n\t\t[ Product Not Found ]')
            time.sleep(2)
        elif a_ch == '4':
            break
        else:
            print('\n\t\tWrong Choice, try again')
        conn.commit()
    cls()
    print('\n\n\t\t*********[ Portal Exit ]*********')
    time.sleep(2)

def m_sale():
    global con, cur, cls, logo
    while True:
        cls()
        logo()
        print('\n\t\t*********[ Sale Portal ]*********')
        print('\n\n\t\t [ Insert Product Sale Details\t: 1 ]')
        print('\t\t [ Update Product sale Details\t: 2 ]')
        print('\t\t [ View Product sale Details\t: 3 ]')
        print('\t\t [ Exit\t\t\t\t: 4 ]')
        a_ch = input('\n\t\t\t  Enter the Choice : ')
        if a_ch == '1':
            cls()
            logo()
            print('\n\t\t[ Add Sale Details ]')
            sal_id = int(input('\n\t\tSale ID : '))
            pro_id = input('\n\t\tProduct ID : ')
            pro_pr = int(input('\n\t\tPrice : '))
            dd = input('\n\t\tDate : ')
            sal_qt = int(input('\n\t\tSale Quantity : '))
            cur.execute(f'insert into sale values({sal_id},{pro_id},{pro_pr},"{dd}",{sal_qt})')
            cur.execute(f'update product set productQty = productQty - {sal_qt} where productID = {pro_id}')
            print('\n\t\t [ Inventory Updated ]')
            time.sleep(2)
        elif a_ch == '3':
            cur.execute('select * from sale')
            res = cur.fetchall()
            print('\n\tSale_ID\tProduct_ID\tPrice\t\tDate\t\tSale_Qty')
            for i in res:
                print(f'\n\t{i[0]}\t{i[1]}\t\t{i[2]}\t{i[3]}\t{i[4]}')
            time.sleep(4)
        elif a_ch == '2':
            cls()
            logo()
            print('\n\t\t[ Sale Detail Update ]')
            s_upd = int(input('\n\t\tSale_ID to update : '))
            cur.execute(f'select saleid from sale where saleid = {s_upd}')
            ch = cur.fetchone()
            try:
                if ch[0] == s_upd:
                    sl = float(input('\n\t\tSale Price : '))
                    sl_qt = int(input('\n\t\tSale Quantity : '))
#                    cur.execute(f'select saleQty from product where saleid = {s_upd}')
#                    r = cur.fetchone()
                    cur.execute(f'update sale SET saleQty=saleQty+{sl_qt}, price={sl} where saleid = {s_upd}')
#                    cur.execute(f'select * from product, sale where product.productID = sale.productID and saleid = {s_upd}')
#                    res = cur.fetchall()
                    cur.execute(f'update product, sale SET productQty = productQty - {sl_qt} where product.productID=sale.productID and saleid = {s_upd}')
                    print('\n\t\t[ Successfully Updated ]')
            except:
                print('\n\t\t[ Product Not Found ]')
        elif a_ch == '4':
            break
        else:
            print('\n\t\tWrong Choice, try again')
        time.sleep(2)
        conn.commit()
    cls()
    print('\n\n\t\t*********[ Portal Exit ]*********')
    time.sleep(2)
 
