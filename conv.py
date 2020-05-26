from tkinter import *
from currency_converter import CurrencyConverter

app = Tk()
c = CurrencyConverter()

app.title('Конвертор')
app.configure(bg='#3eb489', padx=20, pady=20)

var1 = StringVar(app)
var2 = StringVar(app)
var1.set('Валюта')
var2.set('Валюта')

amount1 = Entry(app)
amount2 = Entry(app)

cCodes = ['USD', 'EUR', 'JPY', 'GBP', 'RUB']


def conv():
    sum = float(amount1.get())
    fromCur = var1.get()
    toCur = var2.get()

    calc = c.convert(sum, fromCur, toCur)
    res = amount2.insert(0, calc)

def clear():
    amount1.delete(0, END)
    amount2.delete(0, END)

app.mainloop()
