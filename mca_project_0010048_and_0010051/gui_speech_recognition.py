from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser as wb
import speech_recognition as sr

def countdown():
    pop_up = Tk()
    pop_up.geometry("250x100")
    pop_up.title("Action")
    pop_up_label = Label(pop_up, text = " [ Speak as Pops_down ] ")
    pop_up_label.pack(padx=10,pady=10)
    pop_up.after(5000, pop_up.destroy)
    mainloop()

def error_call(msg = 'Internet connection lost.\nEstablish connection and Try again'):
    messagebox.showinfo('Failed',msg)

def openAbout():
    messagebox.showinfo('About', 'About App: \nThis software is a voice to text sample project.\n\n*[ Note: ] \nFor Better Experience use microphone.\n\nDeveloper :\n1)Neha Pandey(Front-End_Developer)\n2)Prashant Tiwari(Back-End_Developer)')
def openContact():
    messagebox.showinfo('Contacts', 'For any Feedback & Query contact us at : \n\n\t[ xyz123@gmail.com ]')
def clicked():
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        r1.adjust_for_ambient_noise(source, duration=3)
        messagebox.showinfo('Action', '[ SPEAK ]\n   &\nClick OK')
#        countdown()
        audio = r1.listen(source, timeout=5)
#        url = 'https://www.youtube.com/results?search_query={}'
        url = 'https://www.google.com/search?q={}'
        try:
            search_word = r1.recognize_google(audio)
            wb.get().open_new(url.format(search_word))
        except sr.UnknownValueError:
            error_call('Sorry your voice is not clear')
        except sr.RequestError:
            error_call()

        messagebox.showwarning('Alert','Internet Signal too weak.\nCheck your connection.')


def action_go1():
    wb.get().open_new("https://www.News18.com")
def action_go2():
    wb.get().open_new("https://www.sarkariresult.com")
def action_go3():
    wb.get().open_new("https://www.amazon.com")


root = Tk()
root.title("Universely Browser")
root.geometry("700x500")
root.maxsize(700,500)
root.minsize(700,500)
root.configure(background="white")

f1 = Frame(root, width=700, height=70, bg="white", borderwidth = 6, relief=SUNKEN)
f1.pack(side=TOP, pady=10,padx=10)

#   1)creating menubar
menu = Menu()
new_item = Menu(menu)
#   1.1)adding items
new_item.add_command(label='About', command=openAbout)
new_item.add_command(label='Contact',command=openContact)
new_item.add_command(label='Exit', command=root.quit)
menu.add_cascade(label='MENU', menu=new_item)
root.config(menu=menu)


#   2)for jpg images
logopic = Image.open("universally2.jpg")
logopic = logopic.resize((500, 200), Image.ANTIALIAS)
logophoto = ImageTk.PhotoImage(logopic)
logo = Label(f1, image = logophoto)
logo.pack()

#   3)creating the button
mic = Image.open("mic2.png")
mic = mic.resize((50, 50), Image.ANTIALIAS)
micphoto = ImageTk.PhotoImage(mic)
btn = Button(f1, image = micphoto, command=clicked)
btn.pack()

#   4)Creating labelframe
frame2 = LabelFrame(root,width=700, height=100, bg="white", text='Articals and Tags for you',
    relief=GROOVE)

lbl1 = Label(frame2, width=50, bg='SkyBlue2')
lbl1.pack(side=LEFT, pady=5, padx=5)

lbl2 = Label(frame2, width=50, bg='SkyBlue3')
lbl2.pack(side=LEFT, pady=5, padx=5)

lbl3 = Label(frame2, width=50, bg='SkyBlue4')
lbl3.pack(side=LEFT, pady=5, padx=5)

frame2.pack(padx=10, pady=10)
#
article1 = "[Latest News]\n\nLatest international news and\n national news\n with currently \nupdates here."
article2 = "[Job Search]\n\nFor latest jobs and services\n updates at state and\n central level and\n exam results here."
article3 = "[Shopping & Sales]\n\nOnline shopping for latest\n trendies and \nsales of latest fashion\n 2019"
l1 = Label(lbl1,text=article1)
l2 = Label(lbl2,text=article2)
l3 = Label(lbl3,text=article3)      #,font = "Arial 8 bold italic")#.grid(row=2,sticky='E', padx=5, pady=2)
       
l1.pack()
l2.pack()
l3.pack()


go1 = Button(lbl1, text = "[Go]", command=action_go1)
go2 = Button(lbl2, text = "[Go]", command=action_go2)
go3 = Button(lbl3, text = "[Go]", command=action_go3)
go1.pack()
go2.pack()
go3.pack()


root.mainloop()
