from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry('450x800')

def click(event):
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()    


    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


scvalue = StringVar()
scvalue.set("")
screen=Entry(root, textvar=scvalue, font="Lucida 40 bold")
screen.pack(fill=X, ipadx=8, ipady=8, padx=8 )

f1 = Frame(root, bg="grey")

b1 = Button(f1, text="9", padx=11, pady=5, font="lucida 35 bold")
b1.pack(side=LEFT, padx=9, pady=6)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="8", padx=11, pady=5, font="lucida 35 bold")
b1.pack(side=LEFT, padx=9, pady=6)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="7", padx=11, pady=5, font="lucida 35 bold")
b1.pack(side=LEFT, padx=9, pady=6)
b1.bind("<Button-1>", click)


f1.pack()

f1 = Frame(root, bg="grey")

b1 = Button(f1, text="6", padx=11, pady=5, font="lucida 35 bold")
b1.pack(side=LEFT, padx=9, pady=6)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="5", padx=11, pady=5, font="lucida 35 bold")
b1.pack(side=LEFT, padx=9, pady=6)
b1.bind("<Button-1>", click)


b1 = Button(f1, text="4", padx=11, pady=5, font="lucida 35 bold")
b1.pack(side=LEFT, padx=9, pady=6)
b1.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root, bg="grey")

b1 = Button(f1, text="3", padx=11, pady=5, font="lucida 35 bold")
b1.pack(side=LEFT, padx=9, pady=6)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="2", padx=11, pady=5, font="lucida 35 bold")
b1.pack(side=LEFT, padx=9, pady=6)
b1.bind("<Button-1>", click)


b1 = Button(f1, text="1", padx=11, pady=5, font="lucida 35 bold")
b1.pack(side=LEFT, padx=9, pady=6)
b1.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root, bg="grey")

b1 = Button(f1, text="0", padx=11, pady=5, font="lucida 35 bold")
b1.pack(side=LEFT, padx=10, pady=6)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="+", padx=15, pady=5, font="lucida 35 bold")
b1.pack(side=LEFT, padx=9, pady=6)
b1.bind("<Button-1>", click)


b1 = Button(f1, text="-", padx=11, pady=5, font="lucida 35 bold")
b1.pack(side=LEFT, padx=9, pady=6)
b1.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root, bg="grey")

b1 = Button(f1, text="*", padx=11, pady=5, font="lucida 35 bold")
b1.pack(side=LEFT, padx=9, pady=6)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="C", padx=11, pady=5, font="lucida 35 bold")
b1.pack(side=LEFT, padx=9, pady=6)
b1.bind("<Button-1>", click)


b1 = Button(f1, text="=", padx=11, pady=5, font="lucida 35 bold")
b1.pack(side=LEFT, padx=9, pady=6)
b1.bind("<Button-1>", click)

f1.pack()

root.mainloop()