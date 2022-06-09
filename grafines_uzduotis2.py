
from tkinter import *

def submit():
    user_input.set(field.get())
    print(user_input)
    result["text"] = f'Sveikas {user_input.get()}'

def delete():
    result["text"]= ""
    


def restore():
    result["text"] = f'Sveikas {user_input.get()}'

window = Tk()
user_input =StringVar()

window.geometry("300x80")

menu = Menu(window)
window.config(menu=menu)
submenu = Menu(menu, tearoff=0)

menu.add_cascade(label="menu", menu=submenu)
submenu.add_command(label = "Delete", command=delete)
submenu.add_command(label = "Restore", command=restore)
submenu.add_separator()
submenu.add_command(label="Exit")


submenu.add_command(label="First")
submenu.add_command(label="Second")


name = Label(window, text="Name")
field1 = Entry(window)
button = Button(window, text="Enter", command= "enter_name")
output = Label(window, text="")
window.bind("<Return>", lambda event: "enter_name"())
# button.pack()
name.grid(row=0, column=0, sticky=W)
field1.grid(row=0, column=1, sticky=W)
button.grid(row=0, column=2, sticky=W)
output.grid(row=1, column=1, sticky=W)


window.mainloop()


