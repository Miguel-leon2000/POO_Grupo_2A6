import math #Libreria math

class Ecuacion:  #Nombre de la clase
    __ValorA = int(0)
    __ValorB = int(0)
    __ValorC = int(0)              #Atributos de entrada y salida
    __ResultadoRaiz = float(0)
    __x1 = float(0)
    __x2 = float(0)

    def __init__(self, ValorA, ValorB, ValorC):  #Metodo constructor con atributos de entrada
        self.__ValorA = ValorA
        self.__ValorB = ValorB
        self.__ValorC = ValorC

    def calcularRaizCuadrada(self):  #Metodo para saber el resultado de la raiz cuadrada
        self.__ResultadoRaiz = (self.__ValorB * self.__ValorB) - 4 * self.__ValorA * self.__ValorC

        if(self.__ResultadoRaiz < 0):  #Condicion para el caso de que la raiz sea menor a 0
            self.__x1 = 0
            self.__x2 = 0
        else:    #Condicion "Si no", realiza las demas operaciones de manera normal
            self.__x1 = ((- self.__ValorB) + math.sqrt(self.__ResultadoRaiz)) / (2 * self.__ValorA)
            self.__x2 = ((- self.__ValorB) - math.sqrt(self.__ResultadoRaiz)) / (2 * self.__ValorA)

    def getx1(self):  #Metodos get para obtener los valores de los atributos (x1 y x2)
        return self.__x1

    def getx2(self):
        return self.__x2
