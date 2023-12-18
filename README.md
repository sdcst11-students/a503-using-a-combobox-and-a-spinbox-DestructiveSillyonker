## SDSS Computing Studies Python Assignment
### Assignment #A503 Comboboxes

Objectives:
* Limit user entry to specific values using a combobox
* Limit user entry to specific values using a spinbox
* Decide whether to use a combobox or spinbox for data entry

Sometimes you don't want to allow the user to enter in any values that they want into an Entry box; sometimes you want to limit the variety fo their responses.  For example, you might want them to choose their birthdate.  Month should only be from January to Decemeber, and maybe you don't want to allow spelling errors (which could easily happen).  You also don't want to allow numbers out of the range of 1-31 for day of the month.

In these circumstances, you may want to use a combobox or spinbox. These are modifications to an Entry box widget that allow you to limit responses.

A combobox is also known as a drop down dialog. When you click on it, a number of options become visibile and you can choose which one to select.

A spinbox has arrows that allow you to scroll up and down allowing you to scroll through the entries.  On touch devices, you can swipe to rapidly scroll through.

Retrieving data from a combobox or spinbox is accomplished using the .get() method (very similar to the entry box widget), and the .set() method can be used to set the currently selected value to a specific one.

### 3 Tasks (8 points)

##### Task 1 Select birthdate.
Create an application that allows the user to select the month, day and year of their birthdate. You will need 3 separate entries: month,day, year.

You are responsible for designing your GUI.  You may use the pack, grid or place methods for doing so, but your GUI layout should be organized and visually appealing.

Display the results of their selection in an entry box in the widget.

Extra: Can you create some of the lists of values dynamically instead of explicitly listing them all?

##### Task 2 Calculator
Create a simple app that allows you to do a calculation with an arithmetic operation.  You will need a spinbox between 2 entry boxes.  The entryboxes are where you should be entering your numbers, and the spinbox should be the operator.  You will need a button to do the calculation.  You can modify your assignment from A500 for this.

##### Task 3 tKinter Compound Interest 
Create an application to calculate the final value of a compount interest value problem.  Recall that the final value can be calculated with:

A = P(1+r/n)^(n*t) where:
P = Principal (amount of the initial investment)
r = Interest rate as a decimal (4% has r = 0.04)
n = Number of compounding periods in a year (monthly n = 12, daily n=365)
t = number of years

You should decide which values should have regular entry widgets, comboboxes or spinboxes.  You will need a label or entry box to show your result.
