class producto:

    def __new__(cls,codigo,nombre):
        objeto=super(producto,cls).__new__(cls)
        return objeto
    
    def __init__(self,codigo,nombre):
        self.codigo=codigo
        self.nombre=nombre