from tkinter import *
from crawPCJIC import analizarTest
import time

top= Tk()
top.geometry("1000x450")
top.title("Buscador de tesis PCJIC")
top["bg"]="#ECE7E6"


def validarBuscar():
   if len(txtName.get()) == 0:
      txtArea.delete(1.0, END)
      txtArea.insert(INSERT, "Faltan Datos\n")
   else:
      txtArea.delete(1.0, END)
      texto = str(analizarTest(txtName.get()))
      txtArea.insert(INSERT, texto + "\n")

def limpiar():
   txtArea.delete(1.0, END)
   txtName.delete(first=0,last=len(txtName.get()))


scroll = Scrollbar(top)

txtArea = Text(top, height=18, width=115, yscrollcommand=scroll.set)
txtArea.place(x=20,y=20)
scroll.config(command=txtArea.yview)
scroll.pack(side=RIGHT,fill=Y)

lblUrl=Label(top, text="Digite nombre (Docente o Estudiante)", justify=LEFT)
lblUrl.place(x=20,y=320)

btnBuscar=Button(top,text="Buscar",command=validarBuscar)
btnBuscar.place(x=20, y=380)

btnLimpiar=Button(top,text="Limpiar",command=limpiar)
btnLimpiar.place(x=80, y=380)

txtName=Entry(top,width=55)
txtName.place(x=20,y=350)

top.mainloop()