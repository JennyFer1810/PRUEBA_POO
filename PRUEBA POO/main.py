from clientesActual import Actual
from clientesAntiguo import Antiguos
from clientesTotal import ClientesTotal

if __name__ == "__main__":
        
    print("Clientes Actuales:")
    clientesActual2 = Actual(25, "Kerlly", "Aconda", "kerlly1546gmail.com", 22, "098546923", "Las casas")
    print(vars(clientesActual2))
    
    print("Clientes Actuales:") 
    clientesActual1 = Actual(18, "Jennyfer", "Chalacan", "jenny1810@gmail.com", 22, "098974536", "la comuna")
    print(vars(clientesActual1))
    
    print("Clientes Antiguos:")
    clientesAntiguo1 = Antiguos(10, "Jonathan", "Diaz", "jonathan6523gmail.com", 25, "09965874", "La comuna alta")
    print(vars(clientesAntiguo1))
    
    print("Clientes Antiguos:")
    clientesAntiguo2 = Antiguos(73, "Jefferson", "Chimborazo", "jefferson4852gmail.com", 21, "095784562", "el reten")
    print(vars(clientesAntiguo2))
    
    
    print("Clientes total:")
    clientesTotal1 = ClientesTotal(15, Actual(18, "Jennyfer", "Chalacan", "jenny1810@gmail.com", 22, "098974536", "la comuna"), Antiguos(10, "Jonathan", "Diaz", "jonathan6523gmail.com", 25, "09965874", "La comuna alta"))
    print(vars(clientesTotal1))
    print(vars(clientesTotal1.antiguos))
    print(vars(clientesTotal1.actual))
   
