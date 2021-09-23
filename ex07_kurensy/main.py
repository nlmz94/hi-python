from tkinter import *

window = Tk()
window.title("Convert currencies")
window.minsize(1024, 480)
window.config(background='grey')
left_frame = Frame()

label_title = Label(
    window, text="Welcome to currency_converter.py", font=("Arial", 20), bg='blue', foreground='white')
label_title.pack()

input_amount = Entry(window, width=50, borderwidth=5)
input_amount.pack()

currency_to_convert = StringVar()
rb1 = Radiobutton(left_frame, text="Dollars", variable=currency_to_convert,
                  font=("Arial", 30),  value="Dollars")
rb2 = Radiobutton(left_frame, text="Pounds", variable=currency_to_convert,
                  font=("Arial", 30), value="Pounds")
rb3 = Radiobutton(left_frame, text="Rupees", variable=currency_to_convert,
                  font=("Arial", 30), value="Rupees")
rb4 = Radiobutton(left_frame, text="Euros", variable=currency_to_convert,
                  font=("Arial", 30), value="Euros")
rb1.grid(row=1, column=1)
rb2.grid(row=2, column=1)
rb3.grid(row=3, column=1)
rb4.grid(row=4, column=1)

new_currency = StringVar()
rba = Radiobutton(left_frame, text="Dollars", variable=new_currency,
                  font=("Arial", 30),  value="Dollars")
rbb = Radiobutton(left_frame, text="Pounds", variable=new_currency,
                  font=("Arial", 30), value="Pounds")
rbc = Radiobutton(left_frame, text="Rupees", variable=new_currency,
                  font=("Arial", 30), value="Rupees")
rbd = Radiobutton(left_frame, text="Euros", variable=new_currency,
                  font=("Arial", 30), value="Euros")
rba.grid(row=1, column=2)
rbb.grid(row=2, column=2)
rbc.grid(row=3, column=2)
rbd.grid(row=4, column=2)

pound_to_euro = 1.17
dollar_to_euro = 0.85
rupee_to_euro = 0.012
pound_to_dollar = pound_to_euro / dollar_to_euro
pound_to_rupee = pound_to_euro / rupee_to_euro
euro_to_pound = 1 / pound_to_euro
euro_to_dollar = 1 / dollar_to_euro
euro_to_rupee = 1 / rupee_to_euro
rupee_to_dollar = rupee_to_euro / dollar_to_euro
rupee_to_pound = rupee_to_euro / pound_to_euro
dollar_to_pound = dollar_to_euro / pound_to_euro
dollar_to_rupee = dollar_to_euro / rupee_to_euro


def convert_curreny():
    if currency_to_convert.get() == new_currency.get():
        return int(input_amount.get())
    elif currency_to_convert.get() == "Dollars" and new_currency.get() == "Euros":
        return int(input_amount.get()) * dollar_to_euro
    elif currency_to_convert.get() == "Pounds" and new_currency.get() == "Euros":
        return int(input_amount.get()) * pound_to_euro
    elif currency_to_convert.get() == "Rupees" and new_currency.get() == "Euros":
        return int(input_amount.get()) * rupee_to_euro
    elif currency_to_convert.get() == "Euros" and new_currency.get() == "Dollars":
        return int(input_amount.get()) * euro_to_dollar
    elif currency_to_convert.get() == "Pounds" and new_currency.get() == "Dollars":
        return int(input_amount.get()) * pound_to_dollar
    elif currency_to_convert.get() == "Rupees" and new_currency.get() == "Dollars":
        return int(input_amount.get()) * rupee_to_dollar
    elif currency_to_convert.get() == "Euros" and new_currency.get() == "Pounds":
        return int(input_amount.get()) * euro_to_pound
    elif currency_to_convert.get() == "Dollars" and new_currency.get() == "Pounds":
        return int(input_amount.get()) * dollar_to_pound
    elif currency_to_convert.get() == "Rupees" and new_currency.get() == "Pounds":
        return int(input_amount.get()) * rupee_to_pound
    elif currency_to_convert.get() == "Euros" and new_currency.get() == "Rupees":
        return int(input_amount.get()) * euro_to_rupee
    elif currency_to_convert.get() == "Dollars" and new_currency.get() == "Rupees":
        return int(input_amount.get()) * dollar_to_rupee
    elif currency_to_convert.get() == "Pounds" and new_currency.get() == "Rupees":
        return int(input_amount.get()) * pound_to_rupee


def generate_label():
    result = convert_curreny()
    new_amount_label = Label(window, text=f"{result} €", font=(
        "Arial", 30), bg='blue', foreground='white')
    new_amount_label.pack()


convert_button = Button(window, text="convert", command=generate_label, font=(
    "Arial", 30), bg='blue', foreground='white')
left_frame.pack()
convert_button.pack()
window.mainloop()
