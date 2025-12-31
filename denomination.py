from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("Denomination calculator")
window.configure(bg= "Light Green")
window.geometry('600x600')

uploaded_image = Image.open("download (2).jpg")
uploaded_image = uploaded_image.resize((400, 400))
image = ImageTk.PhotoImage(uploaded_image)
image_label = Label(window, image= image, bg= "#15EB7C")
image_label.place(x=50, y=50)

label1 = Label(window, text= "Welcome to our Denomination Counter Application", bg= 'light blue')
label1.place(relx= 0.5, y= 470, anchor= CENTER)

def message():
    msgbox = messagebox.showinfo("Alert", "Are you sure you want to proceed")
    if msgbox == 'ok':
        topwin()

button = Button(window, text= "Let's get started", command= message, bg= "#1BA3E7")
button.place(x= 200, y= 500, anchor= CENTER)

def topwin():
    top = Toplevel()
    top.title("Notes")
    top.configure('light blue')
    top.geometry('400x400+50+50')
    
    label = Label(top, text= "Enter amount")
    entry = Entry(top)

    label1 = Label(top, text= "2000", bg= 'light grey')
    label2 = Label(top, text= "500", bg= 'light grey')
    label3 = Label(top, text= "100", bg= 'light grey')
    
    Entry1= Entry(top)
    Entry2= Entry(top)
    Entry3= Entry(top)

    def calculate():
        try:
            
            global amount
            amount = int(entry.get())
            note2000 = amount //2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            Entry1.delete(0, END)
            Entry2.delete(0, END)
            Entry3.delete(0, END)

            Entry1.insert(END, str(note2000))
            Entry2.insert(END, str(note500))
            Entry3.insert(END, str(note100))

        except ValueError:
            messagebox.showerror("Error", "Enter a valid number")
          

    button = Button(top, text= "Calculate", command= calculate)
    top.mainloop()

window.mainloop()











