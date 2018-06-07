#1.registra usuario
#2.registra pago de usuario
#3.registra los 2 referidos
#4.regitra el pago de los 2 referidos
#5.autoriza la participacion del usuario y lo mete en la cola.
#6.permite consultar estado del acumulado del usuario.

####
class usuario:
    cc = '0'
    valor = 25000
    nombre = 'sin nombre'
    turno = 0
    estadopago = 'sin pago'
    estadopremio = 'acumulando'
    acumulado = 0
    referidos = 0

    def __init__(self):
        self.cc = '0'
        self.valor = 25000
        self.nombre = 'sin nombre'
        self.turno = 0
        self.estadopago = 'sin pago'
        self.estadopremio = 'acumulando'
        self.acumulado = 0
        self.referidos = 0
    
    def asigna_Referido(self):
        msg = ''
        if self.referidos < 2:
            self.referidos +=1
            msg = 'asignado'
        else:
            msg = 'ya cumplio sus referidos'
        return msg
    

    def acumular(self):
        msg = ''
        if self.acumulado < 10:
            self.acumulado +=1
            msg = 'ok'
        else:
            self.estadopremio = 'listo para pago'
            msg = 'ya se llego a tope'
        return msg

    def retira_Premio(self):
        msg = ''
        if self.acumulado == 10:
            self.estadopremio = 'pagado'
            msg = 'ha ganado ' + str(self.acumulado * self.valor)
        else:
            msg = 'no se puede retirar premio'
        return msg

        
        
    
        
    
            
            
