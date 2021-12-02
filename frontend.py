from tkinter import *
import backend

# query functions


def view_clear():
    list1.delete(0, END)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)


def query_view():
    list1.delete(0, END)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)

    for row in backend.view():
        list1.insert(END, row)


def query_search():
    list1.delete(0, END)
    for row in backend.search(site.get(), email.get(), username.get(), password.get()):
        list1.insert(END, row)


def query_entry():
    backend.insert(site.get(), email.get(), username.get(), password.get())
    list1.delete(0, END)
    list1.insert(END, (site.get(), email.get(),
                 username.get(), password.get()))


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    entry1.delete(0, END)
    entry1.insert(END, selected_tuple[1])
    entry2.delete(0, END)
    entry2.insert(END, selected_tuple[2])
    entry3.delete(0, END)
    entry3.insert(END, selected_tuple[3])
    entry4.delete(0, END)
    entry4.insert(END, selected_tuple[4])


def query_delete():
    backend.delete(selected_tuple[0])
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def query_update():
    backend.update(selected_tuple[0], site.get(), email.get(),
                   username.get(), password.get())


window = Tk()
# lables
lable1 = Label(window, text="Website/ Program")
lable1.grid(row=0, column=0)

lable2 = Label(window, text="email ID")
lable2.grid(row=0, column=2)

lable3 = Label(window, text="Username")
lable3.grid(row=1, column=0)

lable4 = Label(window, text="Password")
lable4.grid(row=1, column=2)

# entries
site = StringVar()
entry1 = Entry(window, textvariable=site)
entry1.grid(row=0, column=1)

email = StringVar()
entry2 = Entry(window, textvariable=email)
entry2.grid(row=0, column=3)

username = StringVar()
entry3 = Entry(window, textvariable=username)
entry3.grid(row=1, column=1)

password = StringVar()
entry4 = Entry(window, textvariable=password)
entry4.grid(row=1, column=3)

# list
list1 = Listbox(window, height=8, width=42)
list1.grid(row=2, column=0, rowspan=6, columnspan=3)

# scrollbar
scrollbar1 = Scrollbar(window)
scrollbar1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=scrollbar1.set)
scrollbar1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)
# buttons
button1 = Button(window, text="View all", width=15, command=query_view)
button1.grid(row=2, column=3)

button2 = Button(window, text="Search entry", width=15, command=query_search)
button2.grid(row=3, column=3)

button3 = Button(window, text="Add entry", width=15, command=query_entry)
button3.grid(row=4, column=3)

button4 = Button(window, text="Update Selected",
                 width=15, command=query_update)
button4.grid(row=5, column=3)

button5 = Button(window, text="Delete selected",
                 width=15, command=query_delete)
button5.grid(row=6, column=3)

button6 = Button(window, text="Close", width=15, command=window.destroy)
button6.grid(row=8, column=3)

button7 = Button(window, text="Clear All", width=15, command=view_clear)
button7.grid(row=8, column=2)

window.wm_title("Password Manager")

window.mainloop()

# pyinstaller --onefile -windowed --icon=image.ico frontend.py
