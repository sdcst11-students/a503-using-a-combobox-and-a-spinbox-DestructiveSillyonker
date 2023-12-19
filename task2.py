#!python3

"""
##### Task 2 Calculator
Create a simple app that allows you to do a calculation with an arithmetic operation.  You will need a spinbox between 2 entry boxes.  The entryboxes are where you should be entering your numbers, and the spinbox should be the operator.  You will need a button to do the calculation.  You can modify your assignment from A500 for this.
"""
import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.num1 = tk.StringVar()
        self.num2 = tk.StringVar()
        self.operator = tk.StringVar()
        self.result = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        entry_label1 = tk.Label(self.root, text="Number 1:")
        entry_label1.grid(row=0, column=0, padx=10, pady=10)
        entry_box1 = tk.Entry(self.root, textvariable=self.num1)
        entry_box1.grid(row=0, column=1, padx=10, pady=10)

        entry_label2 = tk.Label(self.root, text="Number 2:")
        entry_label2.grid(row=1, column=0, padx=10, pady=10)
        entry_box2 = tk.Entry(self.root, textvariable=self.num2)
        entry_box2.grid(row=1, column=1, padx=10, pady=10)

        operator_label = tk.Label(self.root, text="Operator:")
        operator_label.grid(row=0, column=2, padx=10, pady=10)
        operators = ("+", "-", "*", "/")
        operator_spinbox = ttk.Combobox(self.root, values=operators, textvariable=self.operator)
        operator_spinbox.grid(row=0, column=3, padx=10, pady=10)
        operator_spinbox.set("+")

        calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        calculate_button.grid(row=2, column=0, columnspan=4, pady=10)

        result_label = tk.Label(self.root, text="Result:")
        result_label.grid(row=3, column=0, padx=10, pady=10)
        result_entry = tk.Entry(self.root, textvariable=self.result, state='readonly')
        result_entry.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

    def calculate(self):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            operator = self.operator.get()
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2
            else:
                raise ValueError("Invalid operator")
            self.result.set(result)
        except ValueError as e:
            self.result.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
