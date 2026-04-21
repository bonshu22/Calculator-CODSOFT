from tkinter import *



app = Tk()
app.title("Simple Calculator by Soumyadeep Biswas")
app.iconbitmap()

app.config(background="#54AB80")

app.resizable(True, True)






def click(num):
    """
    function to get the numbers clicked
    and displayed to the screen
    """
    
    exp = entry_field.get()
    
    entry_field.delete(0, END)

    
    entry_field.insert(0, str(exp) + str(num))


def add_button():
    """function to add two or more integers"""
    
    first_num = entry_field.get()
    global expression
    global operation
    operation = "add"
    expression = int(first_num)
    entry_field.delete(0, END)


def subtract_button():
    """function to subtract two or more integers"""
    
    first_num = entry_field.get()
    global expression
    global operation
    operation = "subtract"
    expression = int(first_num)
    entry_field.delete(0, END)


def multiply_button():
    """function to multiply two or more integers"""
    
    first_num = entry_field.get()
    
    global expression
    global operation
    operation = "multiply"
    expression = int(first_num)
    entry_field.delete(0, END)

def divide_button():
    """function to divide integers"""
    
    first_num = entry_field.get()
    
    global expression
    global operation
    operation = "divide"
    expression = int(first_num)
    entry_field.delete(0, END)

def clear():
    """function to clear entry field"""
    entry_field.delete(0, END)

def equal_button():
    """function to equate the values using an operation"""
    
    second_num = entry_field.get()

    
    entry_field.delete(0, END)

    
    if operation == "add":
        entry_field.insert(0, expression + int(second_num))

    elif operation == "subtract":
        entry_field.insert(0, expression - int(second_num))

    elif operation == "multiply":
        entry_field.insert(0, expression * int(second_num))

    elif operation == "divide":
        result = expression / int(second_num)
        if (expression % int(second_num) == 0):
            entry_field.insert(0, int(result))
        else:
            entry_field.insert(0, result)
        

    else:
        entry_field.insert("error")


entry_field = Entry(app,
                width=35,
                justify="right",
                borderwidth=5,
                
            )

entry_field.grid(row=0, column=0, columnspan=3, ipadx=10, pady=10)



button_1 = Button(app, borderwidth=3, text="1", height=1, width=7, padx=20, pady=10, command=lambda:click(1))
button_2 = Button(app, borderwidth=3, text="2", height=1, width=7, padx=20, pady=10, command=lambda:click(2))
button_3 = Button(app, borderwidth=3, text="3", height=1, width=7, padx=20, pady=10, command=lambda:click(3))
button_4 = Button(app, borderwidth=3, text="4", height=1, width=7, padx=20, pady=10, command=lambda:click(4))
button_5 = Button(app, borderwidth=3, text="5", height=1, width=7, padx=20, pady=10, command=lambda:click(5))
button_6 = Button(app, borderwidth=3, text="6", height=1, width=7, padx=20, pady=10, command=lambda:click(6))
button_7 = Button(app, borderwidth=3, text="7", height=1, width=7, padx=20, pady=10, command=lambda:click(7))
button_8 = Button(app, borderwidth=3, text="8", height=1, width=7, padx=20, pady=10, command=lambda:click(8))
button_9 = Button(app, borderwidth=3, text="9", height=1, width=7, padx=20, pady=10, command=lambda:click(9))
button_0 = Button(app, borderwidth=3, text="0", height=1, width=7, padx=20, pady=10, command=lambda:click(0))
button_add = Button(app, borderwidth=3, text="+", height=1, width=7, padx=20, pady=10, command=add_button)
button_subtract = Button(app, borderwidth=3, text="-", height=1, width=7, padx=20, pady=10, command=subtract_button)
button_divide = Button(app, borderwidth=3, text="/", height=1, width=7, padx=20, pady=10, command=divide_button)
button_multiply = Button(app, borderwidth=3, text="x", height=1, width=7, padx=20, pady=10, command=multiply_button)
button_equal = Button(app, borderwidth=3, text="=", height=1, width=7, padx=70, pady=10, command=equal_button)
button_clear = Button(app, borderwidth=3, text="clear", height=1, width=7, padx=70, pady=10, command=clear)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)


button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)


button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)


button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)


button_multiply.grid(row=5, column=0)
button_divide.grid(row=6, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=6, column=1, columnspan=2)



app.mainloop()
