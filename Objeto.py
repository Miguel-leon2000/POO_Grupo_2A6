from Ecuacion import Ecuacion

Soluciones = Ecuacion(2, 5, 2)  #Se le asigna valores al parametro del metodo constructor de la clase "Ecuacion"

Soluciones.calcularRaizCuadrada()  #Se manda llamar al metodo "calcularRaizCuadrada"

print("------------Soluciones Reales---------------")

print ("El resultado de x1 es: ", Soluciones.getx1())  #Imprime mensajes para saber las soluciones de x1 y x2

print ("El resultado de x2 es: ", Soluciones.getx2())
