import tkinter as tk

def convert_temperature():
    try:
        fahrenheit = float(entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{fahrenheit}°F = {celsius:.2f}°C")
    except ValueError:
        result_label.config(text="Invalid input")

def clear_input():
    entry.delete(0, tk.END)
    result_label.config(text="")

def exit_app():
    window.destroy()

window = tk.Tk()
window.title("Temperature Converter")

# Styling
window.geometry("300x200")
window.configure(background="#f2f2f2")

frame = tk.Frame(window, bg="#d3d3d3")
frame.place(relx=0.5, rely=0.4, anchor="center")

label = tk.Label(frame, text="Enter Temperature (°F):", bg="#d3d3d3")
label.grid(row=0, column=0, padx=10)

entry = tk.Entry(frame)
entry.grid(row=0, column=1, padx=10)

convert_button = tk.Button(frame, text="Convert", command=convert_temperature, bg="#4caf50", fg="white")
convert_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(frame, text="", bg="#d3d3d3")
result_label.grid(row=2, column=0, columnspan=2)

clear_button = tk.Button(frame, text="Clear", command=clear_input, bg="#f44336", fg="white")
clear_button.grid(row=3, column=0, pady=10)

exit_button = tk.Button(frame, text="Exit", command=exit_app, bg="#2196F3", fg="white")
exit_button.grid(row=3, column=1, pady=10)

# Menu Bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=exit_app)

window.mainloop()