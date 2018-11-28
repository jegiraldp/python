from tkinter import *
from craw import analizarImg, analizarHiper

top= Tk()
top.geometry("600x450")
top.title("Craw-Test_Uno")
top["bg"]="#347D67"

###########
def validarImg():
   if len(txtUrl.get()) == 0:
      txtArea.delete(1.0, END)
      txtArea.insert(INSERT,"Faltan Datos\n")
   else:
      txtArea.delete(1.0, END)
      txtArea.insert(INSERT, "----------------\n")
      texto=str(analizarImg(txtUrl.get()))
      txtArea.insert(INSERT, texto+"\n")

      ###########
def validarHiper():
   if len(txtUrl.get()) == 0:
      txtArea.delete(1.0, END)
      txtArea.insert(INSERT, "Faltan Datos\n")
   else:
      txtArea.delete(1.0, END)
      txtArea.insert(INSERT, "----------------\n")
      texto = str(analizarHiper(txtUrl.get()))
      txtArea.insert(INSERT, texto + "\n")

scroll = Scrollbar(top)

txtArea = Text(top, height=18, width=60, yscrollcommand=scroll.set)
txtArea.place(x=20,y=20)
scroll.config(command=txtArea.yview)
scroll.pack(side=RIGHT,fill=Y)

lblUrl=Label(top, text="URL:", justify=LEFT)
lblUrl.place(x=20,y=320)

btnAnalizarIMG=Button(top,text="Imágenes",command=validarImg)
btnAnalizarIMG.place(x=450, y=345)

btnAnalizarA=Button(top,text="Hipervínculos",command=validarHiper)
btnAnalizarA.place(x=450, y=385)

txtUrl=Entry(top,width=70)
txtUrl.place(x=20,y=350)

top.mainloop()