# Sukurti programą su grafine sąsaja, kuri:

# Turėtų laukelį su užrašu "Įveskite vardą", kuriame vartotojas galėtų įvesti vardą
# Turėtų mygtuką su užrašu "Patvirtinti", kurį nuspaudus, programa po lauku atspausdintų "Labas, {vardas}!"



from tkinter import Button, Entry, Label, Tk


def submit():
    user_input = field.get()
    print(user_input)
    result["text"] = (f'Sveikas {user_input}')

window =Tk()
window.geometry("450x200")
name = Label(window, text ="Enter a username")
button = Button(window, text = "Enter", command = submit)
field = Entry(window)
result = Label(window, text="")

def print3(event):
        print("you pressed ENTER")

button.bind("<Return>", lambda event: submit())


name.pack()
field.pack()
button.pack()
result.pack()

window.mainloop()

# Patobulinti 1 užduoties programą, kad ji:

# Atspausdintų pasisveikinimą ne tik nuspaudus mygtuką, bet ir paspaudus mygtuką "Enter"

