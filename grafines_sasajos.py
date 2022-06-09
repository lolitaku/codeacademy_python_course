# from tkinter import Tk, Label

# # windows = Tk()
# # windows.title("test")
# # windows.geometry("250x200")
# # # uzrasas = Label(windows, text="Tiesiog tekstas")
# # # uzrasas.pack()

# # # windows.mainloop()

# # from tkinter import Checkbutton, Tk, Label, Frame, Button, Entry, E, N, S, W

# # window = Tk()

# # text1 = Label(window, text ="Name")
# # field1 = Entry(window)
# # text2 = Label(window, text="surname")
# # field2 = Entry(window)
# # chech_button = Checkbutton(window, text="Mark me please")

# # text1.grid(row=0, column=0, sticky=E)
# # field1.grid(row=0, column=1)
# # text2.grid(row=1, column=0, sticky=E)
# # field2.grid(row=1, column=1)
# # chech_button.grid(row=2, columnspan=4)

# # window.mainloop()

# # from tkinter import Tk, Button

# # window = Tk()
# # window.geometry("450x200")

# # def say_hello():
# #     print("hello")

# # Button1 = Button(window, text="say hi", command=say_hello)
# # Button1.pack()
# # window.mainloop()



# from tkinter import Tk, Button

# window = Tk()
# window.geometry("450x200")

# def print1(event):
#     print("you pressed left mouse button")

# def print2(event):
#     print("you pressed right mouse button")

# def print3(event):
#     print("you pressed ENTER")

# button = Button(window, text="PRESS ME", height=20, width=40)
# button.bind("<Button-1>", print1)
# button.bind("<Button-3>", print2)
# button.bind("<Return>", print3)

# button.pack()
# window.mainloop()


# from tkinter import Tk, Button

# window = Tk()
# window.geometry("450x430")

# def print1():
#     print("I am printing")

# button = Button(window, text="PRESS ME TO PRINT", command=print1)
# window.bind("<Return>", lambda event:print1())
# button.pack()

# window.mainloop()


# from tkinter import *

# window = Tk()

# def print1():
#     input1 = field1.get()
#     print(input1)
#     result["text"] = input1

# text1 = Label(window, text="Enter a word")
# field1 = Entry(window)
# button = Button(window, text="Enter", command=print1)
# result = Label(window, text="")

# text1.grid(row=0, column=0)
# field1.grid(row=0, column=1)
# button.grid(row=0, column=2)
# result.grid(row=1, columnspan=3)

# window.mainloop()


# from tkinter import *

# window = Tk()
# window.geometry("450x200")
# box = Listbox(window, width=20, height=50)
# list = range(1, 200)
# box.insert(END, *list)
# box.pack(side=LEFT)
# window.mainloop()



# from tkinter import Listbox, Tk, Scrollbar, END, RIGHT,
# langas = Tk()
# masyvas = range(1, 200)
# scrollbaras = Scrollbar(langas)
# boksas = Listbox(langas,
# yscrollcommand=scrollbaras.set)
# scrollbaras.config(command=boksas.yview)
# boksas.insert(END, *masyvas)
# scrollbaras.pack(side=RIGHT, fill=Y)
# boksas.pack(side=LEFT)
# langas.mainloop()



# from tkinter import *

# langas = Tk()
# sarasas = range(1, 200)

# def spausdinti():
#     pasirinkta = sarasas[boksas.curselection()[0]]
#     print(boksas.curselection())
#     uzrasas["text"] = pasirinkta

# mygtukas = Button(langas, text="Spausdinti",
# command=spausdinti)

# uzrasas = Label(langas, text="Nieko")
# boksas = Listbox(langas, selectmode=SINGLE)
# boksas.insert(END, *sarasas)
# boksas.pack(side=LEFT)
# mygtukas.pack()
# uzrasas.pack()
# langas.mainloop()


# from tkinter import *
# langas = Tk()

# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff = 0)
# submeniu2 = Menu(meniu, tearoff = 0)
# submeniu3 = Menu(meniu, tearoff = 0)

# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Pirmas")

# submeniu.add_command(label="Antras")
# submeniu.add_separator()
# submeniu.add_command(label="Trečias")

# meniu.add_cascade(label="Meniu 2",
# menu=submeniu2)
# submeniu2.add_command(label="1")
# submeniu2.add_command(label="2")

# meniu.add_cascade(label="Meniu 3",
# menu=submeniu3)

# langas.mainloop()


# class Person:
#     def __init__(self,name):
#         self.name = name

#     def __getattr__(self, attr):
#         return self.attr

# p1 = Person("vardas")
# print(p1.name)



# from tkinter import *
# langas = Tk()
# langas.geometry("450x200")

# def daryti():
#     status["text"] = "Dabar daro"

# mygtukas = Button(langas, text="Daryti", command=daryti)
# status = Label(langas, text="Nieko nedaro...", bd=1, relief=SUNKEN, anchor=W)
# # status.grid(row=2, columnspan=3, sticky=W + E)
# status.pack(side=BOTTOM, fill=X)

# mygtukas.pack()
# langas.mainloop()

# from tkinter import *
# import webbrowser

# def callback(url):
#     webbrowser.open_new(url)

# root = Tk()
# link1 = Label(root, text="Google Hyperlink", fg="blue", cursor="hand2")
# link1.pack()
# link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))

# link2 = Label(root, text="Ecosia Hyperlink", fg="blue", cursor="hand2")
# link2.pack()
# link2.bind("<Button-1>", lambda e: callback("http://www.ecosia.org"))

# root.mainloop()


# from tkinter import *
# from PIL import ImageTk, Image
# import os

# root = Tk()
# img = ImageTk.PhotoImage(Image.open("paveiksliukas.JPG"))
# panel = Label(root, image = img)
# panel.pack(side = "bottom", fill = "both", expand = "yes")
# root.mainloop()




# from tkinter import *
# import tkinter

# langas = Tk()

# kintamasis = StringVar()

# # kintamasis = ""

# def funkcija():
#     kintamasis.set("Naujas tekstas")
#     print(kintamasis.get())



# from tkinter import

# window = Tk()
# mano_tekstas = StringVar()

# def print1():
#     input1 = field1.get()
#     print(input1)
#     mano_tekstas.set(input1)
#     result["text"] = mano_tekstas.get()
#     print(mano_tekstas.get())

#     text1 = Label(window, text ="iveskite zodi")
#     field1 = Entry(window)
#     button = Button(window, twxt="iveskite zodi", command=print1)

#     text1.grid(row=0, column=0)
#     field1.grid(row=0, column=1)
#     button.grid(row=0, column=2)
#     result.grid(row=1, columnspan=3)

#     window.mainloop()


import tkinter as tk


class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
