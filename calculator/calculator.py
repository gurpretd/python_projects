# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
input_expression = ""
debug_enable = False


def pressed_expression(equation: StringVar, val: str):
    print("button pressed")
    global input_expression
    global debug_enable
    input_expression = input_expression + val
    if debug_enable:
        print("button pressed {} final expression {} ".format(val, input_expression))
    #  global equation
    equation.set(input_expression)


def pressed_equals(equation: StringVar):
    global input_expression
    total = str(eval(input_expression))  # eval(str)
    input_expression = input_expression + "=" + total
    equation.set(input_expression)


def pressed_clear(equation: StringVar):
    global input_expression
    input_expression = ""
    equation.set(input_expression)


def draw_calculator():
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light grey")

    # set the title of GUI window
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    gui.geometry("500x500")

    # StringVar() is the variable class
    # we create an instance of this class

    equation = StringVar()
    equation.set("")

    # create the text entry box for
    # showing the expression .
    row = 0

    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)

    row = row + 1
    column = 0
    button1 = Button(gui, text=' 1 ', fg='black', bg='red',
                     command=lambda: pressed_expression(equation, "1"), height=1, width=7)
    button1.grid(row=row, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='red',
                     command=lambda: pressed_expression(equation, "2"), height=1, width=7)
    button2.grid(row=row, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='red',
                     command=lambda: pressed_expression(equation, "3"), height=1, width=7)
    button3.grid(row=row, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='red',
                     command=lambda: pressed_expression(equation, "4"), height=1, width=7)
    button4.grid(row=row, column=3)

    row = row + 1
    column = 0
    button5 = Button(gui, text=' 5 ', fg='black', bg='red',
                     command=lambda: pressed_expression(equation, "5"), height=1, width=7)
    button5.grid(row=row, column=0)

    button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                     command=lambda: pressed_expression(equation, "6"), height=1, width=7)
    button6.grid(row=row, column=1)

    button7 = Button(gui, text=' 7 ', fg='black', bg='red',
                     command=lambda: pressed_expression(equation, "7"), height=1, width=7)
    button7.grid(row=row, column=2)

    button8 = Button(gui, text=' 8 ', fg='black', bg='red',
                     command=lambda: pressed_expression(equation, "8"), height=1, width=7)
    button8.grid(row=row, column=3)

    row = row + 1
    column = 0
    button9 = Button(gui, text=' 9 ', fg='black', bg='red',
                     command=lambda: pressed_expression(equation, "9"), height=1, width=7)
    button9.grid(row=row, column=0)

    button0 = Button(gui, text=' 0 ', fg='black', bg='red',
                     command=lambda: pressed_expression(equation, "0"), height=1, width=7)
    button0.grid(row=row, column=1)

    button_plus = Button(gui, text=' + ', fg='black', bg='red',
                         command=lambda: pressed_expression(equation, "+"), height=1, width=7)
    button_plus.grid(row=row, column=2)

    button_minus = Button(gui, text=' - ', fg='black', bg='red',
                          command=lambda: pressed_expression(equation, "-"), height=1, width=7)
    button_minus.grid(row=row, column=3)

    row = row + 1
    column = 0
    button_div = Button(gui, text=' / ', fg='black', bg='red',
                        command=lambda: pressed_expression(equation, "/"), height=1, width=7)
    button_div.grid(row=row, column=0)

    button_mul = Button(gui, text=' X ', fg='black', bg='red',
                        command=lambda: pressed_expression(equation, "*"), height=1, width=7)
    button_mul.grid(row=row, column=1)

    button_equals = Button(gui, text=' = ', fg='black', bg='red',
                           command=lambda: pressed_equals(equation), height=1, width=7)
    button_equals.grid(row=row, column=2)

    button_clear = Button(gui, text=' CLEAR ', fg='black', bg='red',
                          command=lambda: pressed_clear(equation), height=1, width=7)
    button_clear.grid(row=row, column=3)

    gui.mainloop()


if __name__ == "__main__":
    draw_calculator()
