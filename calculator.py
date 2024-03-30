from tkinter import *

root = Tk()
root.geometry("500x500")
root.title('CALCUATOR BY Mr.Sabin_kumar')

entry_box = Entry(root, font="lucida 20 bold")
entry_box.pack(fill=X, padx=5, pady=5, ipady=10)

def on_button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        result = str(eval(entry_box.get()))
        entry_box.delete(0, END)
        entry_box.insert(END, result)
    elif text == "C":
        entry_box.delete(0, END)
    elif text == "DEL":
        entry_box.delete(len(entry_box.get()) - 1)
    else:
        entry_box.insert(END, text)

f1 = Frame(root,bg="light blue")
f1.pack(pady=15)

buttons = [

    '7', '8', '9', 'DEL', 'C',
    '4', '5', '6', '*', '/',
    '1', '2', '3', '+', '-',
    '.', '0', '00', '%', '='
]
rows, col = 1, 0

for button_text in buttons:
    btn = Button(f1, text=button_text, font="Lucida 15", width=4, height=2)
    btn.grid(row=rows, column=col)
    col += 1
    if col > 4:
        col = 0
        rows += 1

    btn.bind("<Button-1>", on_button_click)

root.mainloop()