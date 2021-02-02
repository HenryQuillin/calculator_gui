from tkinter import *

master = Tk()
master.geometry('130x130')
master.configure(background="dark blue")
master.title('calculator')


def test_line():
    print("Button Press")


# Operators
plus = Button(master, text='+', command=test_line, bg="gray20", fg="lime green", highlightbackground="gray20",
              activebackground="deep sky blue")
plus.grid(row=1, column=3)
minus = Button(master, text='-', command=test_line, bg="gray20", fg="lime green", highlightbackground="gray20",
               activebackground="deep sky blue")
minus.grid(row=2, column=3)
divide = Button(master, text='/', command=test_line, bg="gray20", fg="lime green", highlightbackground="gray20",
                activebackground="deep sky blue")
divide.grid(row=3, column=3)
multiply = Button(master, text='*', command=test_line, bg="gray20", fg="lime green", highlightbackground="gray20",
                  activebackground="deep sky blue")
multiply.grid(row=4, column=3)
equals = Button(master, text='=', command=test_line, bg="gray20", fg="lime green", highlightbackground="gray20",
                activebackground="deep sky blue")
equals.grid(row=4, column=2)

# Buttons 1 - 9
number = 1
for i in range(1, 4):
    for j in range(3):
        strnumber = str(number)
        button_name = 'button'+strnumber
        button_name = Button(master, text=number, command=test_line, bg="gray20", fg="lime green", highlightbackground="gray20",activebackground="deep sky blue")
        button_name.grid(row=i, column=j)
        number = number + 1

zero = Button(master, text='0', command=test_line, bg="gray20", fg="lime green", highlightbackground="gray20",
activebackground="deep sky blue")
zero.grid(row=4, column=1)

String_input_value = StringVar(master, value='')
Total_box = Entry(master, textvariable=String_input_value)
Total_box.grid(row=0, columnspan=4, sticky=W + E)

master.mainloop()
