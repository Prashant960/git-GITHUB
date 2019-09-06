from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import pymysql as p

win = Tk()
win.title("Inventry Management System")

win.geometry("%dx%d+%d+%d" % (900,500,900,500))
win.resizable(0,0)
win.config(bg="#6666ef")

#-----------------------------------------------variables
username = StringVar()
password = StringVar()
Pro_name = StringVar()
Pro_price = IntVar()
Pro_qty = IntVar()
search = StringVar()

#-----------------------------------------------mathods

def Database():
    global conn, cursor
    conn = p.connect("localhost","root","MySQL@123","inventory_db")
    cur = con.cursor()
    cur.execute("create table if not exists 'product' (productID int(5) PRIMARY KEY, productName varchar(30), purchasePrice int(6), salePrice decimal(8,2), productQty int(5))")
    cur.execute("create table if not exists 'sale' (saleid int(5),productID int(5), price decimal(8,2), date date, saleQty int(5), FOREIGN KEY ( productID ) REFERENCES product ( productID ))")

def exit():
    res = tkMessageBox.askquestion('Inventry Management System','Are you sure you want to exit?',icon="warning")
    if res == 'yes':
        win.destroy()
        exit()

def loginhome():
    global home
    home = Tk()
    home.title("Account login")
    win.geometry("%dx%d+%d+%d" % (900,500,900,500))
    win.resizable(0,0)
    win.config(bg="#6666ef")
    Title = Frame(home, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="Simple Inventory System", font=('arial', 45))
    lbl_display.pack()
    menubar = Menu(home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Manage Stock", command=manage_stock)
    filemenu.add_command(label="Sale", command=sale)
    filemenu.add_command(label="Manage Product", command=manage_product)
    filemenu.add_command(label="Profit Details", command=profit_detail)
    filemenu.add_command(label="exit", command=exit)
    menubar.add_cascade(label="Account", menu=filemenu)
    home.config(menu=menubar)

def manage_stock():
    pass

def sale():
    pass

def manage_product():
    pass

def profit_detail():
    pass


 
#---------------------------------------FRAME
Title = Frame(win, bd=1, relief=SOLID)
Title.pack(pady=10)

#---------------------------------------LABEL WIDGET
m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)
left = Label(m1, text="About Panel", font=('arial', 25))
m1.add(left)

m2 = PanedWindow(m1, orient = VERTICAL)
m1.add(m2)
top = Label(m2, text="Inventory Management System", font=('arial', 10))

bottom = Label(m2, text="Login Account", font=("arial",25))
m2.add(bottom)



#lbl_display.pack()



if __name__ == '__main__':
    win.mainloop()
