import os
import pymysql as p
import time

cls = lambda : os.system('clear')
logo = lambda : os.system('toilet -f small " Inventory System " --filter border:metal')
conn = p.connect("localhost","root","MySQL@123","inventory_db")
cur = conn.cursor()

def details():
    global cls,logo,conn,cur
    cls()
    logo()
    net_profit = 0
    print('\n\t\t ******[ Profit Portal ]******')
    print('\n\tProduct_Name\tSale_Price\tPurchase_Price\tSale_Qty')
    cur.execute('select salePrice, purchasePrice, saleQty, productName from product, sale where product.productID = sale.productID')
    for i in cur.fetchall():
        print(f'\n\t{i[3]}\t\t{i[0]}\t{i[1]}\t\t{i[2]}')
        net_profit = net_profit + ((i[0]-i[1])*i[2])
    print(f'\n\n\t\t [ Net Profit : {net_profit} ]')
    conn.commit()
    time.sleep(5)
