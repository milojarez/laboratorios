import random
from Nodo import usuario
nombresh = ['Pedro', 'Camilo', 'Olmes', 'Jose', 'Enrique', 'David', 'Arturo','Omar']
nombresm = ['Sofia','Isabel','Antonia','Abril','Daniela', 'Angela','Patricia','Judith']
apellidos = ['Jaramillo','Ramirez','Lopez','Aristizabal','Bermudez','Buitrago']
r = random

def generarNombres():
    for x in range (10):
        n1 = r.randrange(len(nombresh))
        n2 = r.randrange(len(nombresh))
        a1 = r.randrange(len(apellidos))
        a2 = r.randrange(len(apellidos))
        if n1 == n2 :
            n = '{0} {1} {2}'.format(nombresh[n1], apellidos[a1], apellidos[a2])
        else:
            n = '{0} {1} {2} {3}'.format(nombresh[n1], nombresh[n2], apellidos[a1], apellidos[a2])
        print(x, ' ->', n)

def getNombreRandom():
    n = ''
    n1 = r.randrange(len(nombresh))
    n2 = r.randrange(len(nombresh))
    a1 = r.randrange(len(apellidos))
    a2 = r.randrange(len(apellidos))
    if n1 == n2 :
        n = '{0} {1} {2}'.format(nombresh[n1], apellidos[a1], apellidos[a2])
    else:
        n = '{0} {1} {2} {3}'.format(nombresh[n1], nombresh[n2], apellidos[a1], apellidos[a2])
    return n

def getCedulaRandom():
    return r.randrange(9999999999)

def dic():
    lista = {}
    u = usuario()
    u.cc = getCedulaRandom()
    u.nombre = getNombreRandom()
    lista[u.cc]= u
    
