from clientesActual import Actual
from clientesAntiguo import Antiguos

class ClientesTotal(Actual, Antiguos):
    idCliente   = int
    actual      = Actual("", "", "", "", "", "", "")
    antiguos    = Antiguos("", "", "", "", "","", "")

    def __init__(self, idCliente, actual, antiguos):
        self.idCliente    = idCliente
        self.actual      = actual
        self.antiguos    = antiguos
