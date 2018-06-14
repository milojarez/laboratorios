class usuario:    
    
    def __init__(self):
        self.cc = ''
        self.nombre = ''
        self.referidos = 0
        self.acumulado = 0
        self.estadopago = 'pendiente'
        self.estadopremio = 'esperando referidos'
        self.estado_juego = True
        self.cc_referido1 = ''
        self.cc_referido2 = ''
    

    def asignaReferido(self, cc_referido):
        if self.referidos <2 and self.estadopago =='pagado':
            self.referidos += 1
            if self.cc_referido1 == '':
                self.cc_referido1 = cc_referido
            else:
                self.cc_referido2 = cc_referido
        else:
            self.estadopremio = 'acumulando'
    
    def acumular(self):
        if self.estadopago =='pagado' and self.cc_referido1 != '' and self.cc_referido2 !='' and self.acumulado < 10:
            self.acumulado += 1
        else:
            self.estadopremio = 'por reclamar'
    
    def reclamar(self):
        if self.referidos ==2 and self.acumulado ==10:
            self.estadopremio = 'reclamado'
            self.estado_juego = False
        return not self.estado_juego
    
    def pagarCuota(self):
        self.estadopago = 'pagado'
