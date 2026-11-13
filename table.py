from tkinter import*
from tkinter.ttk import*
window= Tk()
window.title("Math table")
window.geometry("550x1100")
title= Label(window,text="Mathematical table",font="Arial 20")
text= Label(window,text="Number and range:",font="Arial 20")
title.grid(column=1,row=0)
text.grid(column=0,row=1)
def tables():
    result= ""
    for i in range(1,final.get()+1):
        result+= str(number.get())+"x"+str(i)+"="+str(number.get()*i)+"\n"
    table.configure(text=result)
number= IntVar()
numbers= Combobox(window,textvariable=number,width=5)
numbers["values"]=tuple(range(101))
final= IntVar()
r10= Radiobutton(window,text="10",variable=final,value=10)
r20= Radiobutton(window,text="20",variable=final,value=20)
r30= Radiobutton(window,text="30",variable=final,value=30)
r10.grid(column=2,row=1)
r20.grid(column=2,row=2)
r30.grid(column=2,row=3)
numbers.grid(column=1,row=1)
final.set(30)
generate= Button(window,text="Generate",command=tables)
table= Label(window,font="Arial 20")
generate.grid(column=1,row=3)
table.grid(column=1,row=4)
window.mainloop()