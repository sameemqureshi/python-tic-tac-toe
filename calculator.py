import math
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        self.display = tk.Entry(master, width=30, font=("Helvetica", 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Buttons
        self.create_button("1", 1, 0)
        self.create_button("2", 1, 1)
        self.create_button("3", 1, 2)
        self.create_button("+", 1, 3)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("-", 2, 3)
        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)
        self.create_button("*", 3, 3)
        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("C", 4, 2)
        self.create_button("/", 4, 3)
        self.create_button("sqrt", 5, 0)
        self.create_button("x^2", 5, 1)
        self.create_button("x^y", 5, 2)
        self.create_button("=", 5, 3)

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, width=5, height=2, font=("Helvetica", 16), command=lambda: self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, text):
        if text == "C":
            self.display.delete(0, tk.END)
        elif text == "=":
            self.calculate()
        elif text == "sqrt":
            self.display.insert(tk.END, "sqrt(")
        elif text == "x^2":
            self.display.insert(tk.END, "**2")
        elif text == "x^y":
            self.display.insert(tk.END, "**")
        else:
            self.display.insert(tk.END, text)

    def calculate(self):
        try:
            expression = self.display.get()
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
