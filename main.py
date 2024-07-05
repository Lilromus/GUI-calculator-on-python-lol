from tkinter import *

def clear():
    global equation_text
    equation_text = ""
    equation_label.set(equation_text)


def button_press(num):
    global equation_text
    equation_text += str(num)
    equation_label.set(equation_text)
    print(equation_text)

def equal():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)

    except ZeroDivisionError:
        equation_label.set("Arithmetical error.")

        equation_text = ""
    print(total)


window = Tk()
window.title("Calculator in Python lol")
window.geometry("400x400")

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas', 20), background="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button7 = Button(frame, text=7, height=2, width=6, font=35, command=lambda: button_press(7))
button7.grid(row=0, column=0)

button8 = Button(frame, text=8, height=2, width=6, font=35, command=lambda: button_press(8))
button8.grid(row=0, column=1)

button9 = Button(frame, text=9, height=2, width=6, font=35, command=lambda: button_press(9))
button9.grid(row=0, column=2)

button4 = Button(frame, text=4, height=2, width=6, font=35, command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=2, width=6, font=35, command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=2, width=6, font=35, command=lambda: button_press(6))
button6.grid(row=1, column=2)

button1 = Button(frame, text=1, height=2, width=6, font=35, command=lambda: button_press(1))
button1.grid(row=2, column=0)

button2 = Button(frame, text=2, height=2, width=6, font=35, command=lambda: button_press(2))
button2.grid(row=2, column=1)

button3 = Button(frame, text=3, height=2, width=6, font=35, command=lambda: button_press(3))
button3.grid(row=2, column=2)

button0 = Button(frame, text=0, height=2, width=6, font=35, command=lambda: button_press(0))
button0.grid(row=3, column=0)

button_dot = Button(frame, text=".", height=2, width=6, font=35, command=lambda: button_press('.'))
button_dot.grid(row=3, column=1)

button_equal = Button(frame, text="=", height=2, width=6, font=35, command=equal)
button_equal.grid(row=3, column=2)

button_sum = Button(frame, text="+", height=2, width=6, font=35, command=lambda: button_press('+'))
button_sum.grid(row=0, column=3)

button_minus = Button(frame, text="-", height=2, width=6, font=35, command=lambda: button_press('-'))
button_minus.grid(row=1, column=3)

button_multiply = Button(frame, text="*", height=2, width=6, font=35, command=lambda: button_press('*'))
button_multiply.grid(row=2, column=3)

button_divine = Button(frame, text="/", height=2, width=6, font=35, command=lambda: button_press('/'))
button_divine.grid(row=3, column=3)

button_clear = Button(window, text="AC", height=2, width=28, font=35, command=clear)
button_clear.pack()

window.mainloop()
