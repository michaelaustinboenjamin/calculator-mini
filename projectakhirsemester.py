import tkinter
from tkinter import ttk
from tkinter import Tk,Button,Entry
show=tkinter.Tk()
show.title("Calculator mini")
show.configure(background="black")
show.geometry("325x500")
input_text=tkinter.StringVar()
input_field=Entry(show, textvariable=input_text)
input_field.grid(row=0, column=0)
def clear() :
	input_text.set("")
def calculate():
	try:
		result = str(eval(input_text.get()))
		input_text.set(result)
	except Exception as e:
		input_text.set("ERROR...")
clearall=Button(show,text="Clear",width=10,command=clear)
clearall.grid(row=0,column=15)
calculatenumber=Button(show,text="Calculate",width=10,command=calculate)
calculatenumber.grid(row=0,column=16)
show.mainloop()