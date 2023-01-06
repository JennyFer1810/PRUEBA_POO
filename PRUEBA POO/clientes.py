class Clientes:
    id        = int
    nombre    = str
    apellido  = str
    email     = str
    edad      = int
    telefono  = int
    direccion = str

    def __init__(self, id, nombre, apellido, email, edad, telefono, direccion ):
        self.id        = id
        self.nombre    = nombre
        self.apellido  = apellido
        self.email     = email
        self.edad      = edad
        self.telefono  = telefono
        self.direccion = direccion
        
    def __str__(self):
        return f"El nombre de nuestra cliente es {self.nombre} {self.apellido}, su correo es:{self.email}, su edad es: {self.edad} años, su telefono es: {self.telefono}, y su direccion es: {self.direccion} "
       
cliente1 = Clientes (12, "Jessica", "Bosquez", "jessica22@gmail.com", 21, "0987452136", "La comuna")
print(cliente1)
