from perceptronv0 import Perceptron
ne = Perceptron()
ne.setUmbral = 0.5
lista = [1,0,0]
ne.setEntradas(lista,1)
ne.entrenar()
print('primera prueba')
ne.preguntar(lista)
print('segunda prueba')
lista2 = [1,1,0]
ne.setEntradas(lista2,0)
ne.preguntar(lista2)