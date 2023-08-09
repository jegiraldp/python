#libreria tkinter para IGU
from tkinter import *
#se importa la clase messagebox
from tkinter import messagebox
#import del archivo cuadrado la clase cuadrado
from cuadrado import cuadrado

class frmInicio:
    #self es la misma clase
    #proceder ejecuta lo que hace el boton cuadrado
    def proceder(self):
        if len(self.txtNumero.get())==0:
            #message box para mensaje emergente
            messagebox.showerror("Error","Faltan datos")
        else:
            numero=int(self.txtNumero.get())
            self.lblResultado["text"]="Resultado :"+str(cuadrado.calcular(numero))

       
    
    def inicio(self):
        #se crea el objeto formulario
        self.formulario = Tk()
        self.formulario.geometry("350x150")
        self.formulario.title("Calculadora Python T200")

        #label
        self.lblNumero = Label(self.formulario,text="Digite número")
        #place es para ubicar
        self.lblNumero.place(x=10, y=10)

        self.lblResultado = Label(self.formulario, text="Resultado: ")
        self.lblResultado.place(x=10, y=100)
        
        #entry es campo de texto
        self.txtNumero = Entry(self.formulario)
        self.txtNumero.place(x=100,y=10)

        self.btnCalcular = Button(self.formulario, text="Cuadrado",command=self.proceder)
        self.btnCalcular.place(x=20,y=50)
    
    
        self.formulario.mainloop()
aplicacion = frmInicio()
aplicacion.inicio()

