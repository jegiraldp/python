from tkinter import *
from tkinter import messagebox

import suma
#import resta
##
vnt= Tk()
vnt.geometry("350x150")
vnt.title("Calculadora Python T200")
##
def evSuma():
    if len(txtNumUno.get()) == 0 | len(txtNumDos.get()) == 0:
        lblResultado["text"]="Faltan\nDatos"
    else:
        res=suma.calcular(txtNumUno.get(), txtNumDos.get())
        lblResultado["text"]="Resultado: "+str(res)
##


##labels
lblNumUno = Label(vnt, text="Número 1", justify=LEFT)
lblNumUno.place(x=20,y=20)

lblNumDos = Label(vnt, text="Número 2", justify=LEFT)
lblNumDos.place(x=20,y=60)

lblResultado = Label(vnt, text="...", justify=CENTER, font=('times', 16, 'bold'))
lblResultado.place(x=200, y=50)
##entry
txtNumUno= Entry(vnt,width=10)
txtNumUno.place(x=100,y=20)

txtNumDos= Entry(vnt,width=10)
txtNumDos.place(x=100,y=60)
##
btnCalcular= Button(vnt, text="Sumar", command=evSuma)
btnCalcular.place(x=60,y=100)
##
vnt.mainloop()

