from tkinter import Tk, Label, Button, StringVar, Entry, Frame
from calculator import add, subtract, multiply, divide

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)
        else:
            result = "Invalid operation"
        result_var.set(f"Result: {result}")
    except ValueError:
        result_var.set("Invalid input")

app = Tk()
app.title("Simple Calculator")

frame = Frame(app)
frame.pack(padx=10, pady=10)

entry1 = Entry(frame)
entry1.grid(row=0, column=0, padx=5, pady=5)

entry2 = Entry(frame)
entry2.grid(row=0, column=1, padx=5, pady=5)

result_var = StringVar()
result_label = Label(frame, textvariable=result_var)
result_label.grid(row=1, columnspan=2)

Button(frame, text="Add", command=lambda: calculate('add')).grid(row=2, column=0)
Button(frame, text="Subtract", command=lambda: calculate('subtract')).grid(row=2, column=1)
Button(frame, text="Multiply", command=lambda: calculate('multiply')).grid(row=3, column=0)
Button(frame, text="Divide", command=lambda: calculate('divide')).grid(row=3, column=1)

app.mainloop()