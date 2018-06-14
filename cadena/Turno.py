from Nodo import usuario
class Turno:
    def __init__(self):
        self.t = []
        self.turno = 0
        self.usuarioActual = usuario()

    def validarUsuario(self, usuario):
        u = usuario()
        u = usuario
        valid = False
        if u.estadopago == 'pagado' and u.cc_referido1 !='' and u.cc_referido2 !='' and u.estado_juego:
            valid = True
        return valid
    
    def ponerTurno(self, usuario):
        if self.validarUsuario(usuario):
            if len(self.t) == 0:
                self.usuarioActual = usuario
                self.t.append(self.usuarioActual)
            else: 
                if self.t[self.turno].reclamar():
                    self.turno += 1 if len(self.t)>self.turno else 0
                    self.t[self.turno].acumular()
                else:
                    self.t[self.turno].acumular()
                    u = usuario
                    self.t.append(u)
    

    def totalEnTurno(self):
        return len(self.t)

    

        
