

import tkinter as tk
import math

window = tk.Tk()
window.title("Scientific Calculator")
window.geometry("400x350")

operator = ""

display = tk.Entry(window, width=30)
display.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

def set_operator(op):
    global operator
    operator = op

def clear():
    display.delete(0, tk.END)

def add_to_display(value):
    display.insert(tk.END, value)

tk.Button(window, text="7", command=lambda: add_to_display("7")).grid(row=5, column=0)
tk.Button(window, text="8", command=lambda: add_to_display("8")).grid(row=5, column=1)
tk.Button(window, text="9", command=lambda: add_to_display("9")).grid(row=5, column=2)

tk.Button(window, text="4", command=lambda: add_to_display("4")).grid(row=6, column=0)
tk.Button(window, text="5", command=lambda: add_to_display("5")).grid(row=6, column=1)
tk.Button(window, text="6", command=lambda: add_to_display("6")).grid(row=6, column=2)

tk.Button(window, text="1", command=lambda: add_to_display("1")).grid(row=7, column=0)
tk.Button(window, text="2", command=lambda: add_to_display("2")).grid(row=7, column=1)
tk.Button(window, text="3", command=lambda: add_to_display("3")).grid(row=7, column=2)

tk.Button(window, text="0", command=lambda: add_to_display("0")).grid(row=8, column=1)

tk.Button(window, text=".", command=lambda: add_to_display(".")).grid(row=8, column=1)

tk.Button(window,
          text="C",
          width=4,
          height=2,
          command=clear).grid(row=3, column=2)

def calculate():
    global operator

    try:
        num = float(display.get())

        if operator == "sqrt":
            result = math.sqrt(num)

        elif operator == "sin":
            result = math.sin(math.radians(num))

        elif operator == "cos":
            result = math.cos(math.radians(num))

        elif operator == "tan":
            result = math.tan(math.radians(num))

        elif operator == "10^x":
            result = 10 ** num

        elif operator == "log":
            result = math.log10(num)

        elif operator == "ln":
            result = math.log(num)

        elif operator == "x^2":
            result = num ** 2

        else:
            result = "Select Op"

        display.delete(0, tk.END)
        display.insert(0, result)

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Operation Buttons
tk.Button(window, text="sin",
          command=lambda: set_operator("sin")).grid(row=1, column=0)

tk.Button(window, text="cos",
          command=lambda: set_operator("cos")).grid(row=1, column=1)

tk.Button(window, text="tan",
          command=lambda: set_operator("tan")).grid(row=1, column=2)

tk.Button(window, text="sqrt",
          command=lambda: set_operator("sqrt")).grid(row=2, column=0)

tk.Button(window, text="log",
          command=lambda: set_operator("log")).grid(row=2, column=1)

tk.Button(window, text="ln",
          command=lambda: set_operator("ln")).grid(row=2, column=2)

tk.Button(window, text="x²",
          command=lambda: set_operator("x^2")).grid(row=3, column=0)

tk.Button(window, text="10ˣ",
          command=lambda: set_operator("10^x")).grid(row=3, column=1)

tk.Button(window, text="=",
          command=calculate).grid(row=4, column=0, columnspan=3)
window.mainloop()