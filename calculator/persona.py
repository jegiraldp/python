class persona:

    def __init__(self, documento, nombre, edad):
        print("hola desde el __init__")
        self.documento=documento
        self.nombre=nombre
        self.edad=edad

    def __new__(cls,documento,nombre,edad):
        print("hola desde __new__")
        objeto=super(persona,cls).__new__(cls)
        return objeto    
        

