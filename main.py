from tkinter import *


def F_to_C():
    f = float(temp_in_F.get())
    c = (f - 32) * 0.5556
    result = round(c, 2)
    celsius_result.config(text=f"{result}"+" C")

window = Tk()
window.title("Fahrenheit to Celsius")
window.config(padx=50, pady=50)

temp_in_F = Entry(width=8, font=("courier", 18))
temp_in_F.grid(column=1, row=0)

temp_in_F_label = Label(text="Fahrenheit", font=("courier", 18))
temp_in_F_label.grid(column=2, row=0)

celsius_result = Label(text="C", font=("courier", 16))
celsius_result.grid(column=1, row=1)

calculate_button = Button(text="Calculate", font=("courier", 14), command=F_to_C)
calculate_button.grid(column=2, row=1)


window.mainloop()

