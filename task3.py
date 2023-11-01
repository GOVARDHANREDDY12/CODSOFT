import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(screen.get())
            screen.delete(0, tk.END)
            screen.insert(tk.END, str(result))
        except Exception as e:
            screen.delete(0, tk.END)
            screen.insert(tk.END, "Error")

    elif text == "C":
        screen.delete(0, tk.END)
    else:
        screen.insert(tk.END, text)

root = tk.Tk()
root.title("Simple Calculator")

screen = tk.Entry(root, font=("Arial", 20))
screen.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 1
col = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, font=("Arial", 15))
    button.grid(row=row, column=col)
    button.bind("<Button-1>", on_button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
