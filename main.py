import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Variable to store the current display value
        self.display_value = tk.StringVar()
        self.display_value.set("")

        # Entry widget to display input and output
        self.display = tk.Entry(master, font=("Arial", 24), justify="right", textvariable=self.display_value, state="readonly")
        self.display.grid(row=0, column=0, columnspan=5, sticky="nsew")

        # Button texts and their grid positions
        button_texts = [
            ("%", 1, 0), ("CE", 1, 1), ("C", 1, 2), ("\u232B", 1, 3),
            ("1/x", 2, 0), ("x\u00b2", 2, 1), ("\u221a", 2, 2), ("/", 2, 3),
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("*", 3, 3),
            ("4", 4, 0), ("5", 4, 1), ("6", 4, 2), ("-", 4, 3),
            ("1", 5, 0), ("2", 5, 1), ("3", 5, 2), ("+", 5, 3),
            ("+/-", 6, 0), ("0", 6, 1), (".", 6, 2), ("=", 6, 3)
        ]

        # Create buttons
        for (text, row, column) in button_texts:
            if text == "=":
                button = tk.Button(master, text=text, font=("Arial", 18), width=3, height=1,
                                   command=lambda t=text: self.button_click(t), bg="#58A399")
            else:
                button = tk.Button(master, text=text, font=("Arial", 18), width=3, height=1,
                                   command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
            master.grid_rowconfigure(row, weight=1)
            master.grid_columnconfigure(column, weight=1)

    def button_click(self, value):
        current_display = self.display_value.get()

        if current_display == "Error":
            self.display_value.set("")
            current_display = ""

        if value == "=":
            try:
                result = eval(current_display)
                self.display_value.set(str(result))
            except:
                self.display_value.set("Error")
        elif value == "\u232B":  # Delete button
            self.display_value.set(current_display[:-1])
        elif value == "C":  # Clear button
            self.display_value.set("")
        elif value == "CE":  # Clear Entry button
            self.display_value.set("")
        elif value == "x\u00b2":  # Square button
            try:
                result = eval(current_display) ** 2
                self.display_value.set(str(result))
            except:
                self.display_value.set("Error")
        elif value == "\u221a":  # Square root button
            try:
                result = math.sqrt(eval(current_display))
                self.display_value.set(str(result))
            except:
                self.display_value.set("Error")
        elif value == "1/x":  # Inverse button
            try:
                result = 1 / eval(current_display)
                self.display_value.set(str(result))
            except:
                self.display_value.set("Error")
        elif value == "+/-":  # Sign change button
            if current_display and current_display[0] == "-":
                self.display_value.set(current_display[1:])
            else:
                self.display_value.set("-" + current_display)
        else:
            self.display_value.set(current_display + value)

# Create and run the calculator
root = tk.Tk()
calc = Calculator(root)
root.mainloop()
