from clientes import Clientes

class Actual(Clientes):
    
    cuenta = str
    genero = str
    
    def __init__(self, id, nombre, edad, telefono, direccion, cuenta, genero):
        super().__init__(id, nombre, edad, telefono, direccion, cuenta, genero)
        
        self.cuenta = cuenta
        self.genero = genero
        
        
        