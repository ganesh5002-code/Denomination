from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Checking Your password")
window.configure(bg= 'light green')
window.geometry("400x400")

label = Label(window, text= "Enter your password to see how strong it is", bg= 'grey', fg= 'black', width= 35)
label.grid(row= 1, column= 1)
entry = Entry(window)
entry.grid(row = 1, column= 2)
result_label = Label(window, text= "The strength:")
result_label.grid(row= 4, column= 2)

def check():
   
    password = entry.get()
    messagebox.showerror("Error", "Please enter a valid password")
    length = len(password)
    
    if length <= 5:
        strength = "Weak"
        colour = "red"
    elif 6 <= length <=8:
        strength = "Medium"
        colour = "yellow"
    elif length > 8 and length <= 12:
        strength = "Strong"
        colour = "light green"
    elif length > 12:
        strength = "Very Strong"
        colour = "dark green"
    result_label.config(text= f"Strength: {strength}", fg= colour)
    

button = Button(text= "check", bg= 'light blue', fg= 'orange', command= check)
button.grid(row = 3, column= 2, sticky= 'ew', padx= 10, pady= 5)

window.mainloop()