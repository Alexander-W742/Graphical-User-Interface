import tkinter as tk
from tkinter import messagebox

# Event handler

def displayData():
    first = entFirst.get()
    last = entLast.get()
    email = entEmail.get()
    phone = entPhone.get()

    output = (f"First Name: {first}\nLast Name: {last}\nEmail: {email}\nPhone: {phone}")
    messagebox.showinfo("Submitted Information", output)

def clear():
    entFirst.delete(0, tk.END)
    entLast.delete(0, tk.END)
    entEmail.delete(0, tk.END)
    entPhone.delete(0, tk.END)

# main window

root = tk.Tk()
root.title("Assignment 3 - Tkinter GUI")
root.geometry("500x300")

# Labels and Entry

lblFirstPerson = tk.LabelFrame(root, text = "Person Information")
lblFirstPerson.pack(padx = 10, pady = 10, fill = "both", expand = True)

lblFirst = tk.Label(lblFirstPerson, text = "First Name: ", bg = "blue", fg = "white")
lblFirst.grid(column = 0, row = 0, sticky = "W", padx = 5, pady = 5)

entFirst = tk.Entry(lblFirstPerson)
entFirst.grid(column = 1, row = 0, padx = 5, pady = 5)

lblLast = tk.Label(lblFirstPerson, text = "Last Name: ", bg = "blue", fg = "white")
lblLast.grid(column = 0, row = 1, sticky = "W", padx = 5, pady = 5)

entLast = tk.Entry(lblFirstPerson)
entLast.grid(column = 1, row = 1, padx = 5, pady = 5)

lblEmail = tk.Label(lblFirstPerson, text = "Email: ")
lblEmail.grid(column = 0, row = 2, sticky = "W", padx = 5, pady = 5)

entEmail = tk.Entry(lblFirstPerson)
entEmail.grid(column = 1, row = 2, padx = 5, pady = 5)

lblPhone = tk.Label(lblFirstPerson, text = "Phone: ")
lblPhone.grid(column = 0, row = 3, sticky = "W", padx = 5, pady = 5)

entPhone = tk.Entry(lblFirstPerson)
entPhone.grid(column = 1, row = 3, padx = 5, pady = 5)

# Buttons

fraButtons = tk.Frame(root)
fraButtons.pack(pady = 10)

btnS = tk.Button(fraButtons, text = "Submit", width = 5, command = displayData)
btnS.pack(side = tk.LEFT, padx = 5)

btnR = tk.Button(fraButtons, text = "Reset", width = 5, command = clear)
btnR.pack(side = tk.LEFT, padx = 5)

btnQ = tk.Button(fraButtons, text = "Quit", width = 5, command = root.quit)
btnQ.pack(side = tk.LEFT, padx = 5)

# main loop

root.mainloop()