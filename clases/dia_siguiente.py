from getopt import gnu_getopt
from re import X


class ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def catastrofe(self):
        print("La ciudad "+str(self.nombre)+" ha sido destruida.")
        for persona in empleados:
            if persona.edificio.ciudad.nombre == self.nombre:
                print(str(persona.nombre)+" ha quedado desempleado por la catastrofe.")
                del(persona)
                print("El edificio "+str(persona.edificio)+" ha sido destruido.")
                del(persona.edificio)


class empleado:
    def __init__(self, nombre, empresa, edificio):
        self.nombre = nombre
        self.empresa = empresa
        self.edificio = edificio

class edificio:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

Nueva_York = ciudad("Nueva York")
Los_Angeles = ciudad("Los Angeles")
A = edificio("A", Nueva_York)
B = edificio("B", Nueva_York)
C = edificio("C", Los_Angeles)
Martin = empleado("Martin", "YooHoo!", A)
Xing = empleado("Xing", "YooHoo!", B)
Salim = empleado("Salim", "YooHoo!", C)
empleados = [Martin, Xing, Salim]
estatus = {"Nueva York": True, "Los Angeles": False}

def iniciar():
    print("Se acerca la destruccion del mundo. ¿Que ciudad caerá primero?,")
    genocidio = input("¿Nueva York(1) o Los Angeles(2)?: ")
    if genocidio == int:
        if genocidio == 1:
            Nueva_York.catastrofe()
        elif genocidio == 2:
            Los_Angeles.catastrofe()
        else:
            print("Seleccione una opción válida")
            iniciar()
    else:
        print("Seleccione una opción válida")
        iniciar()