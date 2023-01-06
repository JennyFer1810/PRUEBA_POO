from clientes import Clientes

class Antiguos(Clientes):
    
    def __init__(self, id, nombre, apellido, email, edad, telefono, direccion):
        super().__init__(id, nombre, apellido, email, edad, telefono, direccion)
        
        