class Perceptron:

    def __init__(self):
        self.salida = 0
        self.pesos = []
        self.entradas = []
        self.error = []
        self.correccion = 0
        self.valor_esperado = 0
        self.umbral = 0.0
        self.tasa_aprendizaje = 0.1

    def preguntar(self, pregunta):
        self.pensarPerceptron(pregunta)
        print('la salida para ',pregunta, ' es ', self.salida)
        return self.salida

    def pensarPerceptron(self, entradas):
        print('pensando..')
        if self.productoEscalar(entradas, self.pesos) > self.umbral:
            self.salida = 1
        else:
            self.salida = 0

    def setUmbral(self,umbral):
        self.umbral = umbral
    
    def setTasaAprendizaje(self, tasa_aprendizaje):
        self.tasa_aprendizaje = tasa_aprendizaje
    
    def setEntradas(self, entradas, valor_esperado):
        n = len(entradas)
        self.entradas = entradas
        self.valor_esperado = valor_esperado
        self.error.clear()
        self.pesos.clear()
        #self.umbral = self.valor_esperado
        for x in range(n):
            self.pesos.append(0)
            self.error.append(0)
        #self.entrenar()

    def productoEscalar(self, entradas, pesos):
        res = 0
        for x, w in zip(self.entradas, self.pesos):
            res += x * w
        print('producto escalar ', res)
        return res
    
    def entrenar(self):
        interaciones = 0
        top = 20

        while True:
            #if self.productoEscalar(self.entradas, self.pesos) > self.umbral:
            #    self.salida = 1
            #else:
            #    self.salida = 0
            self.pensarPerceptron(self.entradas)
            print('comparando salida ', self.salida, ' con valor esperado ', self.valor_esperado)
            if self.salida != self.valor_esperado:
                print('no son iguales...')
                self.error = self.valor_esperado - self.salida
                self.correccion = self.tasa_aprendizaje * self.error
                print('error ', self.error, ' correccion ', self.correccion)
                i = 0
                print('calculando nuevos pesos...')
                for d in self.entradas:                    
                    w  = 0
                    w = (d * self.correccion) + self.pesos[0]
                    print('valor del peso ', w)
                    self.pesos[i] = w
            else:
                print('Entrenado con ', interaciones, ' interacciones, pesos finales:')
                print(self.pesos)
                break
            
            interaciones += 1
            if interaciones > top:
                top += top
                print('se han realizado ', interaciones, ' interacciones desea salir pres x')
                r = input()
                if r == 'x':
                    print('valores de entrada')
                    print(self.entradas)
                    print('valor esperado')
                    print(self.valor_esperado)
                    print('ultima salida del Perceptron')
                    print(self.salida)
                    print('ultima tabla de pesos')
                    print(self.pesos)
                    break
            
            

        



