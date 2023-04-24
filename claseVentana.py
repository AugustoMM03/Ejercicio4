class Ventana:
    
    def __init__(self, titulo = '', valorXSupIzq = 0, valorYSupIzq = 0, valorXInfDer = 100, valorYInfDer = 100):
        self.__titulo = titulo
        self.__valorXSupIzq = max(0,valorXSupIzq)
        self.__valorYSupIzq = max(0,valorYSupIzq)
        self.__valorXInfDer = min(500,valorXInfDer)
        self.__valorYInfDer = min(500,valorYInfDer)

        if self.__valorXSupIzq > self.__valorXInfDer:
            self.__valorXSupIzq, self.__valorXInfDer = self.__valorXInfDer, self.__valorXSupIzq
        if self.__valorYSupIzq > self.__valorYInfDer:
            self.__valorYSupIzq, self.__valorYInfDer = self.__valorYInfDer, self.__valorYSupIzq
    
    def mostrar(self):

        print("Ventana {} con vertice superior izquierdo ({}, {}) y vertice inferior derecho ({}, {})".format(self.__titulo, self.__valorXSupIzq, self.__valorYSupIzq, self.__valorXInfDer, self.__valorYInfDer))

    def alto(self):
        return self.__valorYInfDer - self.__valorYSupIzq

    def ancho(self):
        return self.__valorXInfDer - self.__valorXSupIzq

    def getTitulo(self):
        return self.__titulo

    def moverDerecha(self, xUnidades = 1):
        self.__valorXSupIzq = min(self.__valorXSupIzq + xUnidades, 500)
        self.__valorXInfDer = min(self.__valorXInfDer + xUnidades, 500)


    def moverIzquierda(self, xUnidades = 1):
        self.__valorYSupIzq = max(self.__valorYSupIzq - xUnidades, 0)
        self.__valorXInfDer = max(self.__valorXInfDer - xUnidades, 0)


    def subir(self, xUnidades = 1):
        self.__valorYSupIzq = min(self.__valorYSupIzq + xUnidades, 500)
        self.__valorYInfDer = min(self.__valorYInfDer + xUnidades, 500)
    
    def bajar(self, xUnidades = 1):
        self.__valorYSupIzq = max(self.__valorYSupIzq - xUnidades, 0)
        self.__valorYInfDer = max(self.__valorYInfDer - xUnidades, 0)