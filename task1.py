"""
##### Task 1 Select birthdate.
Create an application that allows the user to select the month, day and year of their birthdate. You will need 3 separate entries: month,day, year.

You are responsible for designing your GUI.  You may use the pack, grid or place methods for doing so, but your GUI layout should be organized and visually appealing.

Display the results of their selection in an entry box in the widget.

Extra: Can you create some of the lists of values dynamically instead of explicitly listing them all?
"""
import tkinter as tk
from tkinter import ttk

class BirthdateSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("Birthdate Selector")

        
        self.selected_month = tk.StringVar()
        self.selected_day = tk.StringVar()
        self.selected_year = tk.StringVar()

    
        self.create_widgets()

    def create_widgets(self):
        # Month
        months_label = tk.Label(self.root, text="Month:")
        months_label.grid(row=0, column=0, padx=10, pady=10)
        months = [str(i) for i in range(1, 13)]
        self.month_combobox = ttk.Combobox(self.root, values=months, textvariable=self.selected_month)
        self.month_combobox.grid(row=0, column=1, padx=10, pady=10)
        self.month_combobox.set("1") 
    
        days_label = tk.Label(self.root, text="Day:")
        days_label.grid(row=1, column=0, padx=10, pady=10)

    
        days = [str(i) for i in range(1, 32)]
        self.day_combobox = ttk.Combobox(self.root, values=days, textvariable=self.selected_day)
        self.day_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.day_combobox.set("1") 

        
        years_label = tk.Label(self.root, text="Year:")
        years_label.grid(row=2, column=0, padx=10, pady=10)

        
        current_year = 2023  
        years = [str(i) for i in range(current_year - 100, current_year + 1)]
        self.year_combobox = ttk.Combobox(self.root, values=years, textvariable=self.selected_year)
        self.year_combobox.grid(row=2, column=1, padx=10, pady=10)
        self.year_combobox.set(str(current_year))  
      
        display_button = tk.Button(self.root, text="Display", command=self.display_birthdate)
        display_button.grid(row=3, column=0, columnspan=2, pady=10)

        
        self.result_entry = tk.Entry(self.root, state='readonly')
        self.result_entry.grid(row=4, column=0, columnspan=2, pady=10)

    def display_birthdate(self):
        
        birthdate = f"{self.selected_month.get()}/{self.selected_day.get()}/{self.selected_year.get()}"
        self.result_entry.config(state='normal')
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, birthdate)
        self.result_entry.config(state='readonly')

if __name__ == "__main__":
    root = tk.Tk()
    app = BirthdateSelector(root)
    root.mainloop()