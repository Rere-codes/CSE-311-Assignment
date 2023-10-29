import tkinter as tk

def fahrenheit_to_celsius():
    fahrenheit = float(entry.get())
    celsius = (fahrenheit - 32) * 5/9
    result_label.config(text=f"{fahrenheit}°F is {celsius:.2f}°C")

def celsius_to_fahrenheit():
    celsius = float(entry.get())
    fahrenheit = (celsius * 9/5) + 32
    result_label.config(text=f"{celsius}°C is {fahrenheit:.2f}°F")

def celsius_to_kelvin():
    celsius = float(entry.get())
    kelvin = celsius + 273.15
    result_label.config(text=f"{celsius}°C is {kelvin:.2f}K")

def kelvin_to_celsius ():
    kelvin = float(entry.get())
    celsius = kelvin - 273.15
    result_label.config(text=f"{kelvin}K is {celsius:.2f}°C")

def fahrenheit_to_kelvin():
    fahrenheit = float(entry.get())
    kelvin = ((fahrenheit - 32) * 5/9) + 273.15
    result_label.config(text=f"{fahrenheit}°F is {kelvin:.2f}K")

def kelvin_to_fahrenheit ():
    kelvin = float(entry.get())
    fahrenheit = ((kelvin - 273.15) * 9/5) + 32
    result_label.config(text=f"{kelvin}K is {fahrenheit:.2f}°F")

def clear_result():
    result_label.config(text="")
    
def exit_app():
    app.destroy()

def edit():
    pass

# Function to toggle between dark mode and light mode
def toggle_mode():
    global dark_mode
    dark_mode = not dark_mode
    app.configure(bg="#2E2E2E" if dark_mode else "#E8E8E8")
    main_frame.configure(bg="#2E2E2E" if dark_mode else "#E8E8E8")
    entry_label.configure(bg="#DDDDDD" if dark_mode else "#E8E8E8")
    result_label.configure(bg="#2E2E2E" if dark_mode else "#E8E8E8")
    clear_button.configure(bg="#FF5733" if dark_mode else "#DDDDDD", fg="white" if dark_mode else "black")
    view_menu.entryconfig(0, label="Light Mode" if dark_mode else "Dark Mode")


# Create the main application window
app = tk.Tk()
app.title("Temperature Converter")

# Create a menu
menu = tk.Menu(app)
app.config(menu=menu)

# Create the file sub-menu
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=clear_result)
file_menu.add_command(label="Edit", command=edit)
file_menu.add_command(label="Exit", command=exit_app)

# Create the view menu for dark and light mode
view_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="View", menu=view_menu)
dark_mode = True  # Initial dark mode
view_menu.add_command(label="Light Mode", command=toggle_mode)


# Create the temperature conversion sub-menu
conversion_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Conversion", menu=conversion_menu)
conversion_menu.add_command(label="Fahrenheit to Celsius", command=fahrenheit_to_celsius)
conversion_menu.add_command(label="Celsius to Fahrenheit", command=celsius_to_fahrenheit)
conversion_menu.add_command(label="Celsius to Kelvin", command=celsius_to_kelvin)
conversion_menu.add_command(label="Kelvin to Celsius", command=kelvin_to_celsius)
conversion_menu.add_command(label="Fahrenheit to Kelvin", command=fahrenheit_to_kelvin)
conversion_menu.add_command(label="Kelvin to Fahrenheit", command=kelvin_to_fahrenheit)

# Create the main frame
main_frame = tk.Frame(app, padx=20, pady=20)
main_frame.pack()

# Create an entry for temperature input
entry_label = tk.Label(main_frame, text="Enter Temperature:")
entry_label.pack()
entry = tk.Entry(main_frame)
entry.pack()

# Create a label for displaying the result
result_label = tk.Label(main_frame, text="")
result_label.pack()

# Create a button to clear the result
clear_button = tk.Button(main_frame, text="Clear Result", command=clear_result)
clear_button.pack()

# Style the app
app.geometry("600x400")
app.configure(bg="#E8E8E8")
main_frame.configure(bg="#E8E8E8")
entry_label.configure(bg="#E8E8E8")
result_label.configure(bg="#E8E8E8")
clear_button.configure(bg="#FF5733", fg="white")

# Start the application
app.mainloop()
