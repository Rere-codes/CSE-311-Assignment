import tkinter as tk
window = tk.Tk()
window.title("Simple Tkinter Desktop App")
window.geometry("600x400")
newlabel = tk.Label(text="This is my first Tkinter App")
newlabel.grid(column=0,row=0)
window.mainloop()