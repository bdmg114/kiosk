import tkinter as tk
from tkinter import messagebox

price = {'milsut':3500, 'coffee':3000,'tea':1500,'latte':2500}
order = []
sum = 0


def order_menu(menu):
    global sum

    if menu not in price:
        print("no drink")
    this_price = price.get(menu)
    sum += this_price
    order.append(menu)
    textarea.insert(tk.INSERT, menu+" ")
    label1['text'] = "금액" + str(sum)

def btn_exit():
    msgbox = messagebox.askquestion('confirm', 'end of order?')
    if msgbox == 'yes':
        exit()

window = tk.Tk()
window.title("kiosk")
window.geometry("300x350")

frame1 = tk.Frame(window)
frame1.pack()

tk.Button(frame1,text="coffee", command=lambda : order_menu("coffee"), width=20, height=3).grid(row=0, column=0)
tk.Button(frame1,text="tea", command=lambda : order_menu("tea"), width=20, height=3).grid(row=1, column=0)
tk.Button(frame1,text="latte", command=lambda : order_menu("latte"), width=20, height=3).grid(row=3, column=0)
tk.Button(frame1,text="milsut", command=lambda : order_menu("milsut"), width=20, height=3).grid(row=4, column=0)
tk.Button(frame1,text="exit", command=btn_exit, width=30, height=3).grid(row=5, column=0)

label1 = tk.Label(window, text="금액 0원", width=100, height=2, fg="blue")
label1.pack()

textarea = tk.Text(window)
textarea.pack()

window.mainloop()