from Nodo import usuario

class Control:

    def __init__(self):
        self.l = {}
    
    def regitrarUsuario(self, cc, nombre):
        u = usuario()
        u.cc = cc
        u.nombre = nombre
        self.l[cc] = u
    
    def registrarReferido(self, cc, cc_referido, nombre_referido):
        nu = usuario()
        nu.cc = cc_referido
        nu.nombre = nombre_referido
        u = self.l[cc]
        u.asignaReferido(cc_referido)
        self.l[cc_referido] = nu

    def registraPago(self, cc):
        u = self.l[cc]
        u.pagarCuota()



