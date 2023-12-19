#!python3

"""
##### Task 3 tKinter Compound Interest 
Create an application to calculate the final value of a compount interest value problem.  Recall that the final value can be calculated with:

A = P(1+r/n)^(n*t) where:
P = Principal (amount of the initial investment)
r = Interest rate as a decimal (4% has r = 0.04)
n = Number of compounding periods in a year (monthly n = 12, daily n=365)
t = number of years

You should decide which values should have regular entry widgets, comboboxes or spinboxes.  You will need a label or entry box to show your result.
"""




import tkinter as tk
from tkinter import ttk

class CompoundInterestCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Compound Interest Calculator")
        self.principal = tk.StringVar()
        self.interest_rate = tk.StringVar()
        self.compounding_periods = tk.StringVar()
        self.years = tk.StringVar()
        self.result = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        principal_label = tk.Label(self.root, text="Principal:")
        principal_label.grid(row=0, column=0, padx=10, pady=10)
        principal_entry = tk.Entry(self.root, textvariable=self.principal)
        principal_entry.grid(row=0, column=1, padx=10, pady=10)

        interest_rate_label = tk.Label(self.root, text="Interest Rate (%):")
        interest_rate_label.grid(row=1, column=0, padx=10, pady=10)
        interest_rate_entry = tk.Entry(self.root, textvariable=self.interest_rate)
        interest_rate_entry.grid(row=1, column=1, padx=10, pady=10)

        compounding_label = tk.Label(self.root, text="Compounding Periods per Year:")
        compounding_label.grid(row=2, column=0, padx=10, pady=10)
        compounding_spinbox = ttk.Combobox(self.root, values=["1", "2", "4", "12", "365"], textvariable=self.compounding_periods)
        compounding_spinbox.grid(row=2, column=1, padx=10, pady=10)
        compounding_spinbox.set("1")

        years_label = tk.Label(self.root, text="Number of Years:")
        years_label.grid(row=3, column=0, padx=10, pady=10)
        years_entry = tk.Entry(self.root, textvariable=self.years)
        years_entry.grid(row=3, column=1, padx=10, pady=10)

        calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

        result_label = tk.Label(self.root, text="Final Value:")
        result_label.grid(row=5, column=0, padx=10, pady=10)
        result_entry = tk.Entry(self.root, textvariable=self.result, state='readonly')
        result_entry.grid(row=5, column=1, padx=10, pady=10)

    def calculate(self):
        try:
            principal = float(self.principal.get())
            interest_rate = float(self.interest_rate.get()) / 100
            compounding_periods = int(self.compounding_periods.get())
            years = float(self.years.get())

            result = principal * (1 + interest_rate / compounding_periods) ** (compounding_periods * years)
            self.result.set(round(result, 2))

        except ValueError as e:
            self.result.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = CompoundInterestCalculator(root)
    root.mainloop()
