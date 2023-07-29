from tkinter import *
from tkinter import messagebox
from cuadrado import cuadrado

class frmInicio:
    
    def proceder(self):
        if len(self.txtNumero.get())==0:
            messagebox.showerror("Error","Faltan datos")
        else:
            numero=int(self.txtNumero.get())
            self.lblResultado["text"]="Resultado :"+str(cuadrado.calcular(numero))

       
    
    def inicio(self):
        self.formulario = Tk()
        self.formulario.geometry("350x150")
        self.formulario.title("Calculadora Python T200")
    
        self.lblNumero = Label(self.formulario,text="Digite número")
        self.lblNumero.place(x=10, y=10)

        self.lblResultado = Label(self.formulario, text="Resultado: ")
        self.lblResultado.place(x=10, y=100)
        
        self.txtNumero = Entry(self.formulario)
        self.txtNumero.place(x=100,y=10)

        self.btnCalcular = Button(self.formulario, text="Cuadrado",command=self.proceder)
        self.btnCalcular.place(x=20,y=50)
    
    
        self.formulario.mainloop()
aplicacion = frmInicio()
aplicacion.inicio()

