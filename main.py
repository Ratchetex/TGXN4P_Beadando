import tkinter
from tkinter import *
import tkinter.messagebox
# from subprocess import call
# import time
from calcModule import Calculate

tinker = Tk()
tinker.title("Számológép")
tinker.resizable(False, False)
e = Entry(tinker, width=50, borderwidth=1)
e.grid(row=0, column=0, columnspan=4)


def button_click(number):
    num = e.get()
    e.delete(0, END)
    e.insert(0, str(num) + str(number))


def button_clear():
    e.delete(0, END)
    e.insert(0, "")


def button_add():
    matek = Calculate
    matek.operand = "+"
    first_number = e.get()
    if first_number.isdigit():
        matek.x = float(first_number)
        e.delete(0, END)
    else:
        e.delete(0, END)


def button_subtract():
    matek = Calculate
    matek.operand = "-"
    first_number = e.get()
    if first_number.isdigit():
        matek.x = float(first_number)
        e.delete(0, END)
    else:
        e.delete(0, END)


def button_multiply():
    matek = Calculate
    matek.operand = "*"
    first_number = e.get()
    if first_number.isdigit():
        # Calculate.x = float(first_number)
        e.delete(0, END)
    else:
        e.delete(0, END)


def button_divide():
    matek = Calculate
    matek.operand = "/"
    first_number = e.get()
    if first_number.isdigit():
        matek = Calculate
        matek.x = float(first_number)
        e.delete(0, END)
    else:
        e.delete(0, END)


def button_equals():
    second_number = e.get()
    if second_number.isdigit():
        matek = Calculate()
        matek.y = float(second_number)
        e.delete(0, END)
        resval = matek.result()
        if resval.is_integer():
            e.insert(0, str(int(resval)))
        else:
            e.insert(0, resval)
    else:
        e.delete(0, END)

        def msgbx():
            tkinter.messagebox.showinfo("Hiba!", "A megadott érték nem megfelelő!")

        msgbx()


def button_pow2():
    matek = Calculate
    matek.operand = "2"
    number = e.get()
    if number.isdigit():
        matek = Calculate()
        matek.y = float(number)
        e.delete(0, END)
        resval = matek.result()
        if resval.is_integer():
            e.insert(0, str(int(resval)))
        else:
            e.insert(0, resval)
    else:
        e.delete(0, END)

        def msgbx():
            tkinter.messagebox.showinfo("Hiba!", "A megadott érték nem megfelelő!")

        msgbx()


def button_pow3():
    matek = Calculate
    matek.operand = "3"
    number = e.get()
    if number.isdigit():
        matek = Calculate()
        matek.y = float(number)
        e.delete(0, END)
        resval = matek.result()
        if resval.is_integer():
            e.insert(0, str(int(resval)))
        else:
            e.insert(0, resval)
    else:
        e.delete(0, END)

        def msgbx():
            tkinter.messagebox.showinfo("Hiba!", "A megadott érték nem megfelelő!")

        msgbx()


def button_sqrt():
    matek = Calculate
    matek.operand = "s"
    number = e.get()
    if number.isdigit():
        matek = Calculate()
        e.delete(0, END)
        resval = matek.result()
        e.insert(0, resval)
    else:
        e.delete(0, END)

        def msgbx():
            tkinter.messagebox.showinfo("Hiba!", "A megadott érték nem megfelelő!")

        msgbx()


def button_negate():
    value = float(e.get())
    negateable = value * -1
    if value.is_integer():
        if negateable.is_integer():
            negateable = int(negateable)
            e.delete(0, END)
            e.insert(0, str(negateable))
        else:
            e.delete(0, END)
            e.insert(0, str(value))
    else:
        e.delete(0, END)

        def msgbx():
            tkinter.messagebox.showinfo("Hiba!", "A megadott érték nem megfelelő!")

        msgbx()


button0 = Button(tinker, text="0", width=10, height=5, command=lambda: button_click(0))
button1 = Button(tinker, text="1", width=10, height=5, command=lambda: button_click(1))
button2 = Button(tinker, text="2", width=10, height=5, command=lambda: button_click(2))
button3 = Button(tinker, text="3", width=10, height=5, command=lambda: button_click(3))
button4 = Button(tinker, text="4", width=10, height=5, command=lambda: button_click(4))
button5 = Button(tinker, text="5", width=10, height=5, command=lambda: button_click(5))
button6 = Button(tinker, text="6", width=10, height=5, command=lambda: button_click(6))
button7 = Button(tinker, text="7", width=10, height=5, command=lambda: button_click(7))
button8 = Button(tinker, text="8", width=10, height=5, command=lambda: button_click(8))
button9 = Button(tinker, text="9", width=10, height=5, command=lambda: button_click(9))
button_add = Button(tinker, text="+", width=10, height=5, command=button_add)
button_subtract = Button(tinker, text="-", width=10, height=5, command=button_subtract)
button_multiply = Button(tinker, text="*", width=10, height=5, command=button_multiply)
button_divide = Button(tinker, text="/", width=10, height=5, command=button_divide)
button_ce = Button(tinker, text="CE", width=10, height=5, command=lambda: button_clear())
button_equals = Button(tinker, text="=", width=10, height=5, command=button_equals)
button_pow2 = Button(tinker, text="x²", width=10, height=5, command=button_pow2)
button_pow3 = Button(tinker, text="x³", width=10, height=5, command=button_pow3)
button_sqrt = Button(tinker, text="√", width=10, height=5, command=button_sqrt)
button_negate = Button(tinker, text="*-1", width=10, height=5, command=button_negate)

button0.grid(row=5, column=0)
button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
button_pow2.grid(row=1, column=0)
button_pow3.grid(row=1, column=1)
button_sqrt.grid(row=1, column=2)
button_negate.grid(row=1, column=3)
button_add.grid(row=2, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=4, column=3)
button_divide.grid(row=5, column=3)
button_ce.grid(row=5, column=1)
button_equals.grid(row=5, column=2)

tinker.mainloop()
