#create UI with Python that prints "Hello, World!" when a button is clicked
import tkinter as tk
from tkinter import messagebox
def on_button_click():
    messagebox.showinfo("Greeting", "Hello, World!")
# Create the main window
root = tk.Tk()
root.title("Hello World App")

# Create a button and attach the click event
button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack(pady=20)
# Run the application
root.mainloop()