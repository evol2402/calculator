import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = combo_operation.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                result = "Error! Division by zero."
            else:
                result = num1 / num2
        else:
            result = "Invalid operation"

        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Invalid input! Please enter numbers.")

# Setting up the main window
root = tk.Tk()
root.title("Simple Calculator")

# Creating widgets
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.grid(row=0, column=0)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.grid(row=1, column=0)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

label_operation = tk.Label(root, text="Select operation:")
label_operation.grid(row=2, column=0)

combo_operation = tk.StringVar()
combo_operation.set("Add")
operation_dropdown = tk.OptionMenu(root, combo_operation, "Add", "Subtract", "Multiply", "Divide")
operation_dropdown.grid(row=2, column=1)

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=3, column=0, columnspan=2)

label_result = tk.Label(root, text="Result: ")
label_result.grid(row=4, column=0, columnspan=2)

# Run the application
root.mainloop()
