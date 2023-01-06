class comprador:
    nombre     = str
    ciudad     = str
    direccion  = str
    telefono   = str
    cedula     = str
    
    def __init__(self, nombre, ciudad, direccion, telefono, cedula):
        self.nombre     = nombre 
        self.ciudad     = ciudad
        self.direccion  = direccion
        self.telefono   = telefono
        self.cedula     = cedula
        
    def platicar (self, otro_comprador):
        return f'¡¡Hola!! {otro_comprador.nombre} ¡Gracias por tomar mis datos para el envio!, me llamo {self.nombre}, mi residencia esta en la ciudad de: {self.ciudad}, mi direccion para el envio es:{self.direccion}, me pueden contactar al: {self.telefono} y para la factura mi numero de cedula es: {self.cedula} '  
    
if __name__== "__main__" :
    Comprador1 = comprador("Estefania Maldonado", "quito", "las casas", "0988563214", "175487854")
    Comprador2 = comprador("Kerly Pantoja", "quito", "san vicente", "0921547855", "1736547895") 
    
    print(Comprador1.platicar(Comprador2))  