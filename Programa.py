#1.registra usuario
#2.registra pago de usuario
#3.registra los 2 referidos
#4.regitra el pago de los 2 referidos
#5.autoriza la participacion del usuario y lo mete en la cola.
#6.permite consultar estado del acumulado del usuario.

from cadena import usuario

b = True
lusuarios = []


def getMenu():
    menu = '1.Ingresar Usuario \n2.Ingresar Referido \npresione x para salir'
    return menu

def validarOpcion(opcion):
    if opcion == '1':
        regirtroUsuario()
    elif opcion =='2':
        registroReferido()
    else:
        return 'Elija una Opcion Valida..'
    
def registroReferido():
    pass

def regirtroUsuario():
    u = usuario()
    print('Ingrese numero de cc')
    u.cc = input()
    print('ingrese Nombre de Usuario')
    u.nombre = input()
    print('usuario paga? s > si , n > no ')
    pago = input()
    if pago == 's':
        u.estadopago = 'Pago'
    else:
        u.estadopago = 'sin pago'
    
    lusuarios.append(u)
    print('usuario registrado con Exito!')






while b:
    print(getMenu())
    n = input()
    validarOpcion(n)
    if n =='x':
        b= False


