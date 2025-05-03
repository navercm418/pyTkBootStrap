import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import StringVar

# Initialize the main application window
root = tb.Window(themename="cyborg")  # Change theme as needed

# Title and size
root.title("ttkbootstrap Showcase")
root.geometry("500x400")

# Label
label = tb.Label(root, text="Welcome to ttkbootstrap!", font=("Arial", 16))
label.pack(pady=10)

# Entry box with styled text variable
entry_var = StringVar()
entry = tb.Entry(root, textvariable=entry_var, bootstyle="success")
entry.pack(pady=5)

# Button that retrieves entry value
def show_entry():
    print(f"Entered text: {entry_var.get()}")

button = tb.Button(root, text="Submit", bootstyle="primary", command=show_entry)
button.pack(pady=5)

# Progress bar
progress = tb.Progressbar(root, bootstyle="info-striped", mode="determinate")
progress.pack(pady=5)
progress.start(10)

# Meter widget
meter = tb.Meter(root, bootstyle="warning", metersize=100, amountused=70)
meter.pack(pady=10)

# Toggle switch
toggle_var = StringVar()
toggle = tb.Checkbutton(root, text="Enable feature", bootstyle="success-round-toggle", variable=toggle_var)
toggle.pack(pady=10)

# Run the application
root.mainloop()
