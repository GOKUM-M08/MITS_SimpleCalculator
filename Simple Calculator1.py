import tkinter as tk

# Function to update the expression
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the input field
def clear():
    global expression
    expression = ""
    equation.set("")

# Main code
if __name__ == "__main__":
    # Create GUI window
    gui = tk.Tk()
    gui.configure(background="lightgray")
    gui.title("Simple Calculator")
    gui.geometry("300x400")

    expression = ""

    # StringVar to update text in Entry widget
    equation = tk.StringVar()

    # Entry field
    expression_field = tk.Entry(gui, textvariable=equation, font=('Arial', 20), justify='right')
    expression_field.grid(columnspan=4, ipadx=10, ipady=20)

    # Buttons layout
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ]

    for (text, row, col) in buttons:
        if text == '=':
            action = equalpress
        else:
            action = lambda x=text: press(x)

        tk.Button(gui, text=text, fg='black', bg='white',
                  font=('Arial', 18), command=action,
                  height=2, width=6).grid(row=row, column=col)

    # Clear Button
    tk.Button(gui, text='C', fg='white', bg='red',
              font=('Arial', 18), command=clear,
              height=2, width=25).grid(row=5, columnspan=4)

    gui.mainloop()
