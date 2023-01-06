class Vendedor:
    id       = int
    nombre   = str
    apellido = str
    edad     = str
        
    def __init__(self, id, nombre, apellido, edad):
        self.id       = id
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
        
    
class Empleado(Vendedor):
    ciudad = str
    
    def __init__(self, id, nombre, apellido, edad, ciudad):
        Vendedor.__init__(self, id, nombre, apellido, edad)
        self.ciudad = ciudad        
            
    def informar(self, otro_trabajador):
        return f"Buenos dias {otro_trabajador.nombre} {otro_trabajador.apellido} !!, nos comunicamos para tomar su pedido, ¿tiene {self.edad} años, cierto?. Un gusto en ayudarle, Yo me llamo {self.nombre} {self.apellido} y tengo {self.edad}. Nuestros pedidos solo los realizamos en {self.ciudad}, el codigo de su pedido es: {self.id} "

jefe = Vendedor(15, "Damian", "Chimborazo", 25)
empleado  = Empleado(16, "Fernanda", "Aconda", 25, "Quito")

print(empleado.informar(jefe)) 
        
